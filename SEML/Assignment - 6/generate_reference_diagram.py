"""
Generate the exact pixel-perfect recreation of the user's reference diagram
into Activity_Diagram_New.html.
"""

def generate_exact_svg_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Open Ocean Cleanup — Activity Diagram</title>
    <script src="https://unpkg.com/@panzoom/panzoom@4.5.1/dist/panzoom.min.js"></script>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body, html {
            width: 100vw;
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow: hidden;
            font-family: Arial, Helvetica, sans-serif;
            background-color: #f8fafc;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        .canvas-container {
            width: 100vw;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: grab;
            background-color: #ffffff;
            background-image: 
                linear-gradient(to right, #f1f5f9 1px, transparent 1px),
                linear-gradient(to bottom, #f1f5f9 1px, transparent 1px);
            background-size: 20px 20px;
        }
        .canvas-container:active {
            cursor: grabbing;
        }

        #pan-viewport {
            transform-origin: 0 0;
            display: flex;
            justify-content: center;
            align-items: center;
        }

        svg {
            display: block;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
            background: #ffffff;
            user-select: none;
        }

        /* Typography & Styles */
        text {
            font-family: Arial, Helvetica, sans-serif;
        }
        .col-header {
            font-size: 11px;
            font-weight: bold;
            fill: #111827;
            text-anchor: middle;
        }
        .sec-title {
            font-size: 8.5px;
            font-weight: bold;
            fill: #111827;
            text-anchor: start;
        }
        .sec-sub {
            font-size: 7.5px;
            font-weight: normal;
            fill: #111827;
            text-anchor: start;
        }
        .node-text {
            font-size: 7.5px;
            fill: #111827;
            text-anchor: middle;
            pointer-events: none;
        }
        .node-text-bold {
            font-size: 7.5px;
            font-weight: bold;
            fill: #111827;
            text-anchor: middle;
            pointer-events: none;
        }
        .diamond-text {
            font-size: 6.8px;
            fill: #111827;
            text-anchor: middle;
            pointer-events: none;
        }
        .branch-label {
            font-size: 6.8px;
            fill: #111827;
            font-weight: normal;
        }
        .loop-tag {
            font-size: 8px;
            font-weight: bold;
            fill: #0284c7;
        }

        /* Shapes */
        .process-box {
            fill: #ffffff;
            stroke: #1e3a8a;
            stroke-width: 1;
            rx: 4px;
            ry: 4px;
        }
        .decision-shape {
            fill: #ffffff;
            stroke: #1e3a8a;
            stroke-width: 1;
        }
        .connector-line {
            fill: none;
            stroke: #1e3a8a;
            stroke-width: 1;
        }
        .grid-line {
            stroke: #93c5fd;
            stroke-width: 0.8;
        }
        .dashed-grid {
            stroke: #93c5fd;
            stroke-width: 0.8;
            stroke-dasharray: 2 2;
        }
        .loop-boundary {
            fill: none;
            stroke: #3b82f6;
            stroke-width: 1;
            stroke-dasharray: 4 2;
            rx: 6px;
            ry: 6px;
        }
        .sync-bar-shape {
            fill: #0f172a;
        }
    </style>
</head>
<body>

    <div class="canvas-container" id="canvas-container">
        <div id="pan-viewport">
            <svg id="exact-diagram" width="1010" height="554" viewBox="0 0 1010 554" xmlns="http://www.w3.org/2000/svg">
                <defs>
                    <marker id="arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="4.5" markerHeight="4.5" orient="auto">
                        <path d="M 0 1.5 L 8 5 L 0 8.5 Z" fill="#1e3a8a" />
                    </marker>
                </defs>

                <!-- ==================== 1. GRID & SWIMLANE BACKGROUNDS ==================== -->
                <g id="swimlanes">
                    <!-- Outer Border -->
                    <rect x="1" y="1" width="1004" height="550" fill="#ffffff" stroke="#94a3b8" stroke-width="1" />

                    <!-- Header Fills -->
                    <!-- Col 0: Section Column (x: 1 to 91, w: 90) -->
                    <rect x="1" y="1" width="90" height="27" fill="#ffffff" />
                    <!-- Col 1: Player (x: 91 to 330, w: 239) - Light pastel blue -->
                    <rect x="91" y="1" width="239" height="27" fill="#e0f2fe" />
                    <text x="210" y="18" class="col-header">Player</text>

                    <!-- Col 2: Game System (x: 330 to 609, w: 279) - Light pastel green -->
                    <rect x="330" y="1" width="279" height="27" fill="#dcfce7" />
                    <text x="469" y="18" class="col-header">Game System</text>

                    <!-- Col 3: Ocean Environment (x: 609 to 819, w: 210) - Light pastel yellow/cream -->
                    <rect x="609" y="1" width="210" height="27" fill="#fef9c3" />
                    <text x="714" y="18" class="col-header">Ocean Environment</text>

                    <!-- Col 4: Database (x: 819 to 1005, w: 186) - Light pastel lavender/purple -->
                    <rect x="819" y="1" width="186" height="27" fill="#ede9fe" />
                    <text x="912" y="18" class="col-header">Database</text>

                    <!-- Header Bottom Line -->
                    <line x1="1" y1="28" x2="1005" y2="28" class="grid-line" />

                    <!-- Vertical Grid Lines Separating Columns -->
                    <line x1="91" y1="1" x2="91" y2="551" class="grid-line" />
                    <line x1="330" y1="1" x2="330" y2="551" class="grid-line" />
                    <line x1="609" y1="1" x2="609" y2="551" class="grid-line" />
                    <line x1="819" y1="1" x2="819" y2="551" class="grid-line" />

                    <!-- Horizontal Dashed Lines Separating Sections -->
                    <!-- Sec 1 Bottom -->
                    <line x1="1" y1="152" x2="1005" y2="152" class="dashed-grid" />
                    <!-- Sec 2 Bottom -->
                    <line x1="1" y1="267" x2="1005" y2="267" class="dashed-grid" />
                    <!-- Sec 3 Bottom -->
                    <line x1="1" y1="391" x2="1005" y2="391" class="dashed-grid" />
                    <!-- Sec 4 Bottom -->
                    <line x1="1" y1="514" x2="1005" y2="514" class="dashed-grid" />
                </g>

                <!-- ==================== 2. SECTION LABELS ==================== -->
                <g id="section-labels">
                    <!-- Section 1 -->
                    <text x="7" y="75" class="sec-title">1. Authentication</text>
                    <text x="7" y="87" class="sec-sub">(Registration &amp; Login)</text>

                    <!-- Section 2 -->
                    <text x="7" y="198" class="sec-title">2. Game Setup</text>
                    <text x="7" y="210" class="sec-sub">(Select Zone &amp; Launch)</text>

                    <!-- Section 3 -->
                    <text x="7" y="318" class="sec-title">3. Ocean Exploration</text>
                    <text x="7" y="329" class="sec-sub">(Collect Waste /</text>
                    <text x="7" y="339" class="sec-sub">Rescue Marine Life)</text>

                    <!-- Section 4 -->
                    <text x="7" y="440" class="sec-title">4. Base Operations</text>
                    <text x="7" y="451" class="sec-sub">(Sell Waste / Upgrade /</text>
                    <text x="7" y="461" class="sec-sub">View Report)</text>

                    <!-- Section 5 -->
                    <text x="7" y="536" class="sec-title">5. Exit</text>
                </g>

                <!-- ==================== 3. CONNECTORS & ARROWS ==================== -->
                <g id="connectors">
                    <!-- ---------- Section 1 Connectors ---------- -->
                    <!-- Start -> Open Game -->
                    <path d="M 160,47 L 160,56" class="connector-line" marker-end="url(#arrow)" />
                    <!-- Open Game -> Registered? -->
                    <path d="M 160,74 L 160,81" class="connector-line" marker-end="url(#arrow)" />
                    <!-- Registered? [No] -> Enter Registration Details -->
                    <path d="M 184,95 L 223,95" class="connector-line" marker-end="url(#arrow)" />
                    <text x="194" y="90" class="branch-label">[No]</text>

                    <!-- Enter Registration Details -> Create New User -->
                    <path d="M 318,92 L 368,92 L 368,87 L 419,87" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Enter Registration Details -> Store User Data (Database) -->
                    <path d="M 270,82 L 270,68 L 865,68" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Registered? [Yes] -> Login -->
                    <path d="M 160,109 L 160,122" class="connector-line" marker-end="url(#arrow)" />
                    <text x="165" y="117" class="branch-label">[Yes]</text>

                    <!-- Login -> Validate Login -->
                    <path d="M 197,131 L 242,131 L 242,113 L 419,113" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Validate Login -> Retrieve User Data (Database) -->
                    <path d="M 518,113 L 865,113" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Create New User -> Validate Login -->
                    <path d="M 468,96 L 468,104" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Validate Login -> Main Menu -->
                    <path d="M 468,122 L 468,130" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Main Menu -> Select Action (Sec 2) -->
                    <path d="M 468,148 L 468,156 L 189,156 L 189,161" class="connector-line" marker-end="url(#arrow)" />

                    <!-- ---------- Section 2 Connectors ---------- -->
                    <!-- Select Action distribution bus to 4 actions -->
                    <path d="M 161,179 L 161,187" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 189,179 L 189,174 L 513,174" class="connector-line" />
                    <path d="M 272,174 L 272,181" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 393,174 L 393,181" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 513,174 L 513,181" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Start Game -> Select Ocean Zone -->
                    <path d="M 161,205 L 161,227" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Select Ocean Zone -> Zone Unlocked? -->
                    <path d="M 200,236 L 286,236" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Zone Unlocked? [No] -> Prepare Boat -->
                    <path d="M 332,236 L 380,236" class="connector-line" marker-end="url(#arrow)" />
                    <text x="345" y="230" class="branch-label">[No]</text>

                    <!-- Zone Unlocked? [Yes] -> Detect Environment (Sec 3) -->
                    <path d="M 309,250 L 309,289" class="connector-line" marker-end="url(#arrow)" />
                    <text x="315" y="262" class="branch-label">[Yes]</text>

                    <!-- Prepare Boat -> Boat Ready? -->
                    <path d="M 453,231 L 484,231" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Boat Ready? [No] -> Show Repair Message -->
                    <path d="M 530,231 L 596,231" class="connector-line" marker-end="url(#arrow)" />
                    <text x="552" y="225" class="branch-label">[No]</text>

                    <!-- Boat Ready? [Yes] -> Launch Boat -->
                    <path d="M 507,245 L 507,250" class="connector-line" marker-end="url(#arrow)" />
                    <text x="515" y="247" class="branch-label">[Yes]</text>

                    <!-- Show Repair Message -> Load Boat Data & Launch Boat -->
                    <path d="M 691,230 L 865,230" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 691,230 L 730,230 L 730,262 L 549,262" class="connector-line" marker-end="url(#arrow)" />

                    <!-- View Leaderboard -> Load Zone Data (Database) -->
                    <path d="M 318,190 L 335,190 L 335,194 L 865,194" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Launch Boat -> Detect Environment (Sec 3) -->
                    <path d="M 475,259 L 400,259 L 320,259 L 320,289" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Exit Game line passing all the way down to Section 5 Logout / Close Game -->
                    <path d="M 513,198 L 513,520 L 176,520 L 176,527" class="connector-line" marker-end="url(#arrow)" />

                    <!-- ---------- Section 3 Connectors ---------- -->
                    <!-- Control Boat -> Detect Environment -->
                    <path d="M 197,303 L 258,303" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Detect Environment -> Object Detected? -->
                    <path d="M 358,300 L 390,300" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Object Detected? -> 4 branches -->
                    <!-- [Waste] -->
                    <path d="M 418,285 L 450,277 L 516,277" class="connector-line" marker-end="url(#arrow)" />
                    <text x="475" y="271" class="branch-label">[Waste]</text>

                    <!-- [Marine Life] -->
                    <path d="M 446,297 L 516,297" class="connector-line" marker-end="url(#arrow)" />
                    <text x="465" y="293" class="branch-label">[Marine Life]</text>

                    <!-- [Obstacle] -->
                    <path d="M 435,308 L 470,319 L 516,319" class="connector-line" marker-end="url(#arrow)" />
                    <text x="475" y="315" class="branch-label">[Obstacle]</text>

                    <!-- [None] -->
                    <path d="M 418,315 L 418,348 L 472,348" class="connector-line" marker-end="url(#arrow)" />
                    <text x="430" y="341" class="branch-label">[None]</text>

                    <!-- 3 actions -> Join Bar -->
                    <path d="M 595,282 L 620,282" class="connector-line" />
                    <path d="M 595,303 L 620,303" class="connector-line" />
                    <path d="M 595,324 L 620,324" class="connector-line" />

                    <!-- Join Bar -> Update Score & Progress -->
                    <path d="M 624,302 L 655,302" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Continue Exploring -> Update Score & Progress -->
                    <path d="M 566,353 L 694,353 L 694,314" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Update Score & Progress -> Continue Exploring? -->
                    <path d="M 734,302 L 757,302" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Continue Exploring? -> Save Game Progress (Database) -->
                    <path d="M 803,302 L 866,302" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Continue Exploring? [No] -> End Exploration -->
                    <path d="M 780,316 L 780,356" class="connector-line" marker-end="url(#arrow)" />
                    <text x="786" y="335" class="branch-label">[No]</text>

                    <!-- Exploration Loop back to Control Boat -->
                    <path d="M 736,368 L 154,368 L 154,316" class="connector-line" marker-end="url(#arrow)" />

                    <!-- End Exploration -> Base Operations (Sec 4) -->
                    <path d="M 780,380 L 780,490 L 570,490" class="connector-line" marker-end="url(#arrow)" />

                    <!-- ---------- Section 4 Connectors ---------- -->
                    <!-- Base Operations distribution bus at top of Sec 4 -->
                    <path d="M 780,391 L 780,398 L 202,398" class="connector-line" />
                    <path d="M 202,398 L 202,406" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 345,398 L 345,406" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 523,398 L 523,406" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Waste Selling: Sell -> Confirm -> Update Coins -->
                    <path d="M 202,423 L 202,435" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 202,452 L 202,461" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 202,478 L 202,512 L 469,512" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Upgrade Boat: Upgrade -> Check Cost -> Enough Coins? -->
                    <path d="M 345,423 L 345,428" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 345,445 L 345,443" class="connector-line" />

                    <!-- Enough Coins? [Yes] -> Apply Upgrade -->
                    <path d="M 346,467 L 346,473" class="connector-line" marker-end="url(#arrow)" />
                    <text x="330" y="467" class="branch-label">[Yes]</text>

                    <!-- Apply Upgrade -> Update Boat Stats -->
                    <path d="M 346,490 L 346,495" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Update Boat Stats -> Return to Main Menu -->
                    <path d="M 393,503 L 430,503 L 430,508 L 469,508" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Enough Coins? [No] -> Show Insufficient Coins -->
                    <path d="M 371,455 L 449,455 L 449,469" class="connector-line" marker-end="url(#arrow)" />
                    <text x="395" y="450" class="branch-label">[No]</text>

                    <!-- Show Insufficient Coins -> Return to Main Menu -->
                    <path d="M 449,488 L 449,508 L 469,508" class="connector-line" />

                    <!-- View Player Report -> Generate & Display Report -->
                    <path d="M 523,423 L 523,438" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Generate & Display Report -> Return to Main Menu -->
                    <path d="M 523,460 L 523,499" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Database Connectors in Section 4 -->
                    <path d="M 570,415 L 868,415" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 570,445 L 867,445" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 570,475 L 867,475" class="connector-line" marker-end="url(#arrow)" />
                    <path d="M 570,415 L 570,475" class="connector-line" />

                    <!-- ---------- Section 5 Connectors ---------- -->
                    <!-- Return to Main Menu -> Logout / Close Game -->
                    <path d="M 519,516 L 519,520" class="connector-line" />

                    <!-- Logout / Close Game -> Save Game Session -->
                    <path d="M 228,536 L 430,536" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Save Game Session -> Store Game Session -->
                    <path d="M 531,536 L 840,536" class="connector-line" marker-end="url(#arrow)" />

                    <!-- Store Game Session -> End -->
                    <path d="M 935,535 L 960,535" class="connector-line" marker-end="url(#arrow)" />
                </g>

                <!-- ==================== 4. SECTION 1 NODES ==================== -->
                <g id="authentication">
                    <!-- Start Symbol: Solid Black Circle -->
                    <circle cx="160" cy="41" r="6.5" fill="#0f172a" />

                    <!-- Open Game -->
                    <rect x="124" y="56" width="73" height="18" class="process-box" />
                    <text x="160" y="68" class="node-text">Open Game</text>

                    <!-- Registered? Decision -->
                    <polygon points="160,81 184,95 160,109 136,95" class="decision-shape" />
                    <text x="160" y="97" class="diamond-text">Registered?</text>

                    <!-- Enter Registration Details -->
                    <rect x="223" y="82" width="95" height="20" class="process-box" />
                    <text x="270" y="95" class="node-text">Enter Registration Details</text>

                    <!-- Login -->
                    <rect x="124" y="122" width="73" height="18" class="process-box" />
                    <text x="160" y="134" class="node-text">Login</text>

                    <!-- Create New User -->
                    <rect x="419" y="78" width="99" height="18" class="process-box" />
                    <text x="468" y="90" class="node-text">Create New User</text>

                    <!-- Validate Login -->
                    <rect x="419" y="104" width="99" height="18" class="process-box" />
                    <text x="468" y="116" class="node-text">Validate Login</text>

                    <!-- Main Menu -->
                    <rect x="419" y="130" width="99" height="18" class="process-box" />
                    <text x="468" y="142" class="node-text">Main Menu</text>

                    <!-- Store User Data (Database) -->
                    <rect x="865" y="62" width="95" height="18" class="process-box" />
                    <text x="912" y="74" class="node-text">Store User Data</text>

                    <!-- Retrieve User Data (Database) -->
                    <rect x="865" y="104" width="95" height="18" class="process-box" />
                    <text x="912" y="116" class="node-text">Retrieve User Data</text>
                </g>

                <!-- ==================== 5. SECTION 2 NODES ==================== -->
                <g id="game-setup">
                    <!-- Select Action -->
                    <rect x="147" y="161" width="80" height="18" class="process-box" />
                    <text x="187" y="173" class="node-text">Select Action</text>

                    <!-- Start Game -->
                    <rect x="123" y="187" width="76" height="18" class="process-box" />
                    <text x="161" y="199" class="node-text">Start Game</text>

                    <!-- View Leaderboard -->
                    <rect x="226" y="181" width="92" height="18" class="process-box" />
                    <text x="272" y="193" class="node-text">View Leaderboard</text>

                    <!-- Configure Settings -->
                    <rect x="347" y="181" width="92" height="18" class="process-box" />
                    <text x="393" y="193" class="node-text">Configure Settings</text>

                    <!-- Exit Game -->
                    <rect x="473" y="181" width="80" height="18" class="process-box" />
                    <text x="513" y="193" class="node-text">Exit Game</text>

                    <!-- Select Ocean Zone -->
                    <rect x="122" y="227" width="78" height="18" class="process-box" />
                    <text x="161" y="239" class="node-text">Select Ocean Zone</text>

                    <!-- Zone Unlocked? Decision -->
                    <polygon points="309,222 332,236 309,250 286,236" class="decision-shape" />
                    <text x="309" y="238" class="diamond-text">Zone Unlocked?</text>

                    <!-- Prepare Boat -->
                    <rect x="380" y="222" width="73" height="18" class="process-box" />
                    <text x="416" y="234" class="node-text">Prepare Boat</text>

                    <!-- Boat Ready? Decision -->
                    <polygon points="507,217 530,231 507,245 484,231" class="decision-shape" />
                    <text x="507" y="233" class="diamond-text">Boat Ready?</text>

                    <!-- Show Repair Message -->
                    <rect x="596" y="221" width="95" height="18" class="process-box" />
                    <text x="643" y="233" class="node-text">Show Repair: Message</text>

                    <!-- Launch Boat -->
                    <rect x="475" y="250" width="74" height="18" class="process-box" />
                    <text x="512" y="262" class="node-text">Launch Boat</text>

                    <!-- Load Zone Data (Database) -->
                    <rect x="865" y="185" width="95" height="18" class="process-box" />
                    <text x="912" y="197" class="node-text">Load Zone Data</text>

                    <!-- Load Boat Data (Database) -->
                    <rect x="865" y="221" width="95" height="18" class="process-box" />
                    <text x="912" y="233" class="node-text">Load Boat Data</text>
                </g>

                <!-- ==================== 6. SECTION 3 NODES ==================== -->
                <g id="ocean-exploration">
                    <!-- Dashed Ocean Exploration Loop Boundary -->
                    <rect x="98" y="275" width="897" height="110" class="loop-boundary" />
                    <!-- Loop Header Tab -->
                    <path d="M 98,285 L 98,274 Q 98,267 105,267 L 203,267 Q 210,267 210,274 L 210,285 Z" fill="#e0f2fe" stroke="#3b82f6" stroke-width="1" />
                    <text x="154" y="276" text-anchor="middle" class="loop-tag">Ocean Exploration Loop</text>

                    <!-- Control Boat (Move / Navigate) -->
                    <rect x="111" y="291" width="86" height="25" class="process-box" />
                    <text x="154" y="302" class="node-text">Control Boat</text>
                    <text x="154" y="311" class="node-text">(Move / Navigate)</text>

                    <!-- Detect Environment -->
                    <rect x="258" y="289" width="100" height="22" class="process-box" />
                    <text x="308" y="303" class="node-text">Detect Environment</text>

                    <!-- Object Detected? Decision -->
                    <polygon points="418,285 446,300 418,315 390,300" class="decision-shape" />
                    <text x="418" y="302" class="diamond-text">Object Detected?</text>

                    <!-- Collect Waste -->
                    <rect x="516" y="271" width="79" height="15" class="process-box" />
                    <text x="555" y="282" class="node-text">Collect Waste</text>

                    <!-- Rescue Marine Life -->
                    <rect x="516" y="292" width="79" height="15" class="process-box" />
                    <text x="555" y="303" class="node-text">Rescue Marine Life</text>

                    <!-- Avoid Obstacle -->
                    <rect x="516" y="313" width="79" height="15" class="process-box" />
                    <text x="555" y="324" class="node-text">Avoid Obstacle</text>

                    <!-- Join Bar (Vertical Black Bar) -->
                    <rect x="620" y="276" width="4" height="52" rx="1" class="sync-bar-shape" />

                    <!-- Continue Exploring -->
                    <rect x="472" y="344" width="94" height="18" class="process-box" />
                    <text x="519" y="356" class="node-text">Continue Exploring</text>

                    <!-- Update Score & Progress -->
                    <rect x="655" y="290" width="79" height="24" class="process-box" />
                    <text x="694" y="301" class="node-text">Update Score &amp;</text>
                    <text x="694" y="310" class="node-text">Progress</text>

                    <!-- Continue Exploring? Decision -->
                    <polygon points="780,288 803,302 780,316 757,302" class="decision-shape" />
                    <text x="780" y="299" class="diamond-text">Continue</text>
                    <text x="780" y="307" class="diamond-text">Exploring?</text>

                    <!-- End Exploration (Return to Base) -->
                    <rect x="736" y="356" width="90" height="24" class="process-box" />
                    <text x="781" y="367" class="node-text">End Exploration</text>
                    <text x="781" y="376" class="node-text">(Return to Base)</text>

                    <!-- Save Game Progress (Database) -->
                    <rect x="866" y="293" width="98" height="18" class="process-box" />
                    <text x="915" y="305" class="node-text">Save Game Progress</text>
                </g>

                <!-- ==================== 7. SECTION 4 NODES ==================== -->
                <g id="base-operations">
                    <!-- Sell Collected Waste -->
                    <rect x="147" y="406" width="110" height="17" class="process-box" />
                    <text x="202" y="418" class="node-text">Sell Collected Waste</text>

                    <!-- Confirm Sale -->
                    <rect x="157" y="435" width="90" height="17" class="process-box" />
                    <text x="202" y="447" class="node-text">Confirm Sale</text>

                    <!-- Update Coins -->
                    <rect x="157" y="461" width="90" height="17" class="process-box" />
                    <text x="202" y="473" class="node-text">Update Coins</text>

                    <!-- Upgrade Boat -->
                    <rect x="292" y="406" width="107" height="17" class="process-box" />
                    <text x="345" y="418" class="node-text">Upgrade Boat</text>

                    <!-- Check Upgrade Cost -->
                    <rect x="295" y="428" width="100" height="17" class="process-box" />
                    <text x="345" y="440" class="node-text">Check Upgrade Cost</text>

                    <!-- Enough Coins? Decision -->
                    <polygon points="346,443 371,455 346,467 321,455" class="decision-shape" />
                    <text x="346" y="457" class="diamond-text">Enough Coins?</text>

                    <!-- Apply Upgrade -->
                    <rect x="298" y="473" width="95" height="17" class="process-box" />
                    <text x="345" y="485" class="node-text">Apply Upgrade</text>

                    <!-- Update Boat Stats -->
                    <rect x="298" y="495" width="95" height="17" class="process-box" />
                    <text x="345" y="507" class="node-text">Update Boat Stats</text>

                    <!-- Show Insufficient Coins -->
                    <rect x="411" y="469" width="76" height="19" class="process-box" />
                    <text x="449" y="478" class="node-text">Show Insufficient</text>
                    <text x="449" y="486" class="node-text">Coins</text>

                    <!-- View Player Report -->
                    <rect x="467" y="406" width="113" height="17" class="process-box" />
                    <text x="523" y="418" class="node-text">View Player Report</text>

                    <!-- Generate & Display Report -->
                    <rect x="469" y="438" width="110" height="22" class="process-box" />
                    <text x="524" y="448" class="node-text">Generate &amp; Display</text>
                    <text x="524" y="456" class="node-text">Report</text>

                    <!-- Return to Main Menu -->
                    <rect x="469" y="499" width="101" height="17" class="process-box" />
                    <text x="519" y="511" class="node-text">Return to Main Menu</text>

                    <!-- Update Player Coins (Database) -->
                    <rect x="868" y="407" width="95" height="17" class="process-box" />
                    <text x="915" y="419" class="node-text">Update Player Coins</text>

                    <!-- Update Boat Data (Database) -->
                    <rect x="867" y="437" width="95" height="17" class="process-box" />
                    <text x="914" y="449" class="node-text">Update Boat Data</text>

                    <!-- Store Player Report (Database) -->
                    <rect x="867" y="467" width="95" height="17" class="process-box" />
                    <text x="914" y="479" class="node-text">Store Player Report</text>
                </g>

                <!-- ==================== 8. SECTION 5 NODES ==================== -->
                <g id="exit">
                    <!-- Logout / Close Game -->
                    <rect x="125" y="527" width="103" height="17" class="process-box" />
                    <text x="176" y="539" class="node-text">Logout / Close Game</text>

                    <!-- Save Game Session -->
                    <rect x="430" y="528" width="101" height="16" class="process-box" />
                    <text x="480" y="540" class="node-text">Save Game Session</text>

                    <!-- Store Game Session (Database) -->
                    <rect x="840" y="526" width="95" height="17" class="process-box" />
                    <text x="887" y="538" class="node-text">Store Game Session</text>

                    <!-- Terminal End Symbol: Bullseye (Outer ring + filled black circle) -->
                    <circle cx="968" cy="535" r="7.5" fill="none" stroke="#0f172a" stroke-width="1.2" />
                    <circle cx="968" cy="535" r="4.5" fill="#0f172a" />
                    <text x="982" y="538" class="node-text-bold">End</text>
                </g>
            </svg>
        </div>
    </div>

    <!-- Panzoom Interactive Controls -->
    <script>
        document.addEventListener("DOMContentLoaded", function () {
            const viewport = document.getElementById("pan-viewport");
            const container = document.getElementById("canvas-container");
            
            const panzoom = Panzoom(viewport, {
                maxScale: 4.0,
                minScale: 0.5,
                step: 0.15,
                contain: false
            });

            container.addEventListener("wheel", function(event) {
                panzoom.zoomWithWheel(event);
            }, { passive: false });

            // Fit nicely into the viewport on initial open
            function fitToScreen() {
                const scaleX = (window.innerWidth - 40) / 1010;
                const scaleY = (window.innerHeight - 40) / 554;
                const initialScale = Math.min(scaleX, scaleY, 1.4);
                
                const initialX = Math.max(10, (window.innerWidth - 1010 * initialScale) / 2);
                const initialY = Math.max(10, (window.innerHeight - 554 * initialScale) / 2);

                panzoom.zoom(initialScale);
                panzoom.pan(initialX, initialY);
            }

            fitToScreen();

            // Double click to reset framing
            container.addEventListener("dblclick", function() {
                fitToScreen();
            });
        });
    </script>
</body>
</html>
'''

if __name__ == "__main__":
    content = generate_exact_svg_html()
    target_path = "c:\\Users\\adity\\Desktop\\Subjects\\SEML\\Assignment - 6\\Activity_Diagram_New.html"
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully generated {target_path} ({len(content)} bytes).")
