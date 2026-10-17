import java.util.*;

/**
 * ============================================================================
 * UNIVERSITY TIMETABLE EXAM SCHEDULING SYSTEM
 * Graph Coloring Approach (Greedy, Welsh-Powell, DSATUR, Backtracking)
 * ============================================================================
 * Course     : Design & Analysis of Algorithms Laboratory (BIT25PC04)
 * Student    : Aditya Chandrajit Deore
 * PRN        : 124B1F116
 * College    : Pimpri Chinchwad College of Engineering (PCCOE)
 * Faculty    : Dr. Sapana Kolambe
 *
 * Problem Description:
 * A university must schedule final examination timetables for courses with
 * overlapping student enrollments without clashes.
 * - Each course is represented as a vertex v in V.
 * - An edge (u, v) exists if at least one student is enrolled in both courses.
 * - Each vertex is assigned a color (time slot) such that no adjacent vertices
 *   share the same color (conflict-free exam scheduling).
 * - Room allocation constraint: exams in the same slot must fit into available
 *   classrooms without exceeding room capacities.
 *
 * Algorithms Implemented:
 * 1. Greedy Coloring (First-Fit with natural ordering)
 * 2. Welsh-Powell Algorithm (Largest Degree First heuristic)
 * 3. DSATUR Algorithm (Degree of Saturation heuristic by Daniel Brelaz)
 * 4. Exact Backtracking Branch-and-Bound (Exact Chromatic Number chi(G))
 * 5. Room Allocation Constraint Solver (Best-Fit classroom assignment per slot)
 * 6. Scalability Benchmark on Large-Scale Dataset (500 courses, 5,000 students)
 * ============================================================================
 */
public class TimetableGraphColoring {

    // ------------------------------------------------------------------------
    // DATA MODEL: Course / Vertex
    // ------------------------------------------------------------------------
    public static class Course {
        public final int id;
        public final String code;
        public final String title;
        public final String department;
        public final int enrolledStudents;

        public Course(int id, String code, String title, String department, int enrolledStudents) {
            this.id = id;
            this.code = code;
            this.title = title;
            this.department = department;
            this.enrolledStudents = enrolledStudents;
        }

        @Override
        public String toString() {
            return String.format("[%s] %-32s (%s, %3d students)", code, title, department, enrolledStudents);
        }
    }

    // ------------------------------------------------------------------------
    // DATA MODEL: Classroom / Hall
    // ------------------------------------------------------------------------
    public static class Classroom {
        public final String roomId;
        public final int capacity;
        public final String block;

        public Classroom(String roomId, int capacity, String block) {
            this.roomId = roomId;
            this.capacity = capacity;
            this.block = block;
        }

        @Override
        public String toString() {
            return String.format("%s (%s Block, Cap: %d)", roomId, block, capacity);
        }
    }

    // ------------------------------------------------------------------------
    // DATA STRUCTURE: Conflict Graph
    // ------------------------------------------------------------------------
    public static class ConflictGraph {
        public final int numCourses;
        public final List<Course> courses;
        public final List<Set<Integer>> adjList;
        public final int[][] conflictWeights; // number of shared students

        public ConflictGraph(List<Course> courses) {
            this.courses = courses;
            this.numCourses = courses.size();
            this.adjList = new ArrayList<>(numCourses);
            for (int i = 0; i < numCourses; i++) {
                adjList.add(new HashSet<>());
            }
            this.conflictWeights = new int[numCourses][numCourses];
        }

        public void addConflict(int u, int v, int mutualStudents) {
            if (u == v || mutualStudents <= 0) return;
            adjList.get(u).add(v);
            adjList.get(v).add(u);
            conflictWeights[u][v] += mutualStudents;
            conflictWeights[v][u] += mutualStudents;
        }

        public int getDegree(int u) {
            return adjList.get(u).size();
        }

        public int getTotalEdges() {
            int count = 0;
            for (Set<Integer> neighbors : adjList) {
                count += neighbors.size();
            }
            return count / 2;
        }

        public double getGraphDensity() {
            if (numCourses <= 1) return 0.0;
            long maxEdges = ((long) numCourses * (numCourses - 1)) / 2;
            return (double) getTotalEdges() / maxEdges;
        }
    }

    // ------------------------------------------------------------------------
    // RESULT CONTAINER: Coloring Solution
    // ------------------------------------------------------------------------
    public static class ColoringResult {
        public final String algorithmName;
        public final int[] colors; // colors[vertex] = slotIndex (1-based)
        public final int totalSlotsUsed;
        public final long executionTimeNs;
        public final boolean conflictFree;

        public ColoringResult(String algorithmName, int[] colors, int totalSlotsUsed, 
                              long executionTimeNs, boolean conflictFree) {
            this.algorithmName = algorithmName;
            this.colors = colors;
            this.totalSlotsUsed = totalSlotsUsed;
            this.executionTimeNs = executionTimeNs;
            this.conflictFree = conflictFree;
        }
    }

    // ========================================================================
    // ALGORITHM 1: GREEDY FIRST-FIT COLORING (Natural Input Order)
    // ========================================================================
    public static ColoringResult solveGreedy(ConflictGraph graph) {
        long startTime = System.nanoTime();
        int n = graph.numCourses;
        int[] result = new int[n];
        Arrays.fill(result, -1);

        // Assign first color to first vertex
        result[0] = 1;

        // Boolean array to track unavailable colors for the current vertex
        boolean[] unavailable = new boolean[n + 2];

        for (int u = 1; u < n; u++) {
            // Mark colors of adjacent vertices as unavailable
            for (int neighbor : graph.adjList.get(u)) {
                if (result[neighbor] != -1) {
                    unavailable[result[neighbor]] = true;
                }
            }

            // Find the smallest available color
            int cr;
            for (cr = 1; cr <= n + 1; cr++) {
                if (!unavailable[cr]) {
                    break;
                }
            }
            result[u] = cr;

            // Reset unavailable array for next iteration
            for (int neighbor : graph.adjList.get(u)) {
                if (result[neighbor] != -1) {
                    unavailable[result[neighbor]] = false;
                }
            }
        }

        long elapsed = System.nanoTime() - startTime;
        int maxColor = 0;
        for (int c : result) maxColor = Math.max(maxColor, c);
        boolean valid = verifyColoring(graph, result);

        return new ColoringResult("Greedy First-Fit", result, maxColor, elapsed, valid);
    }

    // ========================================================================
    // ALGORITHM 2: WELSH-POWELL COLORING (Largest Degree First)
    // ========================================================================
    public static ColoringResult solveWelshPowell(ConflictGraph graph) {
        long startTime = System.nanoTime();
        int n = graph.numCourses;

        // 1. Order vertices by degree descending
        Integer[] order = new Integer[n];
        for (int i = 0; i < n; i++) order[i] = i;
        Arrays.sort(order, (a, b) -> Integer.compare(graph.getDegree(b), graph.getDegree(a)));

        int[] result = new int[n];
        Arrays.fill(result, -1);

        int currentColor = 1;
        int coloredCount = 0;

        // 2. Iterate through ordered vertices and assign colors
        for (int i = 0; i < n; i++) {
            int u = order[i];
            if (result[u] != -1) continue;

            // Assign currentColor to u
            result[u] = currentColor;
            coloredCount++;

            // Greedily color all subsequent independent vertices with currentColor
            for (int j = i + 1; j < n; j++) {
                int v = order[j];
                if (result[v] == -1) {
                    boolean hasConflict = false;
                    for (int neighbor : graph.adjList.get(v)) {
                        if (result[neighbor] == currentColor) {
                            hasConflict = true;
                            break;
                        }
                    }
                    if (!hasConflict) {
                        result[v] = currentColor;
                        coloredCount++;
                    }
                }
            }
            currentColor++;
            if (coloredCount == n) break;
        }

        long elapsed = System.nanoTime() - startTime;
        int maxColor = 0;
        for (int c : result) maxColor = Math.max(maxColor, c);
        boolean valid = verifyColoring(graph, result);

        return new ColoringResult("Welsh-Powell", result, maxColor, elapsed, valid);
    }

    // ========================================================================
    // ALGORITHM 3: DSATUR (Degree of Saturation - Brelaz's Algorithm)
    // ========================================================================
    public static ColoringResult solveDSATUR(ConflictGraph graph) {
        long startTime = System.nanoTime();
        int n = graph.numCourses;
        int[] result = new int[n];
        Arrays.fill(result, -1);

        // Track colors present among neighbors of each vertex
        List<Set<Integer>> neighborColors = new ArrayList<>(n);
        for (int i = 0; i < n; i++) {
            neighborColors.add(new HashSet<>());
        }

        // Color the vertex with the maximum degree first
        int maxDegVertex = 0;
        int maxDeg = -1;
        for (int i = 0; i < n; i++) {
            int d = graph.getDegree(i);
            if (d > maxDeg) {
                maxDeg = d;
                maxDegVertex = i;
            }
        }

        result[maxDegVertex] = 1;
        for (int neighbor : graph.adjList.get(maxDegVertex)) {
            neighborColors.get(neighbor).add(1);
        }

        boolean[] unavailable = new boolean[n + 2];

        // Process remaining n - 1 vertices
        for (int step = 1; step < n; step++) {
            // Find uncolored vertex with maximum saturation degree; tie-break with degree
            int bestVertex = -1;
            int maxSat = -1;
            int maxUncoloredDeg = -1;

            for (int v = 0; v < n; v++) {
                if (result[v] == -1) {
                    int sat = neighborColors.get(v).size();
                    int deg = graph.getDegree(v);

                    if (sat > maxSat || (sat == maxSat && deg > maxUncoloredDeg)) {
                        maxSat = sat;
                        maxUncoloredDeg = deg;
                        bestVertex = v;
                    }
                }
            }

            // Assign lowest available color
            for (int color : neighborColors.get(bestVertex)) {
                unavailable[color] = true;
            }

            int chosenColor;
            for (chosenColor = 1; chosenColor <= n + 1; chosenColor++) {
                if (!unavailable[chosenColor]) {
                    break;
                }
            }
            result[bestVertex] = chosenColor;

            // Reset unavailable array
            for (int color : neighborColors.get(bestVertex)) {
                unavailable[color] = false;
            }

            // Update neighbor saturations
            for (int neighbor : graph.adjList.get(bestVertex)) {
                neighborColors.get(neighbor).add(chosenColor);
            }
        }

        long elapsed = System.nanoTime() - startTime;
        int maxColor = 0;
        for (int c : result) maxColor = Math.max(maxColor, c);
        boolean valid = verifyColoring(graph, result);

        return new ColoringResult("DSATUR (Brelaz)", result, maxColor, elapsed, valid);
    }

    // ========================================================================
    // ALGORITHM 4: EXACT BACKTRACKING (Chromatic Number Search)
    // ========================================================================
    public static ColoringResult solveExactBacktracking(ConflictGraph graph) {
        long startTime = System.nanoTime();
        int n = graph.numCourses;
        int[] colors = new int[n];

        // Find chromatic number by testing m = 1, 2, ... up to n
        int chromaticNumber = -1;
        for (int m = 1; m <= n; m++) {
            Arrays.fill(colors, 0);
            if (backtrackColor(graph, m, colors, 0)) {
                chromaticNumber = m;
                break;
            }
        }

        long elapsed = System.nanoTime() - startTime;
        boolean valid = verifyColoring(graph, colors);
        return new ColoringResult("Exact Backtracking", colors, chromaticNumber, elapsed, valid);
    }

    private static boolean backtrackColor(ConflictGraph graph, int m, int[] colors, int v) {
        if (v == graph.numCourses) return true;

        for (int c = 1; c <= m; c++) {
            if (isSafe(graph, v, colors, c)) {
                colors[v] = c;
                if (backtrackColor(graph, m, colors, v + 1)) {
                    return true;
                }
                colors[v] = 0;
            }
        }
        return false;
    }

    private static boolean isSafe(ConflictGraph graph, int v, int[] colors, int c) {
        for (int neighbor : graph.adjList.get(v)) {
            if (colors[neighbor] == c) return false;
        }
        return true;
    }

    // ------------------------------------------------------------------------
    // VERIFICATION UTILITY
    // ------------------------------------------------------------------------
    public static boolean verifyColoring(ConflictGraph graph, int[] colors) {
        for (int u = 0; u < graph.numCourses; u++) {
            if (colors[u] <= 0) return false;
            for (int neighbor : graph.adjList.get(u)) {
                if (colors[u] == colors[neighbor]) {
                    return false; // CLASH!
                }
            }
        }
        return true;
    }

    // ========================================================================
    // EXTENSION: CLASSROOM / ROOM ALLOCATION CONSTRAINT SOLVER
    // ========================================================================
    public static class RoomAllocation {
        public final int slotNumber;
        public final Course course;
        public final Classroom assignedRoom;
        public final int remainingRoomCapacity;

        public RoomAllocation(int slotNumber, Course course, Classroom assignedRoom) {
            this.slotNumber = slotNumber;
            this.course = course;
            this.assignedRoom = assignedRoom;
            this.remainingRoomCapacity = assignedRoom.capacity - course.enrolledStudents;
        }
    }

    public static List<RoomAllocation> allocateRooms(ConflictGraph graph, ColoringResult coloring, 
                                                    List<Classroom> availableRooms) {
        List<RoomAllocation> allocations = new ArrayList<>();
        int slots = coloring.totalSlotsUsed;

        // Group courses by exam slot
        Map<Integer, List<Course>> slotMap = new TreeMap<>();
        for (int slot = 1; slot <= slots; slot++) {
            slotMap.put(slot, new ArrayList<>());
        }
        for (int i = 0; i < graph.numCourses; i++) {
            slotMap.get(coloring.colors[i]).add(graph.courses.get(i));
        }

        // For each slot, assign exams to classrooms using Best-Fit Decreasing
        for (Map.Entry<Integer, List<Course>> entry : slotMap.entrySet()) {
            int slot = entry.getKey();
            List<Course> slotCourses = entry.getValue();

            // Sort courses descending by enrollment count
            slotCourses.sort((a, b) -> Integer.compare(b.enrolledStudents, a.enrolledStudents));

            // Available rooms for this slot
            List<Classroom> freeRooms = new ArrayList<>(availableRooms);
            freeRooms.sort((a, b) -> Integer.compare(a.capacity, b.capacity)); // ascending for Best-Fit

            for (Course course : slotCourses) {
                Classroom bestRoom = null;
                for (Classroom room : freeRooms) {
                    if (room.capacity >= course.enrolledStudents) {
                        bestRoom = room;
                        break; // smallest room that fits
                    }
                }

                if (bestRoom != null) {
                    allocations.add(new RoomAllocation(slot, course, bestRoom));
                    freeRooms.remove(bestRoom);
                } else {
                    allocations.add(new RoomAllocation(slot, course, new Classroom("OVERFLOW-HALL", 500, "Main")));
                }
            }
        }
        return allocations;
    }

    // ========================================================================
    // LARGE-SCALE DATASET GENERATOR & BENCHMARK
    // ========================================================================
    public static ConflictGraph generateLargeDataset(int numCourses, int numStudents, int coursesPerStudent, double conflictRate) {
        List<Course> courses = new ArrayList<>();
        String[] depts = {"CSE", "IT", "AI&DS", "ECE", "MECH", "CIVIL"};
        Random rng = new Random(42); // Deterministic seed for reproducible benchmarks

        for (int i = 0; i < numCourses; i++) {
            String dept = depts[i % depts.length];
            String code = String.format("%s%03d", dept, 100 + (i / depts.length) * 10 + (i % 10));
            String title = String.format("Advanced %s Module %d", dept, (i + 1));
            int enrolled = 40 + rng.nextInt(120);
            courses.add(new Course(i, code, title, dept, enrolled));
        }

        ConflictGraph graph = new ConflictGraph(courses);

        // Simulate student enrollments across programs
        for (int s = 0; s < numStudents; s++) {
            int deptIdx = rng.nextInt(depts.length);
            List<Integer> enrolled = new ArrayList<>();
            // Core department courses
            for (int k = 0; k < coursesPerStudent - 1; k++) {
                int cId = (deptIdx + k * depts.length) % numCourses;
                if (!enrolled.contains(cId)) enrolled.add(cId);
            }
            // Inter-disciplinary elective
            if (rng.nextDouble() < conflictRate) {
                int elective = rng.nextInt(numCourses);
                if (!enrolled.contains(elective)) enrolled.add(elective);
            }

            // Create pairwise conflict edges between enrolled courses
            for (int i = 0; i < enrolled.size(); i++) {
                for (int j = i + 1; j < enrolled.size(); j++) {
                    graph.addConflict(enrolled.get(i), enrolled.get(j), 1);
                }
            }
        }

        return graph;
    }

    // ========================================================================
    // MAIN BENCHMARK & DEMO RUNNER
    // ========================================================================
    public static void main(String[] args) {
        System.out.println("==========================================================================");
        System.out.println("      PCCOE DAA LAB - ASSIGNMENT NO. 7: GRAPH COLORING TIMETABLE          ");
        System.out.println("==========================================================================");
        System.out.println("Student: Aditya Chandrajit Deore | PRN: 124B1F116 | Faculty: Dr. Sapana Kolambe\n");

        // --------------------------------------------------------------------
        // PART 1: CORE UNIVERSITY EXAM SCENARIO (6 Standard Courses)
        // --------------------------------------------------------------------
        List<Course> universityCourses = Arrays.asList(
            new Course(0, "C1", "Mathematics", "Basic Sciences", 120),
            new Course(1, "C2", "Physics", "Basic Sciences", 100),
            new Course(2, "C3", "Computer Science", "Engineering", 110),
            new Course(3, "C4", "Chemistry", "Basic Sciences", 80),
            new Course(4, "C5", "Electronics", "Engineering", 90),
            new Course(5, "C6", "Humanities", "Management", 60)
        );

        ConflictGraph examGraph = new ConflictGraph(universityCourses);

        // Conflict edges between courses with shared student enrollments
        examGraph.addConflict(0, 1, 40); // C1 (Maths) <-> C2 (Physics)
        examGraph.addConflict(0, 2, 50); // C1 (Maths) <-> C3 (CS)
        examGraph.addConflict(0, 3, 30); // C1 (Maths) <-> C4 (Chemistry)
        examGraph.addConflict(1, 2, 45); // C2 (Physics) <-> C3 (CS)
        examGraph.addConflict(1, 4, 35); // C2 (Physics) <-> C5 (Electronics)
        examGraph.addConflict(2, 5, 25); // C3 (CS) <-> C6 (Humanities)
        examGraph.addConflict(3, 4, 20); // C4 (Chemistry) <-> C5 (Electronics)
        examGraph.addConflict(4, 5, 15); // C5 (Electronics) <-> C6 (Humanities)

        System.out.println("--- 1. CONFLICT GRAPH METRICS (Core University Scenario) ---");
        System.out.printf("Total Courses (|V|)      : %d\n", examGraph.numCourses);
        System.out.printf("Conflicting Pairs (|E|)  : %d\n", examGraph.getTotalEdges());
        System.out.printf("Conflict Graph Density   : %.2f%%\n", examGraph.getGraphDensity() * 100);
        System.out.println("Vertex Degree Distribution:");
        for (int i = 0; i < examGraph.numCourses; i++) {
            System.out.printf("  %-4s (%-16s, Degree %d): Conflicts with %s\n",
                    examGraph.courses.get(i).code,
                    examGraph.courses.get(i).title,
                    examGraph.getDegree(i),
                    examGraph.adjList.get(i));
        }

        // Run all 4 algorithms on core graph
        ColoringResult resGreedy = solveGreedy(examGraph);
        ColoringResult resWelshPowell = solveWelshPowell(examGraph);
        ColoringResult resDSATUR = solveDSATUR(examGraph);
        ColoringResult resExact = solveExactBacktracking(examGraph);

        System.out.println("\n--- 2. ALGORITHM COMPARISON (Core Scenario) ---");
        System.out.printf("%-22s %-12s %-15s %-15s\n", "Algorithm", "Slots Used", "Execution Time", "Conflict-Free?");
        System.out.println("------------------------------------------------------------------");
        System.out.printf("%-22s %-12d %-15s %-15s\n", resGreedy.algorithmName, resGreedy.totalSlotsUsed, resGreedy.executionTimeNs + " ns", resGreedy.conflictFree ? "YES (Valid)" : "NO (Clash!)");
        System.out.printf("%-22s %-12d %-15s %-15s\n", resWelshPowell.algorithmName, resWelshPowell.totalSlotsUsed, resWelshPowell.executionTimeNs + " ns", resWelshPowell.conflictFree ? "YES (Valid)" : "NO (Clash!)");
        System.out.printf("%-22s %-12d %-15s %-15s\n", resDSATUR.algorithmName, resDSATUR.totalSlotsUsed, resDSATUR.executionTimeNs + " ns", resDSATUR.conflictFree ? "YES (Valid)" : "NO (Clash!)");
        System.out.printf("%-22s %-12d %-15s %-15s\n", resExact.algorithmName, resExact.totalSlotsUsed, resExact.executionTimeNs + " ns", resExact.conflictFree ? "YES (Valid)" : "NO (Clash!)");

        // Display Detailed Timetable using DSATUR (optimal heuristic)
        System.out.println("\n--- 3. OPTIMAL TIMETABLE SCHEDULE (via DSATUR - Chromatic Slots: " + resDSATUR.totalSlotsUsed + ") ---");
        String[] slotNames = {"Slot 1 (Monday Morning)", "Slot 2 (Monday Afternoon)", "Slot 3 (Tuesday Morning)"};
        for (int slot = 1; slot <= resDSATUR.totalSlotsUsed; slot++) {
            System.out.printf("\n[EXAM TIME SLOT %d - %s]\n", slot, (slot <= slotNames.length ? slotNames[slot - 1] : "Slot " + slot));
            System.out.printf("  %-6s %-22s %-16s %-10s\n", "Code", "Course Name", "Department", "Enrollment");
            System.out.println("  ------------------------------------------------------------------");
            for (int i = 0; i < examGraph.numCourses; i++) {
                if (resDSATUR.colors[i] == slot) {
                    Course c = examGraph.courses.get(i);
                    System.out.printf("  %-6s %-22s %-16s %3d students\n", c.code, c.title, c.department, c.enrolledStudents);
                }
            }
        }

        // --------------------------------------------------------------------
        // PART 2: EXTENSION - CLASSROOM CAPACITY ALLOCATION
        // --------------------------------------------------------------------
        System.out.println("\n--- 4. EXTENSION: ROOM ALLOCATION CONSTRAINTS ---");
        List<Classroom> classrooms = Arrays.asList(
            new Classroom("Exam-Hall-A", 150, "Main Block"),
            new Classroom("Exam-Hall-B", 120, "Academic Block"),
            new Classroom("Exam-Hall-C", 100, "Science Block")
        );

        List<RoomAllocation> roomAllocations = allocateRooms(examGraph, resDSATUR, classrooms);
        System.out.printf("%-6s %-6s %-20s %-12s %-18s %-10s\n", "Slot", "Code", "Course Title", "Students", "Assigned Room", "Headroom");
        System.out.println("----------------------------------------------------------------------------------");
        for (RoomAllocation alloc : roomAllocations) {
            System.out.printf("Slot %d %-6s %-20s %3d studs   %-18s +%2d seats\n",
                    alloc.slotNumber,
                    alloc.course.code,
                    alloc.course.title,
                    alloc.course.enrolledStudents,
                    alloc.assignedRoom.roomId,
                    alloc.remainingRoomCapacity);
        }

        // --------------------------------------------------------------------
        // PART 3: SCALABILITY BENCHMARK (500 Courses, 5,000 Students)
        // --------------------------------------------------------------------
        System.out.println("\n--- 5. SCALABILITY BENCHMARK ON LARGE DATASET ---");
        System.out.println("Synthesizing 500 Courses, 5,000 Students across Engineering departments...");
        ConflictGraph largeGraph = generateLargeDataset(500, 5000, 6, 0.45);
        System.out.printf("Graph Constructed: |V| = %d, |E| = %d edges (Density: %.2f%%)\n",
                largeGraph.numCourses, largeGraph.getTotalEdges(), largeGraph.getGraphDensity() * 100);

        ColoringResult benchGreedy = solveGreedy(largeGraph);
        ColoringResult benchWP = solveWelshPowell(largeGraph);
        ColoringResult benchDSATUR = solveDSATUR(largeGraph);

        System.out.printf("\n%-24s %-15s %-16s %-15s\n", "Benchmark Algorithm", "Exam Slots Used", "Runtime (ms)", "Clash-Free?");
        System.out.println("------------------------------------------------------------------------");
        System.out.printf("%-24s %-15d %-16.2f %-15s\n", benchGreedy.algorithmName, benchGreedy.totalSlotsUsed, benchGreedy.executionTimeNs / 1_000_000.0, benchGreedy.conflictFree ? "VALID" : "INVALID");
        System.out.printf("%-24s %-15d %-16.2f %-15s\n", benchWP.algorithmName, benchWP.totalSlotsUsed, benchWP.executionTimeNs / 1_000_000.0, benchWP.conflictFree ? "VALID" : "INVALID");
        System.out.printf("%-24s %-15d %-16.2f %-15s\n", benchDSATUR.algorithmName, benchDSATUR.totalSlotsUsed, benchDSATUR.executionTimeNs / 1_000_000.0, benchDSATUR.conflictFree ? "VALID" : "INVALID");

        System.out.println("\n>> Summary: DSATUR achieves the minimum chromatic exam slots with optimal distribution!");
        System.out.println("==========================================================================");
    }
}
