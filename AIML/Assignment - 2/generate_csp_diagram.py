import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
import networkx as nx
import numpy as np

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['figure.facecolor'] = '#ffffff'

fig = plt.figure(figsize=(24, 11), dpi=200)
fig.patch.set_facecolor('#ffffff')

# Two panels side by side — left 42%, right 56%
ax1 = fig.add_axes([0.01, 0.05, 0.41, 0.90])   # conflict graph
ax2 = fig.add_axes([0.44, 0.04, 0.55, 0.92])   # slot allocation

# =========================================================
# PANEL A: Student Enrollment Conflict Graph
# =========================================================
ax1.set_facecolor('#f9fafb')
for spine in ax1.spines.values():
    spine.set_visible(False)

ax1.set_title("A.  Student Enrollment Conflict Graph\n(CSP Binary Constraints)", 
              fontsize=14, fontweight='bold', color='#111827', pad=16, loc='left')

# --- Node positions (hand-tuned so no node overlaps and labels fit) ---
pos = {
    # TY cluster — top-left quadrant
    'AIML':    (-2.3,  2.1),
    'DAA':     (-0.9,  2.5),
    'OS':      (-2.6,  0.9),
    'AUT':     (-1.2,  1.1),
    # OOP shared node — center
    'OOP':     ( 0.4,  0.5),
    # SY Track A — center-bottom-left
    'DS':      (-0.3, -1.0),
    'COA':     ( 1.2, -1.4),
    # SY Track B — center-right
    'DBMS':    ( 1.8,  1.2),
    'CN':      ( 2.3, -0.2),
    # FE cluster — top-right
    'FE-MATH': ( 0.9,  2.6),
    'FE-PHY':  ( 2.5,  2.3),
    'FE-PROG': ( 1.9,  1.6),
    # FY electives — bottom-left
    'SEC':     (-1.9, -0.8),
    'PE':      (-1.6, -1.8),
}

# Conflict edges per cohort
edges = {
    'TY':    [('AIML','DAA'),('AIML','OS'),('AIML','AUT'),('DAA','OS'),('DAA','AUT'),('OS','AUT')],
    'FE':    [('FE-MATH','FE-PHY'),('FE-MATH','FE-PROG'),('FE-PHY','FE-PROG')],
    'SY-A':  [('OOP','DS'),('OOP','COA'),('DS','COA')],
    'SY-B':  [('OOP','DBMS'),('OOP','CN'),('DBMS','CN')],
    'FY':    [('SEC','PE')],
}

edge_styles = {
    'TY':   {'color': '#dc2626', 'lw': 2.2, 'alpha': 0.80},
    'FE':   {'color': '#ea580c', 'lw': 2.2, 'alpha': 0.80},
    'SY-A': {'color': '#0284c7', 'lw': 2.2, 'alpha': 0.80},
    'SY-B': {'color': '#4f46e5', 'lw': 2.2, 'alpha': 0.80},
    'FY':   {'color': '#9333ea', 'lw': 2.2, 'alpha': 0.80},
}

for cohort, edge_list in edges.items():
    st = edge_styles[cohort]
    for u, v in edge_list:
        x0, y0 = pos[u]; x1, y1 = pos[v]
        ax1.annotate("", xy=(x1, y1), xytext=(x0, y0),
                     arrowprops=dict(arrowstyle='-', color=st['color'],
                                     lw=st['lw'], alpha=st['alpha']))

# Node appearance
node_style = {
    'AIML':    ('#fde8e8', '#dc2626'),
    'DAA':     ('#fde8e8', '#dc2626'),
    'OS':      ('#fde8e8', '#dc2626'),
    'AUT':     ('#fde8e8', '#dc2626'),
    'OOP':     ('#e0f2fe', '#0284c7'),
    'DS':      ('#dbeafe', '#0284c7'),
    'COA':     ('#dbeafe', '#0284c7'),
    'DBMS':    ('#e0e7ff', '#4f46e5'),
    'CN':      ('#e0e7ff', '#4f46e5'),
    'FE-MATH': ('#ffedd5', '#ea580c'),
    'FE-PHY':  ('#ffedd5', '#ea580c'),
    'FE-PROG': ('#ffedd5', '#ea580c'),
    'SEC':     ('#f3e8ff', '#9333ea'),
    'PE':      ('#f3e8ff', '#9333ea'),
}

for node, (x, y) in pos.items():
    fc, ec = node_style[node]
    ax1.text(x, y, node, ha='center', va='center',
             fontsize=9.5, fontweight='bold', color='#111827',
             bbox=dict(boxstyle='round,pad=0.5', fc=fc, ec=ec, lw=2.0, zorder=4))

# Legend
legend_patches = [
    patches.Patch(fc='#fde8e8', ec='#dc2626', lw=1.8, label='TY Core  (AIML, DAA, OS, AUT)'),
    patches.Patch(fc='#dbeafe', ec='#0284c7', lw=1.8, label='SY Track A  (OOP, DS, COA)'),
    patches.Patch(fc='#e0e7ff', ec='#4f46e5', lw=1.8, label='SY Track B  (OOP, DBMS, CN)'),
    patches.Patch(fc='#ffedd5', ec='#ea580c', lw=1.8, label='FE Core  (FE-MATH, FE-PHY, FE-PROG)'),
    patches.Patch(fc='#f3e8ff', ec='#9333ea', lw=1.8, label='FY Electives  (SEC, PE)'),
]
leg = ax1.legend(handles=legend_patches, loc='lower left',
                 fontsize=8.5, framealpha=0.97,
                 facecolor='#ffffff', edgecolor='#d1d5db',
                 handlelength=1.4, handleheight=1.2, labelspacing=0.6)
leg.get_frame().set_linewidth(1.2)

# Note box
ax1.text(0.5, -2.6,
         "★  (DS ↔ DBMS) and (COA ↔ CN) have NO conflict edges\n"
         "     because Track A and Track B students are disjoint.",
         fontsize=8.5, color='#374151', ha='center', style='italic',
         bbox=dict(boxstyle='round,pad=0.55', fc='#f1f5f9', ec='#9ca3af', lw=1.0))

ax1.set_xlim(-3.4, 3.3)
ax1.set_ylim(-3.1, 3.2)
ax1.axis('off')

# =========================================================
# PANEL B: Optimal CSP Solution — Slot / Room Grid
# =========================================================
ax2.set_facecolor('#ffffff')
for spine in ax2.spines.values():
    spine.set_visible(False)

ax2.set_title("B.  Optimal CSP Solution — Disjoint Time-Slot & Room Allocation", 
              fontsize=14, fontweight='bold', color='#111827', pad=16, loc='left')

slots = [
    {
        "label":  "SLOT 1  ·  Monday  09:00 – 12:00",
        "bg":     "#eff6ff", "border": "#2563eb", "title_col": "#1d4ed8",
        "stat":   "✔  8 rooms used  |  0 student clashes",
        "exams": [
            ("AIML",    "TY",   "5-301, 6-101"),
            ("FE-MATH", "FE",   "6-201, 6-301"),
            ("OOP",     "SY",   "5-101, 5-201"),
            ("SEC",     "FY",   "9-101, 9-201"),
        ],
        "node_fc": ["#fde8e8","#ffedd5","#e0f2fe","#f3e8ff"],
        "node_ec": ["#dc2626","#ea580c","#0284c7","#9333ea"],
    },
    {
        "label":  "SLOT 2  ·  Monday  13:30 – 16:30",
        "bg":     "#fdf4ff", "border": "#9333ea", "title_col": "#7c3aed",
        "stat":   "✔  10 rooms used  |  100% capacity met",
        "exams": [
            ("DAA",    "TY",   "6-201, 6-301"),
            ("DBMS",   "SY-B", "5-301, 6-101"),
            ("DS",     "SY-A", "5-101, 5-201"),
            ("FE-PHY", "FE",   "9-101, 9-201"),
            ("PE",     "FY",   "9-301, 9-401"),
        ],
        "node_fc": ["#fde8e8","#e0e7ff","#dbeafe","#ffedd5","#f3e8ff"],
        "node_ec": ["#dc2626","#4f46e5","#0284c7","#ea580c","#9333ea"],
    },
    {
        "label":  "SLOT 3  ·  Tuesday  09:00 – 12:00",
        "bg":     "#f0fdf4", "border": "#16a34a", "title_col": "#15803d",
        "stat":   "✔  8 rooms used  |  0 student clashes",
        "exams": [
            ("CN",      "SY-B", "5-301, 6-101"),
            ("COA",     "SY-A", "5-101, 5-201"),
            ("FE-PROG", "FE",   "9-101, 9-201"),
            ("OS",      "TY",   "6-201, 6-301"),
        ],
        "node_fc": ["#e0e7ff","#dbeafe","#ffedd5","#fde8e8"],
        "node_ec": ["#4f46e5","#0284c7","#ea580c","#dc2626"],
    },
    {
        "label":  "SLOT 4  ·  Tuesday  13:30 – 16:30",
        "bg":     "#fffbeb", "border": "#d97706", "title_col": "#b45309",
        "stat":   "✔  2 rooms used  |  Final TY exam",
        "exams": [
            ("AUT", "TY", "5-101, 5-201"),
        ],
        "node_fc": ["#fde8e8"],
        "node_ec": ["#dc2626"],
    },
]

# Layout: 4 rows stacked, each row = slot card
slot_h  = [0.240, 0.275, 0.240, 0.210]   # vary by exam count
gap     = 0.012
y_top   = 1.00

for s_idx, slot in enumerate(slots):
    sh = slot_h[s_idx]
    y0 = y_top - sh

    # Outer card
    card = patches.FancyBboxPatch((0.01, y0), 0.98, sh - gap,
                                  boxstyle="round,pad=0.012",
                                  fc=slot['bg'], ec=slot['border'], lw=2.0, zorder=1)
    ax2.add_patch(card)

    # Slot label
    ax2.text(0.04, y_top - gap - 0.030, slot['label'],
             fontsize=10.5, fontweight='bold', color=slot['title_col'], va='top')

    # Status pill — right-aligned
    ax2.text(0.965, y_top - gap - 0.030, slot['stat'],
             fontsize=8.5, fontweight='600', color='#15803d', va='top', ha='right')

    # Exam badges
    n = len(slot['exams'])
    col_w = 0.92 / n
    badge_h = sh - 0.085

    for e_idx, (code, cohort, rooms) in enumerate(slot['exams']):
        bx = 0.04 + e_idx * col_w
        by = y0 + gap + 0.010
        bw = col_w - 0.018
        bh = badge_h - 0.018

        fc = slot['node_fc'][e_idx]
        ec = slot['node_ec'][e_idx]

        badge = patches.FancyBboxPatch((bx, by), bw, bh,
                                       boxstyle="round,pad=0.01",
                                       fc='#ffffff', ec=ec, lw=1.5, zorder=2)
        ax2.add_patch(badge)

        mid_x = bx + bw / 2
        mid_y = by + bh / 2

        # Colored dot
        ax2.scatter([mid_x], [mid_y + bh * 0.22], s=40, color=ec, zorder=3)
        # Course code
        ax2.text(mid_x, mid_y + bh * 0.04, code,
                 ha='center', va='center', fontsize=9.5, fontweight='bold', color='#111827', zorder=3)
        # Cohort
        ax2.text(mid_x, mid_y - bh * 0.17, f"({cohort})",
                 ha='center', va='center', fontsize=8.0, color='#6b7280', zorder=3)
        # Rooms
        ax2.text(mid_x, mid_y - bh * 0.37, rooms,
                 ha='center', va='center', fontsize=7.5, color='#374151', zorder=3)
        # 60 seats badge
        ax2.text(mid_x, mid_y - bh * 0.55, "60 seats  ✓",
                 ha='center', va='center', fontsize=7.5, color='#15803d', fontweight='600', zorder=3)

    y_top -= sh

ax2.set_xlim(0, 1)
ax2.set_ylim(y_top - 0.05, 1.04)
ax2.axis('off')

# Thin divider line between panels
fig.add_artist(plt.Line2D([0.440, 0.440], [0.04, 0.96],
                          transform=fig.transFigure,
                          color='#e5e7eb', lw=1.5))

plt.savefig("csp_diagram.png", dpi=200, bbox_inches='tight',
            facecolor='#ffffff', edgecolor='none')
print("Diagram saved: csp_diagram.png")
