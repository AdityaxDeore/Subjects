import os
import base64
import re

dir_path = r"c:\Users\adity\Desktop\Subjects\SEML\Assignment - 7"
html_path = os.path.join(dir_path, "Assignment_7.html")

def read_svg(filename):
    p = os.path.join(dir_path, filename)
    with open(p, "r", encoding="utf-8") as f:
        c = f.read()
    # Strip XML declaration if present
    if c.startswith("<?xml"):
        c = c[c.find("?>")+2:].strip()
    return c

# Read logo as base64
logo_path = os.path.join(dir_path, "pccoelogo.jfif")
with open(logo_path, "rb") as f:
    logo_b64 = base64.b64encode(f.read()).decode("utf-8")
logo_data_uri = f"data:image/jpeg;base64,{logo_b64}"

# Read all SVGs
notations = {
    "initial": read_svg("notation_initial.svg"),
    "action": read_svg("notation_action.svg"),
    "control_flow": read_svg("notation_control_flow.svg"),
    "decision": read_svg("notation_decision.svg"),
    "merge": read_svg("notation_merge.svg"),
    "fork": read_svg("notation_fork.svg"),
    "join": read_svg("notation_join.svg"),
    "swimlanes": read_svg("notation_swimlanes.svg"),
    "final": read_svg("notation_final.svg")
}

flows = {
    "flow1": read_svg("flow_6_1_login.svg"),
    "flow2": read_svg("flow_6_2_preaudit.svg"),
    "flow3": read_svg("flow_6_3_approval.svg"),
    "flow4": read_svg("flow_6_4_weekly.svg"),
    "flow5": read_svg("flow_6_5_completion.svg")
}

master_svg = read_svg("master_activity_diagram.svg")

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEML Assignment 7 - UML 2.0 Activity Diagram for OceanCleanFlow</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    /* ==========================================================================
       PCCOE SEML DESIGN SYSTEM & DUAL-PADDING ARCHITECTURE
       ========================================================================== */
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Plus Jakarta Sans', Arial, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      font-size: 10pt;
      line-height: 1.5;
      color: #0f172a;
      background: #cbd5e1;
      padding: 24px 10px;
      -webkit-font-smoothing: antialiased;
    }}

    .container {{
      max-width: 8.5in;
      margin: 0 auto;
    }}

    .page {{
      min-height: 11in;
      width: 8.5in;
      padding: 0.68in 0.75in;
      background: #ffffff;
      margin: 0 auto 24px auto;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.12), 0 8px 10px -6px rgba(0, 0, 0, 0.08);
      position: relative;
      box-sizing: border-box;
      border-radius: 2px;
    }}

    .page:focus-within {{
      outline: 2px dashed #0284c7;
    }}

    /* Print Architecture */
    @media print {{
      body {{
        background: #ffffff;
        padding: 0;
      }}
      .container {{
        max-width: 100%;
        margin: 0;
        box-shadow: none;
      }}
      .page {{
        width: 100%;
        min-height: auto;
        margin: 0;
        padding: 0.25in 0.35in;
        box-shadow: none;
        border: none;
        page-break-after: always;
        border-radius: 0;
      }}
    }}

    /* ==========================================================================
       PCCOE COVER METADATA TABLE
       ========================================================================== */
    .cover-table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 18px;
      font-family: 'Times New Roman', Times, serif;
    }}
    .cover-table td {{
      border: 1px solid #000;
      padding: 6px 12px;
    }}
    .cover-table .college-info {{
      text-align: center;
      font-weight: bold;
      font-size: 15pt;
      line-height: 1.35;
    }}
    .cover-table .row-centered {{
      text-align: center;
      font-weight: bold;
      font-size: 13.5pt;
    }}
    .cover-table .row-left {{
      text-align: left;
      font-weight: bold;
      font-size: 12.5pt;
    }}
    .logo-container {{
      text-align: center;
      width: 18%;
      padding: 6px !important;
    }}
    .logo-container img {{
      max-width: 95px;
      height: auto;
      display: block;
      margin: 0 auto;
    }}

    /* ==========================================================================
       TYPOGRAPHY
       ========================================================================== */
    h2 {{
      font-size: 13.5pt;
      font-weight: 800;
      color: #0f172a;
      margin-top: 15px;
      margin-bottom: 7px;
      border-bottom: 2px solid #0284c7;
      padding-bottom: 3px;
      letter-spacing: -0.2px;
    }}
    h3 {{
      font-size: 11pt;
      font-weight: 700;
      color: #1e293b;
      margin-top: 12px;
      margin-bottom: 5px;
    }}
    p {{
      text-align: justify;
      line-height: 1.48;
      margin-bottom: 7px;
      color: #334155;
    }}
    ol, ul {{
      margin-left: 20px;
      margin-bottom: 8px;
      color: #334155;
    }}
    li {{
      margin-bottom: 3px;
      line-height: 1.42;
    }}

    code {{
      font-family: 'Fira Code', monospace;
      font-size: 8.5pt;
      background: #f1f5f9;
      color: #0369a1;
      padding: 1px 5px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }}

    /* ==========================================================================
       INFO BOXES & CALLOUTS
       ========================================================================== */
    .info-box {{
      border-radius: 6px;
      padding: 9px 13px;
      margin: 9px 0 10px 0;
      font-size: 9.5pt;
      line-height: 1.42;
      border-left: 4px solid;
    }}
    .info-box.blue {{
      background: #f0f9ff;
      border-color: #0284c7;
      color: #0c4a6e;
    }}
    .info-box.green {{
      background: #f0fdf4;
      border-color: #16a34a;
      color: #14532d;
    }}

    /* ==========================================================================
       PREMIUM STYLED TABLES
       ========================================================================== */
    .styled-table {{
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 10px 0 14px 0;
      font-size: 9pt;
      background: #ffffff;
      border-radius: 6px;
      overflow: hidden;
      border: 1px solid #cbd5e1;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
    }}
    .styled-table thead th {{
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 8pt;
      letter-spacing: 0.5px;
      padding: 8px 10px;
      border: none;
      text-align: left;
    }}
    .styled-table tbody td {{
      padding: 7px 10px;
      border-bottom: 1px solid #e2e8f0;
      border-right: 1px solid #f1f5f9;
      color: #1e293b;
      vertical-align: top;
      line-height: 1.42;
    }}
    .styled-table tbody tr:last-child td {{
      border-bottom: none;
    }}
    .styled-table tbody tr:nth-child(even) {{
      background-color: #f8fafc;
    }}

    /* ==========================================================================
       BADGES & ACTOR PILLS
       ========================================================================== */
    .badge-actor {{
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 7px;
      border-radius: 12px;
      font-size: 7.5pt;
      font-weight: 700;
      letter-spacing: 0.3px;
      text-transform: uppercase;
    }}
    .badge-operator {{
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }}
    .badge-system {{
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
    }}
    .badge-auditor {{
      background: #ccfbf1;
      color: #0f766e;
      border: 1px solid #5eead4;
    }}
    .badge-faculty {{
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fcd34d;
    }}
    .badge-hod {{
      background: #f3e8ff;
      color: #6b21a8;
      border: 1px solid #d8b4fe;
    }}

    .badge-status {{
      display: inline-block;
      padding: 2px 7px;
      font-size: 8pt;
      font-weight: 700;
      border-radius: 4px;
    }}
    .status-pass {{
      background: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }}
    .status-alert {{
      background: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
    }}
    .status-warn {{
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fde047;
    }}

    /* ==========================================================================
       DIAGRAM & NOTATION CONTAINERS (100% INLINE SVG)
       ========================================================================== */
    .diagram-box {{
      text-align: center;
      margin: 6px 0 9px 0;
      padding: 6px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
    }}
    .diagram-box svg {{
      display: block;
      margin: 0 auto;
      max-height: 95px;
      height: auto;
      width: auto;
    }}

    .flow-box {{
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 6px;
      background: #ffffff;
      margin: 6px 0 10px 0;
      text-align: center;
      box-shadow: 0 1px 3px rgba(0,0,0,0.03);
    }}
    .flow-box svg {{
      width: 100%;
      max-height: 120px;
      height: auto;
      display: block;
      margin: 0 auto;
    }}

    .interactive-link {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin: 4px 0 8px 0;
      font-size: 9.5pt;
      color: #0284c7;
      text-decoration: none;
      font-weight: bold;
      border: 1.5px solid #0284c7;
      padding: 6px 14px;
      border-radius: 6px;
      background: #f0f9ff;
      transition: all 0.2s;
    }}
    .interactive-link:hover {{
      background: #0284c7;
      color: #ffffff;
    }}

    /* ==========================================================================
       THE 19 IDENTIFIED ACTIVITIES — STRUCTURED PHASE CARDS
       ========================================================================== */
    .phase-banner {{
      background: linear-gradient(90deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      padding: 5px 10px;
      border-radius: 5px;
      font-size: 8.5pt;
      font-weight: 700;
      letter-spacing: 0.3px;
      margin: 8px 0 6px 0;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .phase-tag {{
      background: #0284c7;
      color: #ffffff;
      font-size: 7.5pt;
      padding: 2px 7px;
      border-radius: 10px;
    }}

    .activity-card {{
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
      padding: 7px 10px;
      margin-bottom: 6px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
    }}
    .activity-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 3px;
    }}
    .act-left {{
      display: flex;
      align-items: center;
      gap: 7px;
    }}
    .act-pill {{
      background: #0f172a;
      color: #ffffff;
      font-family: 'Fira Code', monospace;
      font-size: 7.5pt;
      font-weight: 700;
      padding: 1px 6px;
      border-radius: 4px;
    }}
    .act-title {{
      font-size: 9.5pt;
      font-weight: 700;
      color: #0f172a;
    }}
    .act-desc {{
      font-size: 8.5pt;
      color: #475569;
      line-height: 1.38;
      margin-bottom: 3px;
    }}
    .act-subgrid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      background: #f8fafc;
      padding: 4px 8px;
      border-radius: 4px;
      font-size: 8pt;
      border: 1px solid #f1f5f9;
    }}
    .act-item {{
      color: #334155;
    }}
    .act-label {{
      font-weight: 700;
      color: #0f172a;
    }}

    /* 4-Stage Reconciliation Protocol Grid */
    .protocol-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
      margin: 8px 0 12px 0;
    }}
    .protocol-card {{
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-left: 4px solid #0284c7;
      border-radius: 6px;
      padding: 8px 10px;
    }}
    .protocol-card .title {{
      font-size: 9pt;
      font-weight: 700;
      color: #0f172a;
      margin-bottom: 3px;
    }}
    .protocol-card .desc {{
      font-size: 8pt;
      color: #475569;
      line-height: 1.35;
    }}

    /* Master Diagram Container */
    .master-diagram-card {{
      border: 1.5px solid #cbd5e1;
      border-radius: 8px;
      background: #ffffff;
      padding: 8px;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
      margin: 6px 0;
      text-align: center;
    }}
    .master-diagram-card svg {{
      width: 100%;
      max-height: 745px;
      height: auto;
      display: block;
      margin: 0 auto;
    }}
  </style>
</head>
<body>
  <div class="container" contenteditable="true">
    
    <!-- ==========================================================================
         PAGE 1: COVER, AIM, OBJECTIVES & TOKEN FLOW MECHANICS (PURE SE)
         ========================================================================== -->
    <div class="page">
      <table class="cover-table">
        <tr>
          <td class="logo-container">
            <img src="{logo_data_uri}" alt="PCCOE Logo" contenteditable="false">
          </td>
          <td class="college-info">
            Pimpri Chinchwad Education Trust's<br>
            Pimpri Chinchwad College of Engineering
          </td>
        </tr>
        <tr>
          <td colspan="2" class="row-centered">
            Assignment No. 7
          </td>
        </tr>
        <tr>
          <td colspan="2" class="row-left">
            Course:- Software Engineering and Modeling Laboratory (SEML)
          </td>
        </tr>
        <tr>
          <td colspan="2" class="row-left">
            Name:- Aditya Chandrajit Deore
          </td>
        </tr>
        <tr>
          <td colspan="2" class="row-left">
            PRN:- 124B1F116 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Batch:- B3
          </td>
        </tr>
      </table>

      <h2>Aim</h2>
      <p>To identify and represent the different activities, actions, decisions, and responsibilities involved in the internship and autonomous mission management process of the <strong>OceanCleanFlow &ndash; Department Marine Cleanup Management System</strong> using a UML 2.0 Activity Diagram with swimlanes.</p>

      <h2>Objectives</h2>
      <ol>
        <li>To identify the major operational activities involved in the student operator marine internship application, vessel parameter submission, and multi-tier institutional approval process.</li>
        <li>To represent the flow of activities and decisions from initial cleanup mission proposal to successful 14-week patrol completion, plastic recycling verification, and mission closeout.</li>
        <li>To model the distinct organizational and computational responsibilities of system stakeholders using structured <strong>Swimlanes (Activity Partitions)</strong> across 5 distinct domains.</li>
        <li>To model the complete patrol lifecycle, including automated pre-audit diagnostics, external recycling compliance review, faculty mentor supervision, harbor director departure clearance, weekly telemetry logging, and final dockside weighbridge audits.</li>
        <li>To systematically represent alternative exception flows, including invalid authentication tokens, rejected mission proposals, flagged marine reserve hazards, HOD re-evaluation loops, and iterative document correction loops.</li>
      </ol>

      <h2>Theoretical Overview of UML 2.0 Activity Diagrams</h2>
      <p>An <strong>Activity Diagram</strong> is a behavioral modeling diagram standardized by the Object Management Group (OMG) within UML 2.0. It visually represents the stepwise, dynamic flow of operational control and computational actions within a complex system. Unlike state machine diagrams that model the internal state lifecycle of a single object over time, activity diagrams model cross-functional coordination, concurrency, conditional branching, and data flow across distributed software tiers and human actors.</p>

      <h2>Token Flow Execution Semantics in UML 2.0</h2>
      <p>In UML 2.0, workflow execution is governed by a discrete <strong>token flow mechanism</strong> rather than ad-hoc state transitions. This formal foundation ensures deterministic execution across asynchronous distributed systems:</p>
      
      <ul>
        <li><strong>Token Initiation:</strong> The workflow commences when a control token is deposited at the Initial Node. This token traverses along outgoing directed control edges toward target action nodes.</li>
        <li><strong>Action Firing &amp; Consumption:</strong> An action node is enabled for execution when all required incoming control and data tokens arrive on its input edges. Upon completion, the action consumes the input tokens and emits new control tokens on each outgoing edge.</li>
        <li><strong>Deterministic Decision Routing:</strong> At a decision node, mutually exclusive guard conditions (e.g., <code>[Valid Credentials]</code> vs <code>[Invalid Credentials]</code>) are evaluated sequentially. Exactly one guard evaluates to true, directing the token along the chosen branch without ambiguity.</li>
        <li><strong>Fork &amp; Join Concurrency:</strong> A Fork node duplicates an incoming token across multiple concurrent paths to execute tasks in parallel (e.g., propulsion spin-up and sensor calibration). A Join node halts execution until every incoming concurrent path delivers its token, synchronizing the execution flow.</li>
      </ul>

      <div class="info-box blue">
        <strong>Architectural Principle:</strong> Token flow semantics guarantee that the OceanCleanFlow system operates in a deterministic, deadlock-free manner during distributed marine operations, multi-tier approvals, and weekly iterative telemetry logging.
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 2: MAIN ELEMENTS OF ACTIVITY DIAGRAM (ITEMS 1-4)
         ========================================================================== -->
    <div class="page">
      <h2>Main Elements of an Activity Diagram</h2>
      <p>UML 2.0 standardizes graphical notations to describe workflow sequencing, concurrency, decision branches, and responsibilities with complete visual precision. Below are the primary atomic notations:</p>

      <h3>1. Initial Node</h3>
      <p>The initial node denotes the starting entry point of the workflow. Graphically, it is rendered as a solid filled circle. An activity diagram can possess only one primary initial node per structured control flow. In OceanCleanFlow, the process triggers when the student operator initiates the mission application workflow.</p>
      <div class="diagram-box">
        {notations["initial"]}
      </div>

      <h3>2. Action / Activity Node</h3>
      <p>An action represents an atomic, non-interruptible operational step or computational task performed by an actor or automated software service. It is rendered as a rectangle with smoothly rounded corners. Typical actions in OceanCleanFlow include <em>Login to Portal</em>, <em>Submit Mission Request</em>, <em>Execute Automated Pre-Audit Diagnostics</em>, and <em>Verify Completion Manifest</em>.</p>
      <div class="diagram-box">
        {notations["action"]}
      </div>

      <h3>3. Control Flow</h3>
      <p>Control flow lines depict the sequential ordering and direction of activity execution. They are drawn as solid directed lines with an open arrowhead pointing from the source node to the target node. For example: <code>Login → Verify Login Credentials → Submit Mission Request → Upload Permits</code>.</p>
      <div class="diagram-box">
        {notations["control_flow"]}
      </div>

      <h3>4. Decision Node</h3>
      <p>A decision node routes workflow execution along alternative paths based on the evaluation of conditional guard expressions. It is represented by a diamond shape with a single incoming control flow and two or more outgoing flows labeled with mutually exclusive guard conditions (e.g., <code>[Valid]</code> / <code>[Invalid]</code> or <code>[Approved]</code> / <code>[Rejected]</code>).</p>
      <div class="diagram-box">
        {notations["decision"]}
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 3: MAIN ELEMENTS CONTINUED (ITEMS 5-9)
         ========================================================================== -->
    <div class="page">
      <h2>Main Elements of an Activity Diagram (Contd.)</h2>

      <h3>5. Merge Node</h3>
      <p>A merge node consolidates multiple alternative incoming control paths into a single outgoing flow without requiring synchronization. It is depicted as a diamond shape with multiple incoming flows and one outgoing flow. In OceanCleanFlow, dedicated merge nodes allow operators to retry authentication, revise rejected proposals, re-upload documents, and resubmit weight manifests cleanly without ambiguous loops.</p>
      <div class="diagram-box">
        {notations["merge"]}
      </div>

      <h3>6. Fork Node</h3>
      <p>A fork node divides a single incoming control flow into two or more concurrent, parallel execution paths. It is represented by a thick solid horizontal or vertical coordination bar. In OceanCleanFlow, a fork is used during vessel pre-launch diagnostics to trigger concurrent propulsion spin-up, sensor telemetry calibration, and satellite synchronization.</p>
      <div class="diagram-box">
        {notations["fork"]}
      </div>

      <h3>7. Join Node</h3>
      <p>A join node synchronizes multiple concurrent incoming parallel paths into a single unified control flow. It is represented by a thick solid coordination bar. Control halts at the join bar until all incoming concurrent paths have completed execution and delivered their tokens.</p>
      <div class="diagram-box">
        {notations["join"]}
      </div>

      <h3>8. Swimlanes (Activity Partitions)</h3>
      <p>Swimlanes partition the activity diagram according to the organizational, departmental, or architectural responsibilities of participants. Each action is positioned strictly inside the vertical column of the actor or system tier responsible for its execution (e.g., Operator, Autonomous System, External Auditor, Faculty Mentor, Harbor HOD).</p>
      <div class="diagram-box">
        {notations["swimlanes"]}
      </div>

      <h3>9. Activity Final Node</h3>
      <p>The activity final node indicates the complete termination of the entire workflow. It is represented by a bullseye circle containing a solid filled black circle. In OceanCleanFlow, execution terminates after all 14 patrol weeks are completed, plastic tonnage is verified, the completion certificate is issued, and operator debriefing feedback is submitted.</p>
      <div class="diagram-box">
        {notations["final"]}
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 4: 5 SWIMLANES & CROSS-FUNCTIONAL MATRIX (FIX #9)
         ========================================================================== -->
    <div class="page">
      <h2>Swimlane Partitions &amp; Architectural Responsibilities</h2>
      <p>Swimlanes establish unambiguous architectural boundaries of responsibility across the <strong>five distinct stakeholders</strong> involved in the ocean cleanup lifecycle. By separating concerns into dedicated partitions, the system prevents role confusion and enforces strict separation of duties:</p>

      <table class="styled-table">
        <thead>
          <tr>
            <th style="width: 25%;">Swimlane / Actor</th>
            <th style="width: 37%;">Core Responsibilities</th>
            <th style="width: 38%;">Primary Activities Handled</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>1. Operator / Player</strong><br>
              <span class="badge-actor badge-operator">Student Researcher</span>
            </td>
            <td>
              Initiates mission proposals, inputs vessel technical specifications, uploads compliance documentation, executes autonomous cleanup patrols, submits weekly logs, and uploads dockside weighbridge receipts.
            </td>
            <td>
              <code>ACT-01</code> Login to Portal<br>
              <code>ACT-03</code> Submit Mission Request<br>
              <code>ACT-04</code> Upload Seaworthiness Permits<br>
              <code>ACT-10</code> Start Ocean Cleanup Mission<br>
              <code>ACT-11</code> Submit Weekly Patrol Log<br>
              <code>ACT-14</code> Dock Vessel at Slipway<br>
              <code>ACT-15</code> Upload Waste Manifest<br>
              <code>ACT-19</code> Submit Final Feedback
            </td>
          </tr>
          <tr>
            <td>
              <strong>2. OceanCleanFlow System</strong><br>
              <span class="badge-actor badge-system">Autonomous Backend</span>
            </td>
            <td>
              Validates cryptographic credentials, executes automated pre-audit diagnostics, activates vessel schedule tokens, records weekly telemetry streams, locks persistent logbooks, and issues digital certificates.
            </td>
            <td>
              <code>ACT-02</code> Verify Login Credentials<br>
              <code>ACT-05</code> Execute Pre-Audit Diagnostics<br>
              <code>ACT-09</code> Activate Vessel Schedule<br>
              <code>ACT-12</code> Record Weekly Telemetry<br>
              <code>ACT-17</code> Mark Mission COMPLETED<br>
              <code>ACT-18</code> Record Mass &amp; Issue Certificate
            </td>
          </tr>
          <tr>
            <td>
              <strong>3. External Recycling Auditor</strong><br>
              <span class="badge-actor badge-auditor">Accredited Auditor</span>
            </td>
            <td>
              External statutory authority that audits offloaded recycling partner credentials, verifies marine sanctuary boundary compliance, and issues environmental clearance.
            </td>
            <td>
              <code>ACT-06</code> Verify Recycling Partner &amp; Marine Sanctuary Boundaries
            </td>
          </tr>
          <tr>
            <td>
              <strong>4. Faculty Mentor</strong><br>
              <span class="badge-actor badge-faculty">Academic Supervisor</span>
            </td>
            <td>
              Reviews mission proposals and route safety dossiers, endorses/rejects student applications, audits weekly progress telemetry logs, and inspects final dockside weighbridge receipts.
            </td>
            <td>
              <code>ACT-07</code> Review Mission Proposal<br>
              <code>ACT-13</code> Review Weekly Progress Log<br>
              <code>ACT-16</code> Audit Weighbridge Receipts &amp; Sorting Records
            </td>
          </tr>
          <tr>
            <td>
              <strong>5. Harbor Director (HOD)</strong><br>
              <span class="badge-actor badge-hod">Station Chief</span>
            </td>
            <td>
              Institutional maritime authority governing harbor slipway berths, channel navigation safety, and official port departure clearances.
            </td>
            <td>
              <code>ACT-08</code> Review Berth Allocation &amp; Harbor Traffic Clearance
            </td>
          </tr>
        </tbody>
      </table>

      <h2>Cross-Functional Stakeholder Interaction Matrix</h2>
      <p>The table below summarizes the operational handoffs between swimlane partitions during critical workflow state transitions:</p>

      <table class="styled-table">
        <thead>
          <tr>
            <th style="width: 22%;">Transition Point</th>
            <th style="width: 26%;">Source Actor &rarr; Target Actor</th>
            <th style="width: 26%;">Transferred Artifact / Token</th>
            <th style="width: 26%;">Validation Criterion</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Application Intake</strong></td>
            <td>Operator &rarr; System</td>
            <td>Vessel Specs &amp; Insurance PDF</td>
            <td>Schema validation &amp; file integrity</td>
          </tr>
          <tr>
            <td><strong>Compliance Audit</strong></td>
            <td>System &rarr; External Auditor</td>
            <td>One-Time Audit Token Link</td>
            <td>Recycling facility accreditation</td>
          </tr>
          <tr>
            <td><strong>Academic Review</strong></td>
            <td>Auditor &rarr; Faculty Mentor</td>
            <td>Proposal Dossier &amp; Safety Flags</td>
            <td>Educational &amp; environmental viability</td>
          </tr>
          <tr>
            <td><strong>Harbor Departure</strong></td>
            <td>Faculty &rarr; Harbor HOD</td>
            <td>Endorsed Departure Packet</td>
            <td>Harbor traffic &amp; weather clearance</td>
          </tr>
          <tr>
            <td><strong>Weekly Verification</strong></td>
            <td>System &rarr; Faculty Mentor</td>
            <td>Weekly Telemetry &amp; Log Entry</td>
            <td>Zero bycatch &amp; valid battery curves</td>
          </tr>
          <tr>
            <td><strong>Final Closeout</strong></td>
            <td>Faculty Mentor &rarr; System</td>
            <td>Certified Offload Weighbridge Slip</td>
            <td>Mass balance match (&le; 2% delta)</td>
          </tr>
        </tbody>
      </table>
    </div>

    <!-- ==========================================================================
         PAGE 5: THE 19 IDENTIFIED ACTIVITIES — PART 1 (PHASES 1 & 2)
         ========================================================================== -->
    <div class="page">
      <h2>The 19 Identified System Activities (Phases 1 &amp; 2)</h2>
      <p>The OceanCleanFlow workflow is formalized into 19 discrete atomic activities. Each activity features defined trigger preconditions, operational behavior, and deliverable state postconditions:</p>

      <!-- PHASE 1 -->
      <div class="phase-banner">
        <span>PHASE 1: OPERATOR AUTHENTICATION &amp; MISSION PROPOSAL</span>
        <span class="phase-tag">ACTIVITIES 01 &ndash; 04</span>
      </div>

      <!-- ACT 01 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-01</span>
            <span class="act-title">Login to OceanCleanFlow Portal</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Student operator inputs institutional credentials into the web command terminal to initialize a secure session.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> User credentials, institutional password hash.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Inbound authentication request dispatched to backend.</div>
        </div>
      </div>

      <!-- ACT 02 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-02</span>
            <span class="act-title">Verify Login Credentials &amp; Session</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System validates credentials against identity directory. If invalid, displays error and returns to login merge node.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Inbound credentials from ACT-01.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> JWT session token granted [Valid] or error thrown [Invalid].</div>
        </div>
      </div>

      <!-- ACT 03 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-03</span>
            <span class="act-title">Submit Mission Request &amp; Vessel / Sector Specs</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator defines mission profile, hull specifications, battery capacity, debris payload limits, and GPS boundary coordinates.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Validated session; vessel specification form.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Mission draft created with status <code>DRAFT_PROPOSAL</code>.</div>
        </div>
      </div>

      <!-- ACT 04 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-04</span>
            <span class="act-title">Upload Seaworthiness Permits &amp; Insurance PDFs</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator uploads mandatory compliance documents: seaworthiness certificate, hull insurance policy, and safety checklist.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> PDF compliance certificates, signed indemnity bond.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Document attachments hashed and linked to proposal dossier.</div>
        </div>
      </div>

      <!-- PHASE 2 -->
      <div class="phase-banner">
        <span>PHASE 2: AUTOMATED PRE-AUDIT &amp; EXTERNAL COMPLIANCE</span>
        <span class="phase-tag">ACTIVITIES 05 &ndash; 06</span>
      </div>

      <!-- ACT 05 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-05</span>
            <span class="act-title">Execute Automated Pre-Audit Diagnostics</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System performs automated static diagnostics on vessel specs, verifies digital signatures, and checks power-to-weight safety limits.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Submitted specs and uploaded PDF attachments from ACT-04.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Pre-audit diagnostic report generated; error flags route to retry.</div>
        </div>
      </div>

      <!-- ACT 06 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-06</span>
            <span class="act-title">Verify Recycling Partner &amp; Marine Sanctuaries</span>
          </div>
          <span class="badge-actor badge-auditor">External Auditor</span>
        </div>
        <div class="act-desc">External auditor accesses proposal via one-time secure token to verify facility recycling licensing and sanctuary proximity.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Audit dispatch link, GPS coordinates, recycling partner ID.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Auditor compliance signoff; hazard flags route to boundary adjustment.</div>
        </div>
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 6: THE 19 IDENTIFIED ACTIVITIES — PART 2 (PHASES 3, 4 & 5)
         ========================================================================== -->
    <div class="page">
      <h2>The 19 Identified System Activities (Phases 3, 4 &amp; 5)</h2>
      <p>The institutional approval, operational deployment, and mission closeout phases govern vessel departure, patrol tracking, and final certification:</p>

      <!-- PHASE 3 -->
      <div class="phase-banner">
        <span>PHASE 3: ACADEMIC &amp; HARBOR INSTITUTIONAL APPROVAL</span>
        <span class="phase-tag">ACTIVITIES 07 &ndash; 09</span>
      </div>

      <!-- ACT 07 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-07</span>
            <span class="act-title">Review Mission Proposal &amp; Route Safety Dossier</span>
          </div>
          <span class="badge-actor badge-faculty">Faculty Mentor</span>
        </div>
        <div class="act-desc">Faculty mentor reviews proposal dossier, route feasibility, student learning objectives, and environmental flags.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Cleared dossier &amp; environmental report from ACT-06.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Faculty assessment rubric completed [Approved] / [Rejected].</div>
        </div>
      </div>

      <!-- ACT 08 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-08</span>
            <span class="act-title">Review Berth Allocation &amp; Harbor Traffic Clearance</span>
          </div>
          <span class="badge-actor badge-hod">Harbor Director (HOD)</span>
        </div>
        <div class="act-desc">Harbor Director evaluates port traffic, weather radar, and berth allocation, issuing final legal departure authorization.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Faculty-endorsed departure packet from ACT-07.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Clearance granted [Cleared] or returned [Clearance Denied].</div>
        </div>
      </div>

      <!-- ACT 09 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-09</span>
            <span class="act-title">Activate Vessel Schedule &amp; Issue Departure Token</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System activates vessel operating window in mission registry and generates cryptographically signed departure token.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Harbor Director departure clearance from ACT-08.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Status set to <code>SCHEDULED</code>; token dispatched to vessel.</div>
        </div>
      </div>

      <!-- PHASE 4 -->
      <div class="phase-banner">
        <span>PHASE 4: AUTONOMOUS DEPLOYMENT &amp; 14-WEEK PATROL LOOP</span>
        <span class="phase-tag">ACTIVITIES 10 &ndash; 13</span>
      </div>

      <!-- ACT 10 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-10</span>
            <span class="act-title">Start Ocean Cleanup Mission (Vessel Enters Sector)</span>
          </div>
          <span class="badge-actor badge-operator">Operator &amp; Vessel</span>
        </div>
        <div class="act-desc">Vessel propulsion activates, autopilot disengages moorings, and the autonomous boat enters designated patrol coordinates.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Departure token from ACT-09.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> State transitions to <code>IN_PATROL</code>; week counter initialized to 1.</div>
        </div>
      </div>

      <!-- ACT 11 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-11</span>
            <span class="act-title">Submit Weekly Patrol Log (Plastic Tonnage &amp; Telemetry)</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator submits weekly telemetry log: kilograms of plastic recovered, battery degradation curves, and zero-bycatch sensor logs.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> 7-day patrol telemetry packet; weekly prompt.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Weekly progress report submitted for academic review.</div>
        </div>
      </div>

      <!-- ACT 12 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-12</span>
            <span class="act-title">Record Weekly Telemetry &amp; Increment Week Counter</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System persists incoming telemetry to database, verifies payload sensor thresholds, and increments weekly cycle count.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Weekly telemetry log from ACT-11.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Persistent record committed; week counter updated.</div>
        </div>
      </div>

      <!-- ACT 13 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-13</span>
            <span class="act-title">Review Weekly Progress Log &amp; Sign Off Wildlife Safety</span>
          </div>
          <span class="badge-actor badge-faculty">Faculty Mentor</span>
        </div>
        <div class="act-desc">Faculty mentor reviews debris volume, checks wildlife safety pings, logs operational remarks, and endorses week completion.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Telemetry stream from ACT-12.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Log endorsed; evaluates <code>[Week &lt; 14]</code> vs <code>[Week = 14]</code>.</div>
        </div>
      </div>

      <!-- PHASE 5 -->
      <div class="phase-banner">
        <span>PHASE 5: DOCKING, RECYCLING AUDIT &amp; MISSION CLOSEOUT</span>
        <span class="phase-tag">ACTIVITIES 14 &ndash; 19</span>
      </div>

      <!-- ACT 14 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-14</span>
            <span class="act-title">Dock Vessel at Harbor Dedicated Recycling Slipway</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Upon completing 14 weeks, vessel returns to harbor recycling slipway and offloads plastic to shore weighbridge.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Completion of 14-week patrol cycle.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Vessel safely berthed; physical offload commences.</div>
        </div>
      </div>

      <!-- ACT 15 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-15</span>
            <span class="act-title">Upload Final Waste Manifest &amp; Shore Weighbridge Receipts</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator uploads weighbridge weight slips and polymer category sorting manifests for faculty review.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Shore weighbridge receipts &amp; polymer manifest.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Offload completion dossier uploaded for audit.</div>
        </div>
      </div>

      <!-- ACT 16 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-16</span>
            <span class="act-title">Audit Weighbridge Receipts &amp; NIR Polymer Sorting Records</span>
          </div>
          <span class="badge-actor badge-faculty">Faculty Mentor</span>
        </div>
        <div class="act-desc">Faculty mentor audits physical weighbridge certificates against vessel onboard bin load-cell telemetry for mass reconciliation.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Completion dossier from ACT-15.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Verified mass balance certificate [Verified] / [Discrepancy &gt; 2%].</div>
        </div>
      </div>

      <!-- ACT 17-19 combined summary -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT 17-19</span>
            <span class="act-title">Final Closeout: State Transition, Certificate Issuance &amp; Feedback</span>
          </div>
          <span class="badge-actor badge-system">System &amp; Operator</span>
        </div>
        <div class="act-desc"><code>ACT-17</code> System marks mission <code>COMPLETED</code> and locks logbooks. <code>ACT-18</code> System records diverted mass and issues completion certificate. <code>ACT-19</code> Operator completes final debriefing survey, terminating at Activity Final Node.</div>
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 7: STEP-BY-STEP ACTIVITY FLOWS (6.1 TO 6.3) (100% INLINE SVG)
         ========================================================================== -->
    <div class="page">
      <h2>Step-by-Step Activity Flows (Phases 6.1 to 6.3)</h2>

      <h3>6.1 Operator Login and Mission Application Flow</h3>
      <p>The workflow initiates when the operator accesses the portal. The system evaluates login credentials at a decision node. If invalid, the flow returns directly to the login merge node without redundant intermediate merges. Upon valid authentication, the operator submits mission parameters, configures vessel load limits, and uploads seaworthiness compliance documents.</p>
      
      <div class="flow-box">
        {flows["flow1"]}
      </div>

      <h3>6.2 Pre-Audit Checks and External Auditor Verification Flow</h3>
      <p>Upon proposal submission, the system executes automated pre-audit diagnostics on telemetry schemas and file signatures. If rejected, the operator is prompted to re-upload documents. If valid, an automated time-locked token is dispatched to the External Recycling Auditor (Swimlane 3), who reviews environmental compliance and sanctuary clearance before forwarding to faculty review.</p>

      <div class="flow-box">
        {flows["flow2"]}
      </div>

      <h3>6.3 Faculty Mentor and Harbor Director Institutional Approval Flow</h3>
      <p>The Faculty Mentor evaluates mission route safety, proposed patrol sectors, and auditor notes. If rejected, corrective remarks route back for proposal revision. If approved, the system forwards the dossier to the Harbor Director (HOD) for official maritime clearance. If clearance is denied, control loops back directly to the Faculty Review Merge Node for route re-evaluation.</p>

      <div class="flow-box">
        {flows["flow3"]}
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 8: STEP-BY-STEP ACTIVITY FLOWS (6.4 & 6.5) & RECONCILIATION PROTOCOL
         ========================================================================== -->
    <div class="page">
      <h2>Step-by-Step Activity Flows (Phases 6.4 &amp; 6.5)</h2>

      <h3>6.4 Weekly Progress Tracking and 14-Week Patrol Milestone Loop</h3>
      <p>Upon maritime departure clearance, the vessel engages autonomous route navigation. Every 7 days, the student operator compiles and submits an operational telemetry log detailing debris tonnage recovered, battery endurance, and marine wildlife pings. The Faculty Mentor reviews the log. The system evaluates the loop condition: if fewer than 14 weeks have elapsed (<code>[Week &lt; 14: Continue Patrol Loop]</code>), the loop iterates; once 14 weeks are satisfied (<code>[Week = 14: Patrol Complete]</code>), control transitions to harbor docking.</p>

      <div class="flow-box">
        {flows["flow4"]}
      </div>

      <h3>6.5 Mission Completion, Recycling Verification &amp; Closeout</h3>
      <p>At the conclusion of the 14-week patrol, the vessel docks at the harbor recycling slipway. The operator uploads certified weighbridge slips and polymer manifests. The Faculty Mentor audits physical slips against onboard bin load-cell logs. If variance exceeds 2%, control returns directly to the Manifest Merge Node for resubmission. Upon successful verification, the mission is marked completed, the digital completion certificate is issued, and the operator completes debriefing feedback.</p>

      <div class="flow-box">
        {flows["flow5"]}
      </div>

      <h2>Dockside Offload Reconciliation &amp; Closeout Protocol</h2>
      <p>When the Faculty Mentor verifies dockside offload receipts, the system executes an automated four-stage software engineering verification protocol:</p>

      <div class="protocol-grid">
        <div class="protocol-card">
          <div class="title">1. Weighbridge Telemetry Intake</div>
          <div class="desc">Harbor slipway digital weighbridge transmits gross tare and net payload weight slips directly to the OceanCleanFlow intake API.</div>
        </div>
        <div class="protocol-card">
          <div class="title">2. Load-Cell Cross Reconciliation</div>
          <div class="desc">System cross-compares weighbridge slips against cumulative vessel bin load-cell logs, verifying variance is within acceptable &le; 2.0% tolerance.</div>
        </div>
        <div class="protocol-card">
          <div class="title">3. Polymer Sorting Certification</div>
          <div class="desc">External recycling facility issues Near-Infrared (NIR) spectroscopic classification certificate for PET, HDPE, and recovered ghost net nylon.</div>
        </div>
        <div class="protocol-card">
          <div class="title">4. Tamper-Proof State Locking</div>
          <div class="desc">System sets lifecycle state to <code>COMPLETED</code>, cryptographically seals 14-week telemetry logs, and issues official academic internship signoff.</div>
        </div>
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 9: MASTER UML 2.0 ACTIVITY DIAGRAM VISUALIZATION (100% INLINE & VISIBLE)
         ========================================================================== -->
    <div class="page">
      <h2>Master UML 2.0 Activity Diagram &mdash; Full System View</h2>
      <p>The complete end-to-end activity model unites all five swimlanes, decision nodes, parallel synchronization, weekly iteration loops, and exception correction paths into a cohesive, non-blocking operational workflow:</p>

      <div style="text-align: center; margin: 4px 0 8px 0;">
        <a href="Activity_Diagram_Assignment_7.html" class="interactive-link" contenteditable="false" target="_blank">
          &#x1F517; Launch Full Screen Pan &amp; Zoom Interactive Canvas (Activity_Diagram_Assignment_7.html)
        </a>
      </div>

      <!-- Completely visible master diagram rendered directly inline for zero loading failures -->
      <div class="master-diagram-card">
        {master_svg}
      </div>

      <div style="font-size: 8.5pt; color: #475569; text-align: center; margin-top: 4px;">
        <strong>Figure 7.0:</strong> Complete 5-Swimlane UML 2.0 Activity Diagram for OceanCleanFlow System (Partitions: Operator, System, External Auditor, Faculty Mentor, Harbor HOD).
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 10: EXCEPTION HANDLING, VERIFICATION CHECKLIST & CONCLUSION
         ========================================================================== -->
    <div class="page">
      <h2>Alternative Flows, Exception Handling &amp; Verification</h2>
      <p>A robust software engineering model must systematically account for operational anomalies, sensor faults, document discrepancies, and administrative rejections without reaching permanent deadlock:</p>

      <table class="styled-table">
        <thead>
          <tr>
            <th style="width: 25%;">Failure Scenario</th>
            <th style="width: 32%;">System Detection Mechanism</th>
            <th style="width: 43%;">Alternative Control Flow &amp; Recovery Path</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>
              <strong>Invalid Authentication</strong><br>
              <span class="badge-status status-alert">Security Error</span>
            </td>
            <td>Credential hash mismatch, expired token, or unregistered PRN.</td>
            <td>System routes flow to error action, clears password buffer, and returns to login merge node.</td>
          </tr>
          <tr>
            <td>
              <strong>Pre-Audit Doc Failure</strong><br>
              <span class="badge-status status-warn">Data Error</span>
            </td>
            <td>Corrupted file, missing insurance certificate, or expired seaworthiness permit.</td>
            <td>System generates error report, highlights defective file, and loops back to upload action.</td>
          </tr>
          <tr>
            <td>
              <strong>Environmental Hazard</strong><br>
              <span class="badge-status status-warn">Compliance Alert</span>
            </td>
            <td>External auditor detects proximity to protected coral reef or breeding ground.</td>
            <td>Request flagged with high priority; returned to operator proposal merge node for boundary adjustment.</td>
          </tr>
          <tr>
            <td>
              <strong>Faculty / HOD Rejection</strong><br>
              <span class="badge-status status-alert">Rejection</span>
            </td>
            <td>Adverse weather forecast, harbor channel congestion, or unapproved sector.</td>
            <td>HOD rejection returns directly to Faculty Review Merge Node for route re-evaluation; Faculty rejection returns to proposal merge.</td>
          </tr>
          <tr>
            <td>
              <strong>Mid-Patrol Link Loss</strong><br>
              <span class="badge-status status-warn">Telemetry Alert</span>
            </td>
            <td>Satellite telemetry packet timeout &gt; 15 minutes during patrol.</td>
            <td>Vessel switches to autonomous station-keeping and emergency beacon until link is re-established.</td>
          </tr>
          <tr>
            <td>
              <strong>Manifest Discrepancy</strong><br>
              <span class="badge-status status-alert">Audit Discrepancy</span>
            </td>
            <td>Harbor weighbridge certificate differs from boat load-cell logs by &gt; 2%.</td>
            <td>Supervisor rejects manifest; flow returns directly to Manifest Merge Node for document correction and weight reconciliation.</td>
          </tr>
        </tbody>
      </table>

      <h2>UML 2.0 Formal Verification Checklist</h2>
      <table class="styled-table">
        <thead>
          <tr>
            <th style="width: 28%;">Formal Modeling Criterion</th>
            <th style="width: 20%;">Verification Status</th>
            <th style="width: 52%;">Compliance Justification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Deadlock Prevention</strong></td>
            <td><span class="badge-status status-pass">&#10004; Verified</span></td>
            <td>Every conditional branch either rejoins a valid merge node or reaches the Activity Final Node.</td>
          </tr>
          <tr>
            <td><strong>Guard Mutex Property</strong></td>
            <td><span class="badge-status status-pass">&#10004; Verified</span></td>
            <td>All decision node outputs evaluate mutually exclusive conditions (e.g., <code>[Valid]</code> vs <code>[Invalid]</code>).</td>
          </tr>
          <tr>
            <td><strong>Partition Isolation</strong></td>
            <td><span class="badge-status status-pass">&#10004; Verified</span></td>
            <td>Actions and decision diamonds are strictly localized within their designated swimlane column across all 5 partitions.</td>
          </tr>
          <tr>
            <td><strong>Cyclic Termination</strong></td>
            <td><span class="badge-status status-pass">&#10004; Verified</span></td>
            <td>The 14-week patrol loop is governed by an incrementing counter ensuring deterministic exit (<code>[Week = 14]</code>).</td>
          </tr>
        </tbody>
      </table>

      <h2>Conclusion</h2>
      <p>Through this assignment, we successfully architected, modeled, and verified a comprehensive <strong>UML 2.0 Activity Diagram</strong> with five structured swimlanes for the <strong>OceanCleanFlow &ndash; Department Marine Cleanup Management System</strong>. The model captures the complete operational lifecycle from initial operator authentication, proposal submission, and automated pre-audit diagnostics, through external environmental compliance review, faculty mentor supervision, and institutional HOD harbor clearance. Furthermore, the 14-week iterative patrol tracking loop, dockside weighbridge verification, automated offload reconciliation, and exception recovery paths were thoroughly formalized. This delivers a robust, unambiguous behavioral blueprint for engineering the platform's backend workflow and autonomous marine vessel operations.</p>

      <h3 style="margin-top: 15px;">Signatures and Verification</h3>
      <table style="width: 100%; margin-top: 18px; border-collapse: collapse; font-family: 'Plus Jakarta Sans', Arial, sans-serif;">
        <tr>
          <td style="width: 50%; text-align: left; vertical-align: bottom;">
            <strong>Student Signature:</strong> Aditya Chandrajit Deore<br>
            <strong>Date:</strong> 17th October 2026<br>
            <strong>PRN:</strong> 124B1F116 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <strong>Batch:</strong> B3
          </td>
          <td style="width: 50%; text-align: right; vertical-align: bottom;">
            <strong>Faculty Assessment:</strong> _______________________<br>
            <strong>Marks / Grade:</strong> _______________________<br>
            <strong>Signature with Seal:</strong> _______________________
          </td>
        </tr>
      </table>
    </div>

  </div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"Self-contained HTML successfully written to {html_path} ({len(html)} bytes)!")
