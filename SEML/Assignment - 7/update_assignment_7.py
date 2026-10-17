import os

output_path = r"c:\Users\adity\Desktop\Subjects\SEML\Assignment - 7\Assignment_7.html"

html_content = """<!DOCTYPE html>
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
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      font-size: 10pt;
      line-height: 1.5;
      color: #0f172a;
      background: #cbd5e1;
      padding: 24px 10px;
      -webkit-font-smoothing: antialiased;
    }

    .container {
      max-width: 8.5in;
      margin: 0 auto;
    }

    .page {
      min-height: 11in;
      width: 8.5in;
      padding: 0.72in 0.78in;
      background: #ffffff;
      margin: 0 auto 24px auto;
      box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.12), 0 8px 10px -6px rgba(0, 0, 0, 0.08);
      position: relative;
      box-sizing: border-box;
      border-radius: 2px;
    }

    .page:focus-within {
      outline: 2px dashed #0284c7;
    }

    /* Print Architecture */
    @media print {
      body {
        background: #ffffff;
        padding: 0;
      }
      .container {
        max-width: 100%;
        margin: 0;
        box-shadow: none;
      }
      .page {
        width: 100%;
        min-height: auto;
        margin: 0;
        padding: 0.25in 0.35in;
        box-shadow: none;
        border: none;
        page-break-after: always;
        border-radius: 0;
      }
    }

    /* ==========================================================================
       PCCOE COVER METADATA TABLE
       ========================================================================== */
    .cover-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 20px;
      font-family: 'Times New Roman', Times, serif;
    }
    .cover-table td {
      border: 1px solid #000;
      padding: 7px 12px;
    }
    .cover-table .college-info {
      text-align: center;
      font-weight: bold;
      font-size: 15pt;
      line-height: 1.35;
    }
    .cover-table .row-centered {
      text-align: center;
      font-weight: bold;
      font-size: 13.5pt;
    }
    .cover-table .row-left {
      text-align: left;
      font-weight: bold;
      font-size: 12.5pt;
    }
    .logo-container {
      text-align: center;
      width: 18%;
      padding: 6px !important;
    }
    .logo-container img {
      max-width: 95px;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    /* ==========================================================================
       TYPOGRAPHY
       ========================================================================== */
    h2 {
      font-size: 13.5pt;
      font-weight: 800;
      color: #0f172a;
      margin-top: 16px;
      margin-bottom: 8px;
      border-bottom: 2px solid #0284c7;
      padding-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 8px;
      letter-spacing: -0.2px;
    }
    h3 {
      font-size: 11pt;
      font-weight: 700;
      color: #1e293b;
      margin-top: 14px;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    p {
      text-align: justify;
      line-height: 1.5;
      margin-bottom: 8px;
      color: #334155;
    }
    ol, ul {
      margin-left: 20px;
      margin-bottom: 10px;
      color: #334155;
    }
    li {
      margin-bottom: 4px;
      line-height: 1.45;
    }

    code {
      font-family: 'Fira Code', monospace;
      font-size: 8.5pt;
      background: #f1f5f9;
      color: #0369a1;
      padding: 1px 5px;
      border-radius: 4px;
      border: 1px solid #e2e8f0;
    }

    /* ==========================================================================
       INFO BOXES & CALLOUTS
       ========================================================================== */
    .info-box {
      border-radius: 6px;
      padding: 10px 14px;
      margin: 10px 0 12px 0;
      font-size: 9.5pt;
      line-height: 1.45;
      border-left: 4px solid;
    }
    .info-box.blue {
      background: #f0f9ff;
      border-color: #0284c7;
      color: #0c4a6e;
    }
    .info-box.green {
      background: #f0fdf4;
      border-color: #16a34a;
      color: #14532d;
    }
    .info-box.amber {
      background: #fffbeb;
      border-color: #d97706;
      color: #78350f;
    }

    /* ==========================================================================
       PREMIUM STYLED TABLES (PROFESSIONAL SLATE THEME)
       ========================================================================== */
    .styled-table {
      width: 100%;
      border-collapse: separate;
      border-spacing: 0;
      margin: 12px 0 16px 0;
      font-size: 9pt;
      background: #ffffff;
      border-radius: 8px;
      overflow: hidden;
      border: 1px solid #cbd5e1;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
    }
    .styled-table thead th {
      background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      font-weight: 700;
      text-transform: uppercase;
      font-size: 8pt;
      letter-spacing: 0.5px;
      padding: 9px 12px;
      border: none;
      text-align: left;
    }
    .styled-table tbody td {
      padding: 8px 12px;
      border-bottom: 1px solid #e2e8f0;
      border-right: 1px solid #f1f5f9;
      color: #1e293b;
      vertical-align: top;
      line-height: 1.45;
    }
    .styled-table tbody tr:last-child td {
      border-bottom: none;
    }
    .styled-table tbody tr:nth-child(even) {
      background-color: #f8fafc;
    }
    .styled-table tbody tr:hover {
      background-color: #f1f5f9;
    }

    /* ==========================================================================
       BADGES & ACTOR PILLS
       ========================================================================== */
    .badge-actor {
      display: inline-flex;
      align-items: center;
      gap: 4px;
      padding: 2px 8px;
      border-radius: 12px;
      font-size: 7.5pt;
      font-weight: 700;
      letter-spacing: 0.3px;
      text-transform: uppercase;
    }
    .badge-operator {
      background: #e0f2fe;
      color: #0369a1;
      border: 1px solid #7dd3fc;
    }
    .badge-system {
      background: #f1f5f9;
      color: #334155;
      border: 1px solid #cbd5e1;
    }
    .badge-faculty {
      background: #fef3c7;
      color: #92400e;
      border: 1px solid #fcd34d;
    }
    .badge-hod {
      background: #f3e8ff;
      color: #6b21a8;
      border: 1px solid #d8b4fe;
    }
    .badge-auditor {
      background: #ecfdf5;
      color: #047857;
      border: 1px solid #6ee7b7;
    }

    .badge-status {
      display: inline-block;
      padding: 2px 7px;
      font-size: 8pt;
      font-weight: 700;
      border-radius: 4px;
    }
    .status-pass {
      background: #dcfce7;
      color: #15803d;
      border: 1px solid #86efac;
    }
    .status-alert {
      background: #fee2e2;
      color: #b91c1c;
      border: 1px solid #fca5a5;
    }
    .status-warn {
      background: #fef3c7;
      color: #b45309;
      border: 1px solid #fde047;
    }

    /* ==========================================================================
       DIAGRAM & NOTATION CONTAINERS
       ========================================================================== */
    .diagram-box {
      text-align: center;
      margin: 8px 0 12px 0;
      padding: 6px;
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-radius: 6px;
    }
    .diagram-box img {
      display: inline-block;
      margin: 0 auto;
    }

    .flow-box {
      border: 1px solid #cbd5e1;
      border-radius: 8px;
      padding: 8px;
      background: #ffffff;
      margin: 8px 0 12px 0;
      text-align: center;
      box-shadow: 0 1px 3px rgba(0,0,0,0.04);
    }
    .flow-box img {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .interactive-link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      margin: 6px 0;
      font-size: 9.5pt;
      color: #0284c7;
      text-decoration: none;
      font-weight: bold;
      border: 1px solid #0284c7;
      padding: 6px 14px;
      border-radius: 6px;
      background: #f0f9ff;
      transition: all 0.2s;
    }
    .interactive-link:hover {
      background: #0284c7;
      color: #ffffff;
    }

    /* ==========================================================================
       THE 19 IDENTIFIED ACTIVITIES — STRUCTURED PHASE CARDS
       ========================================================================== */
    .phase-banner {
      background: linear-gradient(90deg, #0f172a 0%, #1e293b 100%);
      color: #ffffff;
      padding: 6px 12px;
      border-radius: 6px;
      font-size: 9pt;
      font-weight: 700;
      letter-spacing: 0.3px;
      margin: 10px 0 8px 0;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }
    .phase-banner span.phase-tag {
      background: rgba(56, 189, 248, 0.2);
      color: #38bdf8;
      padding: 1px 8px;
      border-radius: 4px;
      font-size: 8pt;
      font-family: 'Fira Code', monospace;
    }

    .activity-card {
      background: #ffffff;
      border: 1px solid #e2e8f0;
      border-left: 3.5px solid #0284c7;
      border-radius: 6px;
      padding: 8px 12px;
      margin-bottom: 7px;
      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.03);
      transition: border-color 0.15s, box-shadow 0.15s;
    }
    .activity-card:hover {
      border-color: #0284c7;
      box-shadow: 0 2px 6px rgba(2, 132, 199, 0.12);
    }
    .activity-header {
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 4px;
    }
    .act-left {
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .act-pill {
      font-family: 'Fira Code', monospace;
      font-size: 8pt;
      font-weight: 700;
      color: #ffffff;
      background: #0284c7;
      padding: 1px 6px;
      border-radius: 4px;
    }
    .act-title {
      font-weight: 700;
      font-size: 9.5pt;
      color: #0f172a;
    }
    .act-desc {
      font-size: 9pt;
      color: #334155;
      line-height: 1.4;
      margin-bottom: 5px;
    }
    .act-subgrid {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 6px;
      background: #f8fafc;
      padding: 5px 8px;
      border-radius: 4px;
      font-size: 8.5pt;
      border: 1px solid #e2e8f0;
      margin-left: 4px;
    }
    .act-item {
      display: flex;
      align-items: flex-start;
      gap: 5px;
      color: #475569;
    }
    .act-label {
      font-weight: 700;
      color: #0f172a;
      min-width: 65px;
    }

    /* Credit Settlement Parameter Cards */
    .credit-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
      margin: 10px 0 12px 0;
    }
    .credit-card {
      background: #f8fafc;
      border: 1px solid #cbd5e1;
      border-top: 3px solid #0284c7;
      border-radius: 6px;
      padding: 8px;
      text-align: center;
    }
    .credit-card .title {
      font-size: 8.5pt;
      font-weight: 700;
      color: #1e293b;
      margin-bottom: 4px;
    }
    .credit-card .formula {
      font-family: 'Fira Code', monospace;
      font-size: 8pt;
      color: #0369a1;
      font-weight: 600;
      background: #e0f2fe;
      padding: 2px 4px;
      border-radius: 4px;
      display: inline-block;
      margin-bottom: 4px;
    }
    .credit-card .desc {
      font-size: 8pt;
      color: #64748b;
      line-height: 1.35;
    }
  </style>
</head>
<body>
  <div class="container" contenteditable="true">
    
    <!-- ==========================================================================
         PAGE 1: COVER, AIM, OBJECTIVES & TOKEN FLOW MECHANICS (NO DENSE MATH)
         ========================================================================== -->
    <div class="page">
      <table class="cover-table">
        <tr>
          <td class="logo-container">
            <img src="pccoelogo.jfif" alt="PCCOE Logo" contenteditable="false">
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
        <li>To represent the flow of activities and decisions from initial cleanup mission proposal to successful 14-week patrol completion, plastic recycling verification, and eco-credit disbursement.</li>
        <li>To model the distinct organizational and computational responsibilities of system stakeholders using structured <strong>Swimlanes (Activity Partitions)</strong>.</li>
        <li>To model the complete patrol lifecycle, including automated pre-audit diagnostics, external recycling compliance review, faculty mentor supervision, harbor director departure clearance, weekly telemetry logging, and final dockside weighbridge audits.</li>
        <li>To systematically represent alternative exception flows, including invalid authentication tokens, rejected mission proposals, flagged marine reserve hazards, and iterative document correction loops.</li>
      </ol>

      <h2>Theoretical Overview of UML 2.0 Activity Diagrams</h2>
      <p>An <strong>Activity Diagram</strong> is a behavioral modeling diagram standardized by the Object Management Group (OMG) within UML 2.0. It visually represents the stepwise, dynamic flow of operational control and computational actions within a complex system. Unlike state machines that model the internal states of a single object over time, activity diagrams model the cross-functional coordination, concurrency, conditional branching, and data flow across distributed software tiers and human actors.</p>

      <h2>Token Flow Execution Semantics in UML 2.0</h2>
      <p>In UML 2.0, workflows execute via a discrete <strong>token flow mechanism</strong> rather than ad-hoc state jumping. This formal execution foundation governs how control traverses through nodes:</p>
      
      <ul>
        <li><strong>Token Initiation:</strong> The workflow begins when a single control token is placed at the Initial Node upon process start. This token traverses outgoing directed control edges toward target action nodes.</li>
        <li><strong>Action Firing &amp; Consumption:</strong> An action node is enabled to execute only when all required incoming control and data tokens arrive on its input edges. Upon completing its atomic task, the action consumes the incoming tokens and emits new control tokens on each outgoing flow edge.</li>
        <li><strong>Deterministic Decision Branching:</strong> At a decision node, mutually exclusive guard conditions (e.g., <code>[Approved]</code> vs <code>[Rejected]</code>) are evaluated sequentially. Exactly one guard evaluates to true, directing the token along the chosen path without ambiguity or duplication.</li>
        <li><strong>Fork &amp; Join Concurrency:</strong> A Fork node duplicates an incoming token across multiple concurrent paths to execute tasks in parallel (e.g., propulsion spin-up and sensor calibration). A Join node synchronizes parallel paths by halting execution until every incoming concurrent path delivers its token.</li>
      </ul>

      <div class="info-box blue">
        <strong>Architectural Principle:</strong> The token flow semantics ensure that the OceanCleanFlow system operates in a deterministic, deadlock-free manner during distributed marine operations, multi-tier approvals, and weekly iterative telemetry logging.
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
        <img src="notation_initial.svg" alt="Initial Node Diagram" style="max-height: 105px;">
      </div>

      <h3>2. Action / Activity Node</h3>
      <p>An action represents an atomic, non-interruptible operational step or computational task performed by an actor or automated software service. It is rendered as a rectangle with smoothly rounded corners. Typical actions in OceanCleanFlow include <em>Login to Portal</em>, <em>Submit Mission Request</em>, <em>Perform Pre-Audit Checks</em>, and <em>Calculate Eco-Credits</em>.</p>
      <div class="diagram-box">
        <img src="notation_action.svg" alt="Action Node Diagram" style="max-height: 105px;">
      </div>

      <h3>3. Control Flow</h3>
      <p>Control flow lines depict the sequential ordering and direction of activity execution. They are drawn as solid directed lines with an open arrowhead pointing from the source node to the target node. For example: <code>Login → Verify Login Details → Submit Mission Request → Upload Documents</code>.</p>
      <div class="diagram-box">
        <img src="notation_control_flow.svg" alt="Control Flow Diagram" style="max-height: 105px;">
      </div>

      <h3>4. Decision Node</h3>
      <p>A decision node routes workflow execution along alternative paths based on the evaluation of conditional guard expressions. It is represented by a diamond shape with a single incoming control flow and two or more outgoing flows labeled with mutually exclusive guard conditions (e.g., <code>[Valid]</code> / <code>[Invalid]</code> or <code>[Approved]</code> / <code>[Rejected]</code>).</p>
      <div class="diagram-box">
        <img src="notation_decision.svg" alt="Decision Node Diagram" style="max-height: 110px;">
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 3: MAIN ELEMENTS CONTINUED (ITEMS 5-9)
         ========================================================================== -->
    <div class="page">
      <h2>Main Elements of an Activity Diagram (Contd.)</h2>

      <h3>5. Merge Node</h3>
      <p>A merge node consolidates multiple alternative incoming control paths into a single outgoing flow without requiring synchronization. It is depicted as a diamond shape with multiple incoming flows and one outgoing flow. In OceanCleanFlow, merge nodes allow operators to correct rejected proposals and cleanly re-enter the verification stream.</p>
      <div class="diagram-box">
        <img src="notation_merge.svg" alt="Merge Node Diagram" style="max-height: 110px;">
      </div>

      <h3>6. Fork Node</h3>
      <p>A fork node divides a single incoming control flow into two or more concurrent, parallel execution paths. It is represented by a thick solid horizontal or vertical coordination bar. In OceanCleanFlow, a fork is used during vessel pre-launch diagnostics to trigger concurrent propulsion spin-up, sensor telemetry calibration, and satellite synchronization.</p>
      <div class="diagram-box">
        <img src="notation_fork.svg" alt="Fork Node Diagram" style="max-height: 115px;">
      </div>

      <h3>7. Join Node</h3>
      <p>A join node synchronizes multiple concurrent incoming parallel paths into a single unified control flow. It is represented by a thick solid coordination bar. Control halts at the join bar until all incoming concurrent paths have completed execution and delivered their tokens.</p>
      <div class="diagram-box">
        <img src="notation_join.svg" alt="Join Node Diagram" style="max-height: 115px;">
      </div>

      <h3>8. Swimlanes (Activity Partitions)</h3>
      <p>Swimlanes partition the activity diagram according to the organizational, departmental, or architectural responsibilities of participants. Each action is positioned strictly inside the vertical column of the actor or system tier responsible for its execution (e.g., Operator, Autonomous System, Faculty Mentor, Harbor HOD).</p>
      <div class="diagram-box">
        <img src="notation_swimlanes.svg" alt="Swimlanes Diagram" style="max-height: 115px; width: auto;">
      </div>

      <h3>9. Activity Final Node</h3>
      <p>The activity final node indicates the complete termination of the entire workflow. It is represented by a bullseye circle containing a solid filled black circle. In OceanCleanFlow, execution terminates when all 14 patrol weeks are audited, plastic tonnage is verified, eco-credits are minted, and operator debriefing feedback is submitted.</p>
      <div class="diagram-box">
        <img src="notation_final.svg" alt="Activity Final Node Diagram" style="max-height: 100px;">
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 4: SWIMLANE RESPONSIBILITIES & CROSS-FUNCTIONAL MATRIX
         ========================================================================== -->
    <div class="page">
      <h2>Swimlane Partitions &amp; Architectural Responsibilities</h2>
      <p>Swimlanes establish clear architectural boundaries of responsibility across the four core stakeholders involved in the ocean cleanup lifecycle. By separating concerns into dedicated partitions, the system ensures zero ambiguity regarding which entity originates data, executes decisions, or signs off on deliverables.</p>

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
              Initiates mission proposals, inputs vessel technical specifications, uploads compliance documentation, submits weekly patrol records, and uploads dockside weighbridge receipts.
            </td>
            <td>
              <code>ACT-01</code> Login to Portal<br>
              <code>ACT-02</code> Submit Mission Request<br>
              <code>ACT-03</code> Submit Vessel Details<br>
              <code>ACT-04</code> Upload Documents<br>
              <code>ACT-13</code> Submit Weekly Logs<br>
              <code>ACT-15</code> Upload Manifest &amp; Receipts<br>
              <code>ACT-19</code> Submit Feedback
            </td>
          </tr>
          <tr>
            <td>
              <strong>2. OceanCleanFlow System</strong><br>
              <span class="badge-actor badge-system">Autonomous Backend</span>
            </td>
            <td>
              Validates cryptographic credentials, executes automated sensor pre-audits, coordinates external auditor verification tokens, increments 14-week patrol timer, and calculates eco-credits.
            </td>
            <td>
              <code>ACT-05</code> Verify Login Tokens<br>
              <code>ACT-06</code> Perform Pre-Audit Checks<br>
              <code>ACT-10</code> Forward to Harbor HOD<br>
              <code>ACT-17</code> Mark Mission Completed<br>
              <code>ACT-18</code> Calculate Eco-Credits
            </td>
          </tr>
          <tr>
            <td>
              <strong>3. Faculty Mentor</strong><br>
              <span class="badge-actor badge-faculty">Academic Supervisor</span>
            </td>
            <td>
              Reviews mission route feasibility, assesses flagged environmental hazards, endorses or rejects requests with corrective remarks, audits weekly logs, and inspects final recycling receipts.
            </td>
            <td>
              <code>ACT-08</code> Review Mission Proposal<br>
              <code>ACT-09</code> Approve or Reject Request<br>
              <code>ACT-14</code> Audit Weekly Patrol Logs<br>
              <code>ACT-16</code> Verify Completion Manifest
            </td>
          </tr>
          <tr>
            <td>
              <strong>4. Harbor Director (HOD)</strong><br>
              <span class="badge-actor badge-hod">Station Chief</span>
            </td>
            <td>
              Exercises institutional authority over harbor slipway departures, manages berth scheduling, verifies navigation channel safety, and issues official maritime clearance certificates.
            </td>
            <td>
              <code>ACT-11</code> Final Harbor Departure Clearance or Formal Institutional Rejection
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
            <td>System &rarr; Faculty Mentor</td>
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
            <td>Operator &rarr; Faculty Mentor</td>
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
         PAGE 5: THE 19 IDENTIFIED ACTIVITIES — PART 1 (PHASES 1 TO 3)
         ========================================================================== -->
    <div class="page">
      <h2>The 19 Identified System Activities (Phases 1 to 3)</h2>
      <p>The OceanCleanFlow system workflow is formalized into 19 discrete atomic activities. Each activity features defined trigger preconditions, operational behavior, and deliverable state postconditions:</p>

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
            <span class="act-title">Submit Mission Request</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator initiates a new ocean cleanup patrol proposal for a designated marine sector and selects target mission profile.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Authenticated user session; mission intake form.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Mission record created with status <code>DRAFT_PROPOSAL</code>.</div>
        </div>
      </div>

      <!-- ACT 03 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-03</span>
            <span class="act-title">Submit Vessel &amp; Sector Details</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator specifies vessel hull classification, battery reserve, trash payload limits, and GPS patrol boundary coordinates.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Technical parameters, polygon coordinates, load specs.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Vessel specification manifest attached to proposal.</div>
        </div>
      </div>

      <!-- ACT 04 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-04</span>
            <span class="act-title">Upload Mission Documents</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator uploads mandatory compliance files: vessel seaworthiness certificate, hull insurance policy, and safety checklist.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> PDF compliance certificates, signed indemnity bond.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Document attachments hashed and linked to proposal dossier.</div>
        </div>
      </div>

      <!-- PHASE 2 -->
      <div class="phase-banner">
        <span>PHASE 2: AUTOMATED PRE-AUDIT &amp; EXTERNAL COMPLIANCE</span>
        <span class="phase-tag">ACTIVITIES 05 &ndash; 07</span>
      </div>

      <!-- ACT 05 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-05</span>
            <span class="act-title">Verify Login Details</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System validates operator credentials against user directory. If invalid, displays error and returns to login merge node.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Cryptographic hash from ACT-01.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> JWT session token granted [Valid] or error thrown [Invalid].</div>
        </div>
      </div>

      <!-- ACT 06 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-06</span>
            <span class="act-title">Perform Pre-Audit Checks</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System runs automated static diagnostics on vessel specs, verifies file extensions, and checks power-to-weight safety limits.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Submitted specs and uploaded PDF attachments.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Pre-audit diagnostic report generated; error flags route to retry.</div>
        </div>
      </div>

      <!-- ACT 07 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-07</span>
            <span class="act-title">Verify Environmental Compliance</span>
          </div>
          <span class="badge-actor badge-auditor">External Auditor</span>
        </div>
        <div class="act-desc">External recycling auditor accesses proposal via one-time secure token to verify facility recycling licensing and sanctuary proximity.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Audit dispatch link, GPS coordinates, recycling partner ID.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Auditor compliance signoff; hazard flags appended if near reef.</div>
        </div>
      </div>

      <!-- PHASE 3 -->
      <div class="phase-banner">
        <span>PHASE 3: ACADEMIC &amp; HARBOR INSTITUTIONAL APPROVAL</span>
        <span class="phase-tag">ACTIVITIES 08 &ndash; 11</span>
      </div>

      <!-- ACT 08 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-08</span>
            <span class="act-title">Review Mission Request</span>
          </div>
          <span class="badge-actor badge-faculty">Faculty Mentor</span>
        </div>
        <div class="act-desc">Faculty mentor reviews proposal dossier, route feasibility, student learning objectives, and environmental flags.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Audit-cleared proposal dossier and environmental report.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Faculty assessment rubric completed with mentor notes.</div>
        </div>
      </div>

      <!-- ACT 09 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-09</span>
            <span class="act-title">Approve or Reject Request</span>
          </div>
          <span class="badge-actor badge-faculty">Faculty Mentor</span>
        </div>
        <div class="act-desc">Faculty mentor issues formal decision: endorses proposal or rejects with actionable corrective feedback for the student.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Completed assessment rubric from ACT-08.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Endorsement seal granted [Approved] or rejection remarks logged [Rejected].</div>
        </div>
      </div>

      <!-- ACT 10 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-10</span>
            <span class="act-title">Forward Request to Harbor HOD</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System elevates faculty-endorsed proposal to the Harbor Operations Director queue and sends executive authorization alert.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Faculty approval token from ACT-09.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Status set to <code>PENDING_HARBOR_CLEARANCE</code>; alert dispatched.</div>
        </div>
      </div>

      <!-- ACT 11 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-11</span>
            <span class="act-title">Final Harbor Approval or Rejection</span>
          </div>
          <span class="badge-actor badge-hod">Harbor Director (HOD)</span>
        </div>
        <div class="act-desc">Harbor Director evaluates port traffic, weather radar, and berth allocation, issuing final legal departure authorization.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Executive clearance packet from ACT-10.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Maritime departure clearance granted [Approved] or denied [Rejected].</div>
        </div>
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 6: THE 19 IDENTIFIED ACTIVITIES — PART 2 (PHASES 4 & 5)
         ========================================================================== -->
    <div class="page">
      <h2>The 19 Identified System Activities (Phases 4 &amp; 5)</h2>
      <p>The operational and post-patrol phases govern active sea deployment, iterative 14-week telemetry logging, dockside recycling audits, and incentive settlement:</p>

      <!-- PHASE 4 -->
      <div class="phase-banner">
        <span>PHASE 4: AUTONOMOUS DEPLOYMENT &amp; 14-WEEK PATROL LOOP</span>
        <span class="phase-tag">ACTIVITIES 12 &ndash; 14</span>
      </div>

      <!-- ACT 12 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-12</span>
            <span class="act-title">Start Ocean Cleanup Mission</span>
          </div>
          <span class="badge-actor badge-operator">Operator &amp; Vessel</span>
        </div>
        <div class="act-desc">Vessel propulsion activates, autopilot disengages slipway moorings, and the autonomous boat commences marine cleanup patrol.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Authorized departure clearance from ACT-11.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Mission state transitions to <code>IN_PATROL</code>; week counter initialized to 1.</div>
        </div>
      </div>

      <!-- ACT 13 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-13</span>
            <span class="act-title">Submit Weekly Patrol Log</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator submits weekly telemetry log: kilograms of plastic recovered, battery degradation curves, and zero-bycatch sensor logs.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> 7-day patrol telemetry packet; weekly milestone prompt.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Weekly progress report submitted for academic review.</div>
        </div>
      </div>

      <!-- ACT 14 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-14</span>
            <span class="act-title">Review Weekly Patrol Log</span>
          </div>
          <span class="badge-actor badge-faculty">Faculty Mentor</span>
        </div>
        <div class="act-desc">Faculty mentor reviews debris volume, checks wildlife safety pings, logs operational remarks, and endorses week completion.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Submitted weekly log from ACT-13.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Log signed off; system evaluates loop condition <code>[Week &lt; 14]</code> vs <code>[Week &ge; 14]</code>.</div>
        </div>
      </div>

      <!-- PHASE 5 -->
      <div class="phase-banner">
        <span>PHASE 5: DOCKING, RECYCLING AUDIT &amp; ECO-CREDIT SETTLEMENT</span>
        <span class="phase-tag">ACTIVITIES 15 &ndash; 19</span>
      </div>

      <!-- ACT 15 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-15</span>
            <span class="act-title">Upload Completion Documents</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Upon completing 14 weeks, vessel returns to harbor. Operator uploads weighbridge weight slips and polymer category sorting manifests.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Harbor dock receipts, weighbridge weight certificates.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Offload completion dossier uploaded for faculty audit.</div>
        </div>
      </div>

      <!-- ACT 16 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-16</span>
            <span class="act-title">Verify Completion Documents</span>
          </div>
          <span class="badge-actor badge-faculty">Faculty Mentor</span>
        </div>
        <div class="act-desc">Faculty mentor audits physical weighbridge certificates against vessel onboard bin load-cell telemetry to ensure zero mass discrepancy.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Completion dossier from ACT-15.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Verified mass balance certificate issued [Approved] or rework ordered [Rejected].</div>
        </div>
      </div>

      <!-- ACT 17 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-17</span>
            <span class="act-title">Mark Mission Completed</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System transitions mission lifecycle state to <code>COMPLETED</code> and permanently locks telemetry logs against further modification.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Mentor completion verification token from ACT-16.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Database state set to <code>COMPLETED</code>; triggers credit settlement.</div>
        </div>
      </div>

      <!-- ACT 18 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-18</span>
            <span class="act-title">Calculate Eco-Credits</span>
          </div>
          <span class="badge-actor badge-system">Autonomous System</span>
        </div>
        <div class="act-desc">System algorithmically calculates total earned eco-credits and academic credits based on verified plastic mass and safety factors.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Verified plastic tonnage, zone index, compliance record.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Eco-credits minted and deposited into student digital profile.</div>
        </div>
      </div>

      <!-- ACT 19 -->
      <div class="activity-card">
        <div class="activity-header">
          <div class="act-left">
            <span class="act-pill">ACT-19</span>
            <span class="act-title">Submit Final Feedback</span>
          </div>
          <span class="badge-actor badge-operator">Operator / Student</span>
        </div>
        <div class="act-desc">Operator completes comprehensive debriefing survey evaluating vessel navigation, battery endurance, and system UX.</div>
        <div class="act-subgrid">
          <div class="act-item"><span class="act-label">Trigger / Input:</span> Debriefing questionnaire; credit receipt confirmation.</div>
          <div class="act-item"><span class="act-label">Output / State:</span> Survey archived; control token delivered to Activity Final Node.</div>
        </div>
      </div>

      <div class="info-box green" style="margin-top: 8px;">
        <strong>Process Completeness:</strong> All 19 activities form a continuous, non-blocking workflow from initial operator authentication through the 14-week patrol loop to final eco-credit disbursement.
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 7: STEP-BY-STEP ACTIVITY FLOWS (6.1 TO 6.3)
         ========================================================================== -->
    <div class="page">
      <h2>Step-by-Step Activity Flows (Phases 6.1 to 6.3)</h2>

      <h3>6.1 Operator Login and Mission Application</h3>
      <p>The workflow initiates when the operator accesses the portal. The system evaluates login tokens at a decision node. If invalid, an error memo routes control back to the login merge node. Upon valid authentication, the operator submits mission parameters, configures vessel load limits, and uploads seaworthiness compliance documents.</p>
      
      <div class="flow-box">
        <img src="flow_6_1_login.svg" alt="Activity Flow 6.1: Login & Application">
      </div>

      <h3>6.2 Pre-Audit Checks and External Auditor Verification</h3>
      <p>Upon proposal submission, the system executes automated pre-audit diagnostics on telemetry schemas and file signatures. If rejected, the operator is prompted to correct files. If valid, an automated time-locked token is dispatched to the External Recycling Auditor, who reviews environmental compliance and sanctuary clearance before forwarding.</p>

      <div class="flow-box">
        <img src="flow_6_2_preaudit.svg" alt="Activity Flow 6.2: Pre-Audit & Auditor Verification">
      </div>

      <h3>6.3 Faculty Mentor and HOD Institutional Approval</h3>
      <p>The Faculty Mentor evaluates mission route safety, proposed patrol sectors, and auditor notes. If rejected, corrective remarks route back for proposal revision. If approved, the system forwards the dossier to the Harbor Operations Director (HOD) for official maritime clearance, which activates the vessel's departure authorization.</p>

      <div class="flow-box">
        <img src="flow_6_3_approval.svg" alt="Activity Flow 6.3: Faculty and HOD Approval Hierarchy">
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 8: STEP-BY-STEP ACTIVITY FLOWS (6.4 & 6.5) & CREDIT SETTLEMENT
         ========================================================================== -->
    <div class="page">
      <h2>Step-by-Step Activity Flows (Phases 6.4 &amp; 6.5)</h2>

      <h3>6.4 Weekly Progress Tracking and 14-Week Patrol Milestone Loop</h3>
      <p>Upon maritime departure clearance, the vessel engages autonomous route navigation. Every 7 days, the student operator compiles and submits an operational telemetry log detailing debris tonnage recovered, battery endurance, and marine wildlife pings. The Faculty Mentor reviews the log. The system evaluates the loop condition: if fewer than 14 weeks have elapsed, the loop iterates; once 14 weeks are satisfied, control transitions to harbor docking.</p>

      <div class="flow-box">
        <img src="flow_6_4_weekly.svg" alt="Activity Flow 6.4: 14-Week Patrol Progress Tracking Loop">
      </div>

      <h3>6.5 Mission Completion, Recycling Verification &amp; Eco-Credit Settlement</h3>
      <p>At the conclusion of the 14-week patrol, the vessel docks at the harbor recycling slipway. The operator uploads certified weighbridge slips and polymer manifests. The Faculty Mentor audits physical slips against onboard bin load-cell logs. Upon verification, the mission is marked completed, eco-credits are calculated, and the operator completes debriefing.</p>

      <div class="flow-box">
        <img src="flow_6_5_completion.svg" alt="Activity Flow 6.5: Mission Completion & Eco-Credit Settlement">
      </div>

      <h2>Automated Eco-Credit &amp; Reward Settlement Logic</h2>
      <p>When the Faculty Mentor verifies dockside offload receipts, the system calculates student eco-credits and academic internship reward points using four core operational metrics:</p>

      <div class="credit-grid">
        <div class="credit-card">
          <div class="title">1. Verified Waste Mass</div>
          <div class="formula">Mass &times; 10 Pts/kg</div>
          <div class="desc">Base credits allocated for every verified kilogram of plastic, chemical, or ghost net debris offloaded.</div>
        </div>
        <div class="credit-card">
          <div class="title">2. Sector Difficulty</div>
          <div class="formula">Multiplier &times; [1.0 &ndash; 1.5]</div>
          <div class="desc">Zone difficulty factor scaled according to maritime currents, open-ocean distance, and debris density.</div>
        </div>
        <div class="credit-card">
          <div class="title">3. Wildlife Safety</div>
          <div class="formula">Safety &times; 100%</div>
          <div class="desc">Zero bycatch compliance bonus; deducted if acoustic deterrent sensors fail to divert marine fauna.</div>
        </div>
        <div class="credit-card">
          <div class="title">4. Punctuality Bonus</div>
          <div class="formula">Bonus: +500 Pts</div>
          <div class="desc">Full compliance incentive awarded for submitting all 14 weekly progress logs without delay.</div>
        </div>
      </div>
    </div>

    <!-- ==========================================================================
         PAGE 9: MASTER UML 2.0 ACTIVITY DIAGRAM VISUALIZATION
         ========================================================================== -->
    <div class="page">
      <h2>Master UML 2.0 Activity Diagram &mdash; Full System View</h2>
      <p>The complete end-to-end activity model unites all four swimlanes, decision nodes, parallel fork/join synchronization, weekly iteration loops, and exception correction paths into a cohesive, non-blocking operational workflow:</p>

      <div style="text-align: center; margin: 8px 0 12px 0;">
        <a href="Activity_Diagram_Assignment_7.html" class="interactive-link" contenteditable="false" target="_blank">
          &#x1F517; Launch Full Screen Pan &amp; Zoom Interactive Canvas (Activity_Diagram_Assignment_7.html)
        </a>
      </div>

      <!-- Completely visible master diagram without scrollbars -->
      <div style="border: 1.5px solid #cbd5e1; border-radius: 8px; background: #ffffff; padding: 6px; box-shadow: 0 2px 8px rgba(0,0,0,0.06); margin-bottom: 8px;">
        <img src="master_activity_diagram.svg" alt="Master UML 2.0 Activity Diagram" style="width: 100%; height: auto; display: block; border-radius: 4px;">
      </div>

      <div style="font-size: 8.5pt; color: #475569; text-align: center; margin-top: 4px;">
        <strong>Figure 7.0:</strong> Complete Multi-Swimlane UML 2.0 Activity Diagram for OceanCleanFlow System.
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
            <td>Request flagged with high priority; diverted to special faculty safety review for route adjustment.</td>
          </tr>
          <tr>
            <td>
              <strong>Faculty / HOD Rejection</strong><br>
              <span class="badge-status status-alert">Rejection</span>
            </td>
            <td>Adverse weather forecast, harbor channel congestion, or unapproved sector.</td>
            <td>System generates formal rejection memo; operator edits sector waypoints and resubmits.</td>
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
            <td>Supervisor requests weighbridge re-calibration or manual bin inspection before credit approval.</td>
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
            <td>Actions and decision diamonds are strictly localized within their designated swimlane column.</td>
          </tr>
          <tr>
            <td><strong>Cyclic Termination</strong></td>
            <td><span class="badge-status status-pass">&#10004; Verified</span></td>
            <td>The 14-week patrol loop is governed by an incrementing counter ensuring deterministic exit.</td>
          </tr>
        </tbody>
      </table>

      <h2>Conclusion</h2>
      <p>Through this assignment, we successfully architected, modeled, and verified a comprehensive <strong>UML 2.0 Activity Diagram</strong> with four structured swimlanes for the <strong>OceanCleanFlow &ndash; Department Marine Cleanup Management System</strong>. The model captures the complete operational lifecycle from initial operator authentication, proposal submission, and automated pre-audit diagnostics, through external environmental compliance review, faculty mentor supervision, and institutional HOD harbor clearance. Furthermore, the 14-week iterative patrol tracking loop, dockside weighbridge verification, algorithmic eco-credit settlement, and exception recovery paths were thoroughly formalized. This delivers a robust, unambiguous behavioral blueprint for engineering the platform's backend workflow and autonomous marine vessel operations.</p>

      <h3 style="margin-top: 18px;">Signatures and Verification</h3>
      <table style="width: 100%; margin-top: 25px; border-collapse: collapse; font-family: 'Plus Jakarta Sans', Arial, sans-serif;">
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

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully generated updated Assignment_7.html ({len(html_content)} bytes)")
