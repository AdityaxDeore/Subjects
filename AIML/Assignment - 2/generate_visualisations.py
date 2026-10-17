"""
Visualisation script for PCCOE SmartExam CSP Assignment
Generates 4 publication-quality charts saved as PNG files
"""

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'axes.spines.top': False,
    'axes.spines.right': False,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': '#555555',
    'xtick.color': '#333333',
    'ytick.color': '#333333',
    'axes.labelcolor': '#222222',
    'text.color': '#222222',
})

# ─── Data ────────────────────────────────────────────────────────────────────

slots = ['Slot 1\nMon 09:00', 'Slot 2\nMon 13:30', 'Slot 3\nTue 09:00', 'Slot 4\nTue 13:30']
exams_per_slot = [4, 5, 4, 1]
rooms_per_slot = [8, 10, 8, 2]
capacity_per_slot = [240, 300, 240, 60]

approaches = ['Naive\nBacktracking', 'BT + MRV', 'BT + MRV\n+ LCV', 'MRV + LCV\n+ Forward\nChecking', 'Min-Conflicts\n(Local)']
nodes_visited = [500000, 180, 42, 14, None]
nodes_log = [np.log10(n) if n else 0 for n in nodes_visited]
bar_colors = ['#c0392b', '#e67e22', '#f1c40f', '#27ae60', '#95a5a6']

cohorts = ['TY Core', 'FE Core', 'SY Track A', 'SY Track B', 'FY Electives']
num_subjects = [4, 3, 3, 3, 2]
num_conflicts = [6, 3, 3, 3, 1]
cohort_colors = ['#e74c3c', '#e67e22', '#2980b9', '#8e44ad', '#16a085']

search_labels = ['Naive BT', 'BT+MRV', 'BT+MRV+LCV', 'Full CSP']
backtracks = [500000, 180, 42, 0]

# ─── Figure 1: Exams & Rooms per Slot (Grouped Bar) ─────────────────────────

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(slots))
w = 0.30
b1 = ax.bar(x - w/2, exams_per_slot, width=w, color='#34495e', label='Exams Scheduled', zorder=3)
b2 = ax.bar(x + w/2, rooms_per_slot,  width=w, color='#7f8c8d', label='Classrooms Used',  zorder=3)

for bar in b1:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=11, fontweight='bold')
for bar in b2:
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.15,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_xticks(x); ax.set_xticklabels(slots, fontsize=11)
ax.set_ylabel('Count', fontsize=12); ax.set_ylim(0, 13)
ax.set_title('Examinations & Classrooms Allocated per Time Slot', fontsize=13, fontweight='bold', pad=12)
ax.legend(fontsize=10, framealpha=0.9)
ax.yaxis.grid(True, linestyle='--', alpha=0.5, zorder=0)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('viz_slot_distribution.png', dpi=180, bbox_inches='tight')
plt.close()
print("Saved: viz_slot_distribution.png")

# ─── Figure 2: Nodes Visited (log scale bar) ────────────────────────────────

fig, ax = plt.subplots(figsize=(10, 5))
x = np.arange(len(approaches))
bars = ax.bar(x, nodes_log, color=bar_colors, width=0.55, zorder=3, edgecolor='white', linewidth=0.8)

labels = ['>500,000', '~180', '~42', '14', 'N/A']
for bar, lbl in zip(bars, labels):
    yv = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yv + 0.08, lbl,
            ha='center', va='bottom', fontsize=10.5, fontweight='bold')

ax.set_xticks(x); ax.set_xticklabels(approaches, fontsize=10)
ax.set_ylabel('log₁₀(Nodes Visited)', fontsize=11)
ax.set_title('Search Space Explored — Nodes Visited by Algorithm (Log Scale)', fontsize=13, fontweight='bold', pad=12)
ax.set_ylim(0, 7.2)
ax.yaxis.grid(True, linestyle='--', alpha=0.4, zorder=0)
ax.set_axisbelow(True)

yticks = [0, 1, 2, 3, 4, 5, 6]
ax.set_yticks(yticks)
ax.set_yticklabels([f'10^{t}' for t in yticks], fontsize=9)

optimal_patch = mpatches.Patch(color='#27ae60', label='Optimal: Full CSP (14 nodes, 0 backtracks)')
ax.legend(handles=[optimal_patch], fontsize=10, loc='upper right')
plt.tight_layout()
plt.savefig('viz_nodes_visited.png', dpi=180, bbox_inches='tight')
plt.close()
print("Saved: viz_nodes_visited.png")

# ─── Figure 3: Cohort Conflict Analysis (Subjects vs Conflict Edges) ────────

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(cohorts))
w = 0.30
b1 = ax.bar(x - w/2, num_subjects, width=w, color='#2c3e50', label='Number of Subjects', zorder=3)
b2 = ax.bar(x + w/2, num_conflicts, width=w, color='#7f8c8d', label='Conflict Edges', zorder=3)

for bar in b1:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.06,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=11, fontweight='bold')
for bar in b2:
    ax.text(bar.get_x()+bar.get_width()/2, bar.get_height()+0.06,
            str(int(bar.get_height())), ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_xticks(x); ax.set_xticklabels(cohorts, fontsize=10.5)
ax.set_ylabel('Count', fontsize=12); ax.set_ylim(0, 8)
ax.set_title('Cohort Conflict Graph — Subjects & Binary Constraint Edges', fontsize=13, fontweight='bold', pad=12)
ax.legend(fontsize=10, framealpha=0.9)
ax.yaxis.grid(True, linestyle='--', alpha=0.5, zorder=0)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('viz_conflict_edges.png', dpi=180, bbox_inches='tight')
plt.close()
print("Saved: viz_conflict_edges.png")

# ─── Figure 4: Backtrack Count reduction ────────────────────────────────────

fig, ax = plt.subplots(figsize=(9, 5))
x = np.arange(len(search_labels))
colors_bt = ['#c0392b', '#e67e22', '#f39c12', '#27ae60']
bt_log = [np.log10(b+1) for b in backtracks]

bars = ax.bar(x, bt_log, color=colors_bt, width=0.50, zorder=3, edgecolor='white', linewidth=0.8)
bt_labels = ['>500,000', '~180', '~42', '0']
for bar, lbl in zip(bars, bt_labels):
    yv = bar.get_height()
    ax.text(bar.get_x()+bar.get_width()/2, yv+0.05, lbl,
            ha='center', va='bottom', fontsize=11, fontweight='bold')

ax.set_xticks(x); ax.set_xticklabels(search_labels, fontsize=11)
ax.set_ylabel('log₁₀(Backtracks + 1)', fontsize=11)
ax.set_title('Backtracking Count Reduction with Progressive Heuristic Integration', fontsize=13, fontweight='bold', pad=12)
ax.set_ylim(0, 7.2)
ax.yaxis.grid(True, linestyle='--', alpha=0.4, zorder=0)
ax.set_axisbelow(True)

yticks = [0,1,2,3,4,5,6]
ax.set_yticks(yticks)
ax.set_yticklabels([f'10^{t}' for t in yticks], fontsize=9)
plt.tight_layout()
plt.savefig('viz_backtrack_reduction.png', dpi=180, bbox_inches='tight')
plt.close()
print("Saved: viz_backtrack_reduction.png")

print("\nAll 4 visualisations generated successfully.")
