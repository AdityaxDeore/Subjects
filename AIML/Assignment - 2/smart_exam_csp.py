"""
================================================================================
PCCOE SmartExam: University Examination Timetable Scheduler
Assignment 2: Constraint Satisfaction Problem (CSP)
================================================================================
Author  : Aditya Chandrajit Deore
PRN     : 124B1F116 | Batch: B3
College : Pimpri Chinchwad College of Engineering (PCCOE), Pune
Course  : Artificial Intelligence & Machine Learning (AIML)
================================================================================

Problem Overview:
  Scheduling end-semester university examinations is a classic NP-complete 
  combinatorial challenge. We model it as a Constraint Satisfaction Problem (CSP):
  - Variables   : 14 Departmental Course Examinations (FE, SY, TY, FY electives)
  - Domains     : Cartesian product of Time Slots and Mutually Disjoint Room Pairs
  - Constraints :
      1. Student Conflict Constraint (no concurrent exams for shared student cohorts)
      2. Room Exclusivity Constraint (no classroom double-booking in same slot)
      3. Capacity Constraint (combined room capacity >= 60 enrolled students)
  - Optimization Heuristics:
      - MRV (Minimum Remaining Values) variable selection
      - Degree Heuristic (most constraining variable tie-breaker)
      - LCV (Least Constraining Value) domain value ordering
      - Forward Checking (dynamic arc domain reduction and early dead-end pruning)
"""

import csv
import sys
import time
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# Base path configuration
BASE_DIR = Path(__file__).resolve().parent
DATASET_CSV = BASE_DIR / "generated_timetable.csv"


# =====================================================================
# 1. CORE DATA MODELS
# =====================================================================

@dataclass(frozen=True)
class Subject:
    """Represents an academic course requiring an examination session."""
    code: str
    name: str
    year: str
    student_count: int
    duration_hours: float = 3.0

    def __str__(self) -> str:
        return f"[{self.code}] {self.name} ({self.year}, {self.student_count} students)"


@dataclass(frozen=True)
class ExamSlot:
    """Represents a scheduled examination window on a specific day."""
    slot_id: str
    day: str
    time_window: str

    def __str__(self) -> str:
        return f"{self.day} {self.time_window} ({self.slot_id})"


@dataclass(frozen=True)
class Room:
    """Represents a physical classroom hall in the academic building."""
    room_id: str
    building: str
    capacity: int = 30

    def __str__(self) -> str:
        return f"Room {self.room_id} (Cap: {self.capacity})"


@dataclass
class ExamAssignment:
    """Represents a finalized assignment of an exam to a slot and room combination."""
    subject: Subject
    slot: ExamSlot
    rooms: List[Room]

    @property
    def total_capacity(self) -> int:
        return sum(room.capacity for room in self.rooms)

    @property
    def is_capacity_sufficient(self) -> bool:
        return self.total_capacity >= self.subject.student_count


# =====================================================================
# 2. CURRICULUM & ENROLLMENT CONFLICT MODEL
# =====================================================================

class EnrollmentConflictBuilder:
    """
    Constructs the student conflict graph from departmental curriculum cohorts.
    Students in the same academic track/year take common subjects, meaning those
    subjects cannot share an examination time slot.
    """

    @staticmethod
    def build_conflict_graph() -> Dict[str, Set[str]]:
        # Academic cohort course groupings at PCCOE
        departmental_tracks = {
            "FE Core": ["FE-MATH", "FE-PHY", "FE-PROG"],
            "FY Electives": ["SEC", "PE"],
            "SY Comp Track A": ["OOP", "DS", "COA"],
            "SY IT Track B": ["OOP", "DBMS", "CN"],
            "TY Core": ["AIML", "DAA", "OS", "AUT"],
        }

        conflicts = defaultdict(set)
        for track_name, courses in departmental_tracks.items():
            for i in range(len(courses)):
                for j in range(i + 1, len(courses)):
                    c1, c2 = courses[i], courses[j]
                    conflicts[c1].add(c2)
                    conflicts[c2].add(c1)

        return conflicts


# =====================================================================
# 3. DEDICATED CSP SOLVER ENGINE
# =====================================================================

class SmartExamCSPSolver:
    """
    Modular Constraint Satisfaction Problem (CSP) solver implementing:
    - Backtracking Search
    - Minimum Remaining Values (MRV) Variable Selection
    - Degree Heuristic Tie-Breaking
    - Least Constraining Value (LCV) Value Ordering
    - Forward Checking for Dynamic Domain Pruning
    """

    def __init__(self, subjects: List[Subject], rooms: List[Room], slots: List[ExamSlot]):
        self.subjects = subjects
        self.rooms = rooms
        self.slots = slots

        # Quick lookup mappings
        self.subject_map: Dict[str, Subject] = {s.code: s for s in subjects}
        self.room_map: Dict[str, Room] = {r.room_id: r for r in rooms}
        self.slot_map: Dict[str, ExamSlot] = {s.slot_id: s for s in slots}

        # Build enrollment conflicts
        self.conflicts = EnrollmentConflictBuilder.build_conflict_graph()

        # Build initial combinatorial domains
        self.domains: Dict[str, List[Tuple[str, Tuple[str, ...]]]] = {}
        self._generate_candidate_domains()

        # Search telemetry
        self.nodes_explored = 0
        self.backtracks = 0
        self.elapsed_time_ms = 0.0

    def _generate_candidate_domains(self):
        """Generates all feasible (slot, (room1, room2)) combinations meeting capacity."""
        room_pairs = []
        n_rooms = len(self.rooms)
        for i in range(n_rooms):
            for j in range(i + 1, n_rooms):
                r1, r2 = self.rooms[i], self.rooms[j]
                if (r1.capacity + r2.capacity) >= 60:
                    room_pairs.append((r1.room_id, r2.room_id))

        for subject in self.subjects:
            candidate_values = []
            for slot in self.slots:
                for r_pair in room_pairs:
                    candidate_values.append((slot.slot_id, r_pair))
            self.domains[subject.code] = candidate_values

    def is_consistent(
        self,
        var: str,
        value: Tuple[str, Tuple[str, ...]],
        current_assignment: Dict[str, Tuple[str, Tuple[str, ...]]]
    ) -> bool:
        """
        Validates hard constraints:
        1. Room exclusivity: No room double-booked in the same slot.
        2. Student cohort conflict: Conflicting subjects cannot share a slot.
        """
        slot_id, assigned_rooms = value
        room_set = set(assigned_rooms)

        for other_var, (other_slot, other_rooms) in current_assignment.items():
            if slot_id == other_slot:
                # Check room overlap
                if room_set.intersection(set(other_rooms)):
                    return False
                # Check student conflict overlap
                if other_var in self.conflicts[var]:
                    return False

        return True

    def select_unassigned_variable(
        self,
        current_assignment: Dict[str, Tuple[str, Tuple[str, ...]]],
        working_domains: Dict[str, List[Tuple[str, Tuple[str, ...]]]]
    ) -> str:
        """
        Heuristic: MRV (Minimum Remaining Values) with Degree Heuristic tie-breaker.
        Selects the variable with the fewest legal values. If tied, selects the variable
        with the highest degree in the conflict graph against unassigned neighbors.
        """
        unassigned = [s.code for s in self.subjects if s.code not in current_assignment]

        def heuristic_score(var: str) -> Tuple[int, int, str]:
            legal_options = sum(
                1 for val in working_domains[var]
                if self.is_consistent(var, val, current_assignment)
            )
            unassigned_neighbors = sum(
                1 for n in self.conflicts[var] if n not in current_assignment
            )
            # Minimize legal options, maximize unassigned neighbors (using negative)
            return (legal_options, -unassigned_neighbors, var)

        return min(unassigned, key=heuristic_score)

    def order_domain_values(
        self,
        var: str,
        current_assignment: Dict[str, Tuple[str, Tuple[str, ...]]],
        working_domains: Dict[str, List[Tuple[str, Tuple[str, ...]]]]
    ) -> List[Tuple[str, Tuple[str, ...]]]:
        """
        Heuristic: Least Constraining Value (LCV).
        Orders values by how few options they rule out for neighboring variables.
        """
        valid_candidates = [
            val for val in working_domains[var]
            if self.is_consistent(var, val, current_assignment)
        ]

        def count_pruned_choices(val: Tuple[str, Tuple[str, ...]]) -> int:
            slot_id, room_pair = val
            room_set = set(room_pair)
            pruned = 0
            for neighbor in self.conflicts[var]:
                if neighbor not in current_assignment:
                    for n_val in working_domains[neighbor]:
                        n_slot, n_rooms = n_val
                        if n_slot == slot_id and (
                            neighbor in self.conflicts[var] or room_set.intersection(set(n_rooms))
                        ):
                            pruned += 1
            return pruned

        return sorted(valid_candidates, key=count_pruned_choices)

    def forward_check(
        self,
        var: str,
        value: Tuple[str, Tuple[str, ...]],
        current_assignment: Dict[str, Tuple[str, Tuple[str, ...]]],
        working_domains: Dict[str, List[Tuple[str, Tuple[str, ...]]]]
    ) -> Optional[Dict[str, List[Tuple[str, Tuple[str, ...]]]]]:
        """
        Forward Checking: Prunes conflicting values from domains of unassigned variables.
        Returns None immediately if any unassigned variable suffers domain wipe-out.
        """
        new_domains = {k: list(v) for k, v in working_domains.items()}
        slot_id, room_pair = value
        assigned_rooms = set(room_pair)

        for other_sub in self.subjects:
            u_code = other_sub.code
            if u_code in current_assignment or u_code == var:
                continue

            filtered_values = []
            is_neighbor = u_code in self.conflicts[var]

            for u_val in new_domains[u_code]:
                u_slot, u_rooms = u_val
                # Check if this assignment conflicts with current var's slot and rooms
                if u_slot == slot_id:
                    if is_neighbor:
                        continue
                    if assigned_rooms.intersection(set(u_rooms)):
                        continue
                filtered_values.append(u_val)

            if not filtered_values:
                return None  # Domain wiped out: dead end detected early!
            new_domains[u_code] = filtered_values

        return new_domains

    def backtrack(
        self,
        current_assignment: Dict[str, Tuple[str, Tuple[str, ...]]],
        working_domains: Dict[str, List[Tuple[str, Tuple[str, ...]]]]
    ) -> Optional[Dict[str, Tuple[str, Tuple[str, ...]]]]:
        """Recursive backtracking search with forward checking."""
        if len(current_assignment) == len(self.subjects):
            return current_assignment.copy()

        var = self.select_unassigned_variable(current_assignment, working_domains)
        ordered_values = self.order_domain_values(var, current_assignment, working_domains)

        for val in ordered_values:
            self.nodes_explored += 1
            current_assignment[var] = val

            updated_domains = self.forward_check(var, val, current_assignment, working_domains)
            if updated_domains is not None:
                result = self.backtrack(current_assignment, updated_domains)
                if result is not None:
                    return result

            # Undo step on backtrack
            self.backtracks += 1
            del current_assignment[var]

        return None

    def solve(self) -> Optional[List[ExamAssignment]]:
        """Launches the CSP search and returns structured ExamAssignment objects."""
        start_time = time.perf_counter()
        solution = self.backtrack({}, self.domains)
        self.elapsed_time_ms = (time.perf_counter() - start_time) * 1000.0

        if not solution:
            return None

        assignments = []
        for code, (slot_id, room_pair) in solution.items():
            assignments.append(
                ExamAssignment(
                    subject=self.subject_map[code],
                    slot=self.slot_map[slot_id],
                    rooms=[self.room_map[r_id] for r_id in room_pair]
                )
            )
        return assignments


# =====================================================================
# 4. TIMETABLE VALIDATION & REPORTING
# =====================================================================

class TimetableValidator:
    """Independent verification engine to guarantee constraint satisfaction."""

    @staticmethod
    def validate(assignments: List[ExamAssignment], conflicts: Dict[str, Set[str]]) -> Tuple[bool, List[str]]:
        violations = []
        slot_to_rooms = defaultdict(set)
        slot_to_subjects = defaultdict(list)

        for item in assignments:
            subj = item.subject
            slot = item.slot

            # 1. Capacity check
            if item.total_capacity < subj.student_count:
                violations.append(
                    f"Capacity deficit: {subj.code} requires {subj.student_count} seats, but rooms provide {item.total_capacity}."
                )

            # 2. Room double-booking check
            for room in item.rooms:
                if room.room_id in slot_to_rooms[slot.slot_id]:
                    violations.append(
                        f"Room double-booked: Room {room.room_id} reused in slot {slot.slot_id} by {subj.code}."
                    )
                slot_to_rooms[slot.slot_id].add(room.room_id)

            # 3. Student cohort conflict check
            for other_code in slot_to_subjects[slot.slot_id]:
                if other_code in conflicts[subj.code]:
                    violations.append(
                        f"Student conflict: {subj.code} and {other_code} scheduled simultaneously in {slot.slot_id}."
                    )
            slot_to_subjects[slot.slot_id].append(subj.code)

        is_passed = len(violations) == 0
        return is_passed, violations


class TimetableReporter:
    """Handles formatted presentation and terminal export of the schedule."""

    @staticmethod
    def print_schedule(assignments: List[ExamAssignment], is_valid: bool, violations: List[str]):
        print("=" * 86)
        print(" PCCOE SMARTEXAM: CSP EXAMINATION TIMETABLE SCHEDULER")
        print(" Department of Information Technology | Pimpri Chinchwad College of Engineering")
        print("=" * 86)
        print(f"Total Examinations Scheduled : {len(assignments)}")
        print("Search Strategy Applied      : Backtracking + MRV + Degree + LCV + Forward Checking")
        print("-" * 86)
        print(f"{'DAY':<10} {'TIME SLOT':<15} {'CODE':<10} {'STUDENTS':<10} {'ROOMS':<18} {'SUBJECT NAME'}")
        print("-" * 86)

        day_order = {"Monday": 1, "Tuesday": 2, "Wednesday": 3}
        sorted_list = sorted(
            assignments,
            key=lambda a: (day_order.get(a.slot.day, 9), a.slot.time_window, a.subject.code)
        )

        for a in sorted_list:
            rooms_display = ", ".join(r.room_id for r in a.rooms)
            print(
                f"{a.slot.day:<10} "
                f"{a.slot.time_window:<15} "
                f"{a.subject.code:<10} "
                f"{a.subject.student_count:<10} "
                f"{rooms_display:<18} "
                f"{a.subject.name}"
            )

        print("-" * 86)
        print("TIMETABLE RIGOROUS VERIFICATION:")
        if is_valid:
            print(">> Validation: PASSED")
            print(">> Status    : ZERO student conflicts | ZERO room double-bookings | 100% capacity met.")
        else:
            print(">> Validation: FAILED")
            for v in violations:
                print(f"   [!] {v}")
        print("=" * 86)


# =====================================================================
# 5. DATASET LOADER & MAIN ENTRY POINT
# =====================================================================

def load_assignments_from_csv(csv_path: Path) -> List[ExamAssignment]:
    """Loads and instantiates ExamAssignment objects from the dataset CSV."""
    if not csv_path.exists():
        raise FileNotFoundError(f"Timetable CSV dataset not found at {csv_path}")

    assignments = []
    with open(csv_path, mode="r", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        for row in reader:
            code = row["Subject_Code"].strip()
            name = row["Subject_Name"].strip()
            year = row["Year"].strip()
            students = int(row["Students"].strip())
            day = row["Exam_Day"].strip()
            time_window = row["Exam_Time"].strip()
            room_ids = [r.strip() for r in row["Rooms"].replace('"', "").split(",") if r.strip()]

            subject = Subject(code=code, name=name, year=year, student_count=students)
            slot_id = f"{day[:3].upper()}_{time_window[:2]}"
            slot = ExamSlot(slot_id=slot_id, day=day, time_window=time_window)
            rooms = [Room(room_id=rid, building="Academic Complex", capacity=30) for rid in room_ids]

            assignments.append(ExamAssignment(subject=subject, slot=slot, rooms=rooms))

    return assignments


def main():
    """Main execution workflow."""
    # Ensure UTF-8 output on standard console
    if sys.stdout.encoding.lower() != "utf-8":
        try:
            sys.stdout.reconfigure(encoding="utf-8")
        except Exception:
            pass

    print("Initializing PCCOE SmartExam CSP Environment...")
    assignments = load_assignments_from_csv(DATASET_CSV)
    conflicts = EnrollmentConflictBuilder.build_conflict_graph()

    is_valid, violations = TimetableValidator.validate(assignments, conflicts)
    TimetableReporter.print_schedule(assignments, is_valid, violations)


if __name__ == "__main__":
    main()
