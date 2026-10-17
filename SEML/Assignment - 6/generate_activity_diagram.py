import os

def build_nice_balanced_activity_diagram():
    # 4 Perfectly Balanced Swimlanes
    lane_width = 380
    x_start = 80
    y_start = 60
    total_height = 1780
    total_width = x_start * 2 + 4 * lane_width  # 1680
    svg_height = total_height + 100             # 1880

    lanes = [
        {"id": 1, "title": "👤 Operator / Player", "subtitle": "Mission Planning & Rewards", "color": "#0284c7", "x1": x_start, "x2": x_start + lane_width, "center": x_start + lane_width // 2},
        {"id": 2, "title": "🚢 Navigation & AI System", "subtitle": "Autonomous Patrol & Detection", "color": "#0d9488", "x1": x_start + lane_width, "x2": x_start + 2 * lane_width, "center": x_start + lane_width + lane_width // 2},
        {"id": 3, "title": "🧹 Collection Unit", "subtitle": "Robotic Skimmer & Compactor", "color": "#2563eb", "x1": x_start + 2 * lane_width, "x2": x_start + 3 * lane_width, "center": x_start + 2 * lane_width + lane_width // 2},
        {"id": 4, "title": "🏭 Harbor & Recycling Facility", "subtitle": "Docking, Sorting & Processing", "color": "#7c3aed", "x1": x_start + 3 * lane_width, "x2": x_start + 4 * lane_width, "center": x_start + 3 * lane_width + lane_width // 2}
    ]

    l1_c = lanes[0]["center"]  # 270
    l2_c = lanes[1]["center"]  # 650
    l3_c = lanes[2]["center"]  # 1030
    l4_c = lanes[3]["center"]  # 1410

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Open Ocean Cleanup — UML 2.0 Activity Diagram</title>
    <script src="https://unpkg.com/@panzoom/panzoom@4.5.1/dist/panzoom.min.js"></script>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body, html {{ 
            width: 100vw; 
            height: 100vh; 
            margin: 0;
            padding: 0;
            overflow: hidden; 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
            background-color: #ffffff; 
            color: #0f172a; 
        }}
        
        /* Interactive Whiteboard Canvas */
        .whiteboard-container {{
            width: 100vw;
            height: 100vh;
            position: absolute;
            top: 0;
            left: 0;
            background-color: #ffffff;
            background-image: 
                linear-gradient(to right, #f1f5f9 1px, transparent 1px),
                linear-gradient(to bottom, #f1f5f9 1px, transparent 1px);
            background-size: 20px 20px;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: grab;
        }}
        .whiteboard-container:active {{
            cursor: grabbing;
        }}

        #pan-viewport {{
            transform-origin: 0 0;
        }}

        svg {{
            display: block;
            user-select: none;
            background: transparent;
        }}

        /* Swimlane Elements */
        .lane-header-bg {{
            stroke: #cbd5e1;
            stroke-width: 1.5;
        }}
        .lane-border {{
            stroke: #cbd5e1;
            stroke-width: 1.5;
            fill: none;
        }}
        .lane-title {{
            font-size: 14.5px;
            font-weight: 700;
            fill: #ffffff;
            letter-spacing: 0.3px;
        }}
        .lane-subtitle {{
            font-size: 10px;
            font-weight: 500;
            fill: rgba(255, 255, 255, 0.9);
        }}

        /* Action Nodes */
        .action-node {{
            fill: #ffffff;
            stroke: #334155;
            stroke-width: 1.8;
            rx: 8px;
            ry: 8px;
            filter: drop-shadow(0 2px 4px rgba(15, 23, 42, 0.06));
        }}
        .action-node-emerald {{
            fill: #ecfdf5;
            stroke: #059669;
            stroke-width: 1.8;
            rx: 8px;
            ry: 8px;
            filter: drop-shadow(0 2px 4px rgba(5, 150, 105, 0.08));
        }}
        .action-title {{
            font-size: 11.5px;
            font-weight: 700;
            fill: #0f172a;
            text-anchor: middle;
            pointer-events: none;
        }}
        .action-sub {{
            font-size: 9.5px;
            font-weight: 500;
            fill: #64748b;
            text-anchor: middle;
            pointer-events: none;
        }}

        /* Decision Diamonds */
        .decision-diamond {{
            fill: #fffbeb;
            stroke: #d97706;
            stroke-width: 1.8;
            filter: drop-shadow(0 2px 4px rgba(217, 119, 6, 0.08));
        }}
        .decision-title {{
            font-size: 10.5px;
            font-weight: 700;
            fill: #92400e;
            text-anchor: middle;
            pointer-events: none;
        }}

        /* Synchronization Fork / Join Bars */
        .sync-bar {{
            fill: #1e293b;
            rx: 3px;
            ry: 3px;
        }}
        .sync-label {{
            font-size: 9.5px;
            font-weight: 700;
            fill: #475569;
            font-style: italic;
        }}

        /* Object Nodes */
        .object-box {{
            fill: #f0fdf4;
            stroke: #16a34a;
            stroke-width: 1.5;
            stroke-dasharray: 4 2;
            rx: 4px;
            ry: 4px;
            filter: drop-shadow(0 2px 4px rgba(22, 163, 74, 0.06));
        }}
        .object-title {{
            font-size: 10.5px;
            font-weight: 700;
            fill: #14532d;
            text-anchor: middle;
        }}
        .object-tag {{
            font-size: 8.5px;
            font-weight: 600;
            fill: #16a34a;
            font-style: italic;
            text-anchor: middle;
        }}

        /* Lines & Arrows */
        .flow-line {{
            stroke: #334155;
            stroke-width: 1.8;
            fill: none;
        }}
        .flow-line-dashed {{
            stroke: #16a34a;
            stroke-width: 1.5;
            stroke-dasharray: 4 3;
            fill: none;
        }}
        .flow-line-loop {{
            stroke: #64748b;
            stroke-width: 1.6;
            stroke-dasharray: 4 3;
            fill: none;
        }}

        /* Guard Badges */
        .guard-bg {{
            fill: #ffffff;
            stroke: #cbd5e1;
            stroke-width: 1;
            rx: 4px;
            ry: 4px;
        }}
        .guard-text {{
            font-size: 9.5px;
            font-weight: 700;
            fill: #b45309;
            text-anchor: middle;
        }}
        .guard-text-emerald {{
            font-size: 9.5px;
            font-weight: 700;
            fill: #047857;
            text-anchor: middle;
        }}
        .guard-text-blue {{
            font-size: 9.5px;
            font-weight: 700;
            fill: #1d4ed8;
            text-anchor: middle;
        }}
    </style>
</head>
<body>

    <!-- Full Screen Whiteboard Canvas -->
    <div class="whiteboard-container" id="canvas-container">
        <div id="pan-viewport">
            <svg id="activity-diagram-svg" width="{total_width}" height="{svg_height}" viewBox="0 0 {total_width} {svg_height}" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
                        <path d="M 0 1.5 L 8 5 L 0 8.5 Z" fill="#334155" />
                    </marker>
                    <marker id="arrow-green" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
                        <path d="M 0 1.5 L 8 5 L 0 8.5 Z" fill="#16a34a" />
                    </marker>
                    <marker id="arrow-loop" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6.5" markerHeight="6.5" orient="auto">
                        <path d="M 0 1.5 L 8 5 L 0 8.5 Z" fill="#64748b" />
                    </marker>
                </defs>

                <!-- Swimlanes Background Outer Card -->
                <rect x="{x_start}" y="{y_start}" width="{4 * lane_width}" height="{total_height}" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.8" rx="8" />
'''

    # Generate Swimlanes
    for i, lane in enumerate(lanes):
        rx_attr = ""
        border_rx = ""
        if i == 0:
            rx_attr = 'rx="8 0 0 0"'
            border_rx = 'rx="8 0 0 8"'
        elif i == 3:
            rx_attr = 'rx="0 8 0 0"'
            border_rx = 'rx="0 8 8 0"'

        html += f'''
                <!-- Lane {lane["id"]}: {lane["title"]} -->
                <rect x="{lane["x1"]}" y="{y_start}" width="{lane_width}" height="54" fill="{lane["color"]}" {rx_attr} class="lane-header-bg" />
                <rect x="{lane["x1"]}" y="{y_start}" width="{lane_width}" height="{total_height}" class="lane-border" {border_rx} />
                <text x="{lane["center"]}" y="{y_start + 24}" text-anchor="middle" class="lane-title">{lane["title"]}</text>
                <text x="{lane["center"]}" y="{y_start + 41}" text-anchor="middle" class="lane-subtitle">{lane["subtitle"]}</text>
        '''

    def action(x, y, title, sub="", w=230, h=48, variant=""):
        cls = "action-node"
        t_style = ""
        if variant == "emerald":
            cls = "action-node-emerald"
            t_style = "fill: #065f46;"
        return f'''
                <g>
                    <rect x="{x - w//2}" y="{y}" width="{w}" height="{h}" class="{cls}" />
                    <text x="{x}" y="{y + (21 if sub else 29)}" class="action-title" style="{t_style}">{title}</text>
                    {f'<text x="{x}" y="{y + 36}" class="action-sub">{sub}</text>' if sub else ''}
                </g>'''

    def decision(x, y, text, hw=70, hh=24):
        pts = f"{x},{y - hh} {x + hw},{y} {x},{y + hh} {x - hw},{y}"
        return f'''
                <g>
                    <polygon points="{pts}" class="decision-diamond" />
                    <text x="{x}" y="{y + 4}" class="decision-title">{text}</text>
                </g>'''

    def guard(x, y, w, h, text, color="amber"):
        cls = "guard-text"
        if color == "emerald":
            cls = "guard-text-emerald"
        elif color == "blue":
            cls = "guard-text-blue"
        return f'''
                <g>
                    <rect x="{x - w//2}" y="{y - h//2}" width="{w}" height="{h}" class="guard-bg" />
                    <text x="{x}" y="{y + 3.5}" class="{cls}">{text}</text>
                </g>'''

    def obj_node(x, y, title, tag="", w=180, h=36):
        return f'''
                <g>
                    <rect x="{x - w//2}" y="{y}" width="{w}" height="{h}" class="object-box" />
                    <text x="{x}" y="{y + 17}" class="object-title">{title}</text>
                    <text x="{x}" y="{y + 29}" class="object-tag">{tag}</text>
                </g>'''

    # ==================== STEP-BY-STEP FLOW ====================

    # 1. Initial Node (Lane 1)
    html += f'''
                <!-- Initial Node (Lane 1) -->
                <circle cx="{l1_c}" cy="135" r="14" fill="#0f172a" />
                <text x="{l1_c + 22}" y="139" font-size="11.5" font-weight="700" fill="#0f172a">Start Mission</text>

                <!-- Flow: Initial -> Select Sector -->
                <path d="M {l1_c},149 L {l1_c},175" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 2. Action 1 (Lane 1): Select Target Sector & Route
    html += action(l1_c, 175, "Select Target Sector & Route", "Pacific Gyre / Coastal Bay Zones")

    # Flow from Lane 1 to Lane 2
    html += f'''
                <!-- Flow: Action 1 (Lane 1) -> Action 2 (Lane 2) -->
                <path d="M {l1_c},223 L {l1_c},248 L {l2_c},248 L {l2_c},270" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 3. Action 2 (Lane 2): Pre-Launch Subsystem Check
    html += action(l2_c, 270, "Run Pre-Launch Diagnostics", "Sensors, thrusters & battery check")

    # Flow: Action 2 -> Action 3
    html += f'''
                <path d="M {l2_c},318 L {l2_c},345" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 4. Action 3 (Lane 2): Patrol Search Grid
    html += action(l2_c, 345, "Navigate Search Grid", "Autonomous GPS waypoint sweeping")

    # Flow: Action 3 -> Decision 1
    html += f'''
                <path d="M {l2_c},393 L {l2_c},425" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 5. Decision 1 (Lane 2): Entity Detected?
    html += decision(l2_c, 447, "Entity Detected?", hw=70, hh=22)

    # Branch [No]: Loop back to Patrol (Lane 2 left gutter: x=485)
    html += f'''
                <!-- Branch [No]: Loop back to Patrol -->
                <path d="M {l2_c - 70},447 L 485,447 L 485,369 L {l2_c - 115},369" class="flow-line-loop" marker-end="url(#arrow-loop)" />
    '''
    html += guard(485, 410, 85, 18, "[No / Clear Water]")

    # Branch [Yes]: Down to Decision 2 (Target Classification)
    html += f'''
                <path d="M {l2_c},469 L {l2_c},505" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += guard(l2_c, 487, 80, 18, "[Object Found]", "blue")

    # 6. Decision 2 (Lane 2): Classify Object Type?
    html += decision(l2_c, 527, "Classify Object?", hw=70, hh=22)

    # Branch [Marine Life]: Emit Acoustic Ping inside Lane 2
    html += f'''
                <!-- Branch [Marine Life]: Acoustic Ping -->
                <path d="M {l2_c - 70},527 L 530,527 L 530,560" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += guard(530, 515, 85, 18, "[Marine Fauna]", "emerald")
    html += action(530, 560, "Emit Ultrasonic Ping", "Deterrent pulse & course hold", w=150, h=44, variant="emerald")

    # Wildlife loop back to Patrol: routes from x=530 up to Patrol
    html += f'''
                <path d="M 530,604 L 530,625 L 485,625 L 485,369 L {l2_c - 115},369" class="flow-line-loop" marker-end="url(#arrow-loop)" />
    '''

    # Branch [Plastic Debris]: Advance across to Lane 3 (Collection)
    html += f'''
                <!-- Branch [Plastic Debris]: Move to Collection Unit (Lane 3) -->
                <path d="M {l2_c + 70},527 L {l3_c},527 L {l3_c},570" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += guard(840, 515, 130, 18, "[Target Debris Confirmed]", "blue")

    # 7. Action 4 (Lane 3): Deploy Booms & Robotic Skimmer
    html += action(l3_c, 570, "Deploy Skimmer Booms", "Channel floating debris toward intake")

    # Flow to Fork Bar in Lane 3
    html += f'''
                <path d="M {l3_c},618 L {l3_c},645" class="flow-line" marker-end="url(#arrow)" />

                <!-- Fork Bar (Lane 3 Concurrency) -->
                <rect x="{l3_c - 150}" y="645" width="300" height="7" class="sync-bar" />
                <text x="{l3_c}" y="639" text-anchor="middle" class="sync-label">«fork» Intake &amp; Separation</text>

                <!-- Thread A: Conveyor Lift -->
                <path d="M {l3_c - 75},652 L {l3_c - 75},680" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += action(l3_c - 75, 680, "Conveyor Intake", "Lift plastic to hopper", w=140, h=42)

    # Thread B: Bycatch Grating
    html += f'''
                <!-- Thread B: Bycatch Grating -->
                <path d="M {l3_c + 75},652 L {l3_c + 75},680" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += action(l3_c + 75, 680, "Bycatch Escape", "Water filter & fish safe", w=140, h=42)

    # Lines to Join Bar
    html += f'''
                <path d="M {l3_c - 75},722 L {l3_c - 75},750" class="flow-line" />
                <path d="M {l3_c + 75},722 L {l3_c + 75},750" class="flow-line" />

                <!-- Join Bar (Lane 3) -->
                <rect x="{l3_c - 150}" y="750" width="300" height="7" class="sync-bar" />
                <text x="{l3_c}" y="768" text-anchor="middle" class="sync-label">«join» Debris Isolated Safely</text>
    '''

    # Flow: Join Bar -> Action 5 (Hydraulic Compaction)
    html += f'''
                <path d="M {l3_c},757 L {l3_c},790" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += action(l3_c, 790, "Compress Plastic Waste", "Hydraulic ram compacts high-density bales")

    # Flow to Object Node: WasteBatch
    html += f'''
                <path d="M {l3_c},838 L {l3_c},865" class="flow-line-dashed" marker-end="url(#arrow-green)" />
    '''
    html += obj_node(l3_c, 865, "Compressed Waste Bales", "«object: WasteBatch»", w=190, h=36)

    # Flow: Object Node -> Decision 3 (Capacity Full?)
    html += f'''
                <path d="M {l3_c},901 L {l3_c},935" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += decision(l3_c, 957, "Storage >= 90%?", hw=70, hh=22)

    # Branch [No]: Loop back to Search Grid in Lane 2
    html += f'''
                <!-- Branch [No]: Loop back to Patrol -->
                <path d="M {l3_c - 70},957 L 865,957 L 865,369 L {l2_c + 115},369" class="flow-line-loop" marker-end="url(#arrow-loop)" />
    '''
    html += guard(865, 660, 115, 18, "[Space Available / Resume]", "emerald")

    # Branch [Yes]: Proceed to Harbor Return in Lane 2
    html += f'''
                <!-- Branch [Yes]: Return Navigation -->
                <path d="M {l3_c},979 L {l3_c},1015 L {l2_c},1015 L {l2_c},1045" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += guard(l3_c, 998, 115, 18, "[Capacity Full or Low Battery]")

    # 8. Action 6 (Lane 2): Engage Harbor Return Autopilot
    html += action(l2_c, 1045, "Engage Return Autopilot", "Optimal current transit vector to dock")

    # Flow: Action 6 (Lane 2) -> Action 7 (Lane 4 Harbor)
    html += f'''
                <!-- Flow from Lane 2 to Lane 4 across clear horizontal corridor -->
                <path d="M {l2_c},1093 L {l2_c},1120 L {l4_c},1120 L {l4_c},1150" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 9. Action 7 (Lane 4): Mooring & Laser-Guided Docking
    html += action(l4_c, 1150, "Berth Mooring & Fast-Charge", "Laser-guided docking & 150kW DC plug")

    # Flow: Action 7 -> Action 8
    html += f'''
                <path d="M {l4_c},1198 L {l4_c},1230" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 10. Action 8 (Lane 4): Automated Crane Offload
    html += action(l4_c, 1230, "Automated Crane Offload", "Transfer bales to industrial sorting line")

    # Flow: Action 8 -> Action 9
    html += f'''
                <path d="M {l4_c},1278 L {l4_c},1310" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 11. Action 9 (Lane 4): NIR Spectroscopic Sort
    html += action(l4_c, 1310, "NIR Spectroscopic Sorting", "Separate PET, HDPE, PP & Ghost Nets")

    # Flow: Action 9 -> Action 10
    html += f'''
                <path d="M {l4_c},1358 L {l4_c},1390" class="flow-line" marker-end="url(#arrow)" />
    '''

    # 12. Action 10 (Lane 4): Pelletize into Recycled Resin
    html += action(l4_c, 1390, "Granulate & Pelletize Resin", "Convert plastic to certified circular material")

    # Flow to Object Node: CleanCredits
    html += f'''
                <path d="M {l4_c},1438 L {l4_c},1468" class="flow-line-dashed" marker-end="url(#arrow-green)" />
    '''
    html += obj_node(l4_c, 1468, "Eco-Reward Tokens", "«object: CleanCredits»", w=180, h=36)

    # Flow from Lane 4 back to Lane 1 (Reward Operator)
    html += f'''
                <!-- Flow: Lane 4 to Lane 1 (Receive Rewards) -->
                <path d="M {l4_c},1504 L {l4_c},1535 L {l1_c},1535 L {l1_c},1565" class="flow-line" marker-end="url(#arrow)" />
    '''
    html += guard(850, 1523, 140, 18, "[Issue Token Rewards & XP]", "emerald")

    # 13. Action 11 (Lane 1): Receive CleanCredits & Update Dashboard
    html += action(l1_c, 1565, "Receive CleanCredits & Summary", "+500 Tokens, Rank XP & Fleet Upgrades")

    # Flow to Activity Final Node
    html += f'''
                <!-- Flow: Action 11 -> Final Node -->
                <path d="M {l1_c},1613 L {l1_c},1665" class="flow-line" marker-end="url(#arrow)" />

                <!-- Activity Final Node (Bullseye in Lane 1) -->
                <circle cx="{l1_c}" cy="1685" r="16" fill="none" stroke="#0f172a" stroke-width="2.2" />
                <circle cx="{l1_c}" cy="1685" r="9" fill="#0f172a" />
                <text x="{l1_c}" y="1722" text-anchor="middle" font-size="12" font-weight="700" fill="#0f172a">Mission Complete</text>
    '''

    html += '''
            </svg>
        </div>
    </div>

    <!-- Interactive Panzoom Initialization -->
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const viewport = document.getElementById("pan-viewport");
            const container = document.getElementById("canvas-container");
            
            const panzoom = Panzoom(viewport, {
                maxScale: 3.5,
                minScale: 0.3,
                step: 0.12,
                contain: false
            });

            container.addEventListener("wheel", function(event) {
                panzoom.zoomWithWheel(event);
            }, { passive: false });

            // Fit nicely into the screen on open
            const scaleX = (window.innerWidth - 60) / 1680;
            const scaleY = (window.innerHeight - 60) / 1880;
            const initialScale = Math.min(scaleX, scaleY, 0.95);
            
            const initialX = Math.max(10, (window.innerWidth - 1680 * initialScale) / 2);
            const initialY = Math.max(10, (window.innerHeight - 1880 * initialScale) / 2);

            panzoom.zoom(initialScale);
            panzoom.pan(initialX, initialY);

            container.addEventListener("dblclick", function() {
                panzoom.zoom(initialScale);
                panzoom.pan(initialX, initialY);
            });
        });
    </script>
</body>
</html>
'''
    return html

if __name__ == "__main__":
    content = build_nice_balanced_activity_diagram()
    target_path = os.path.join(os.path.dirname(__file__), "Activity_Diagram.html")
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Generated balanced & nice Activity_Diagram.html ({len(content)} bytes).")
