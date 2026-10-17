import os

output_path = r"c:\Users\adity\Desktop\Subjects\SEML\Assignment - 7\Assignment_7.html"

# We use r""" ... """ so backslashes for LaTeX MathJax are 100% preserved!
html_content = r"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>SEML Assignment 7 - UML 2.0 Activity Diagram for OceanCleanFlow</title>
  <script>
    window.MathJax = {
      tex: {
        inlineMath: [['\\(', '\\)']],
        displayMath: [['\\[', '\\]']]
      }
    };
  </script>
  <script id="MathJax-script" async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
  <style>
    /* Screen CSS (The "Preview") */
    body {
      font-family: Arial, sans-serif;
      font-size: 11pt;
      line-height: 1.45;
      color: #000;
      background: #e5e7eb;
      padding: 20px;
      margin: 0;
    }

    .container {
      max-width: 8.5in;
      margin: 0 auto;
    }

    .page {
      min-height: 11in;
      width: 8.5in;
      padding: 0.7in 0.8in;
      background: #ffffff;
      margin: 0 auto 20px auto;
      box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
      position: relative;
      box-sizing: border-box;
    }

    .page:focus-within {
      outline: 2px dashed #4299e1;
    }

    /* Print CSS */
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
        padding: 0.25in 0.3in;
        box-shadow: none;
        border: none;
        page-break-after: always;
      }
    }

    /* Cover Table CSS */
    .cover-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 18px;
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
      font-size: 13pt;
    }
    .logo-container {
      text-align: center;
      width: 18%;
      padding: 5px !important;
    }
    .logo-container img {
      max-width: 95px;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    /* Typography */
    h2 {
      font-family: Arial, sans-serif;
      font-size: 15pt;
      color: #000;
      margin-top: 16px;
      margin-bottom: 8px;
      border-bottom: 1.5px solid #334155;
      padding-bottom: 3px;
    }
    h3 {
      font-family: Arial, sans-serif;
      font-size: 12pt;
      color: #0f172a;
      margin-top: 12px;
      margin-bottom: 5px;
    }
    h4 {
      font-family: Arial, sans-serif;
      font-size: 10.5pt;
      color: #1e293b;
      margin-top: 10px;
      margin-bottom: 4px;
    }
    p {
      font-family: Arial, sans-serif;
      font-size: 10pt;
      text-align: justify;
      line-height: 1.45;
      margin-bottom: 8px;
    }
    ul, ol {
      margin-left: 20px;
      font-size: 10pt;
      margin-bottom: 8px;
      line-height: 1.45;
    }
    li {
      margin-bottom: 3px;
    }

    /* Styled Tables */
    .styled-table {
      width: 100%;
      border-collapse: collapse;
      margin: 10px 0;
      font-size: 9.5pt;
    }
    .styled-table th, .styled-table td {
      border: 1px solid #000;
      padding: 5px 8px;
      text-align: left;
    }
    .styled-table th {
      background-color: #f2f2f2;
      font-weight: bold;
    }

    /* Centered Diagram Boxes (Standard Textbook Layout) */
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

    /* Flow Diagram Box */
    .flow-box {
      border: 1px solid #cbd5e1;
      border-radius: 6px;
      padding: 6px;
      background: #ffffff;
      margin: 8px 0 12px 0;
      text-align: center;
    }
    .flow-box img {
      max-width: 100%;
      height: auto;
      display: block;
      margin: 0 auto;
    }

    .interactive-link {
      display: inline-block;
      margin: 6px 0;
      font-size: 10pt;
      color: #0284c7;
      text-decoration: none;
      font-weight: bold;
      border: 1px solid #0284c7;
      padding: 5px 12px;
      border-radius: 4px;
      background: #f0f9ff;
    }
    .interactive-link:hover {
      background: #e0f2fe;
    }

    .badge {
      display: inline-block;
      padding: 2px 6px;
      font-size: 8.5pt;
      font-weight: bold;
      border-radius: 3px;
      background-color: #e2e8f0;
      color: #334155;
    }
  </style>
</head>
<body>
  <div class="container" contenteditable="true">
    
    <!-- ==================== PAGE 1: COVER & INTRODUCTION ==================== -->
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
        <li>To identify the major activities involved in the student/operator marine internship application, mission parameter submission, and multi-tier approval process.</li>
        <li>To represent the flow of activities and decisions from initial cleanup mission request submission to successful mission completion, plastic recycling, and credit disbursement.</li>
        <li>To model the distinct organizational and computational responsibilities of participants using structured <strong>Swimlanes (Activity Partitions)</strong>.</li>
        <li>To model the comprehensive 14-week internship and patrol lifecycle, including document verification, external recycling auditor verification, faculty mentor review, HOD institutional authorization, weekly progress tracking, completion audits, and credit calculation.</li>
        <li>To systematically represent alternative flows, including invalid documents, rejected mission requests, flagged environmental hazards, and requests requiring iterative corrections.</li>
      </ol>

      <h2>Theoretical Overview of UML 2.0 Activity Diagrams</h2>
      <p>An <strong>Activity Diagram</strong> is a behavioral diagram specified in the Unified Modeling Language (UML) standard that visually describes the dynamic, step-by-step workflow of operational and computational processes. It maps the sequence of atomic actions, conditional decision branches, concurrent execution paths, and control transitions within a complex system.</p>
      
      <p>In modern software engineering, activity diagrams function as formal, object-oriented process flowcharts. For the <strong>OceanCleanFlow</strong> platform, the activity flow begins when an operator/student logs in and submits an ocean cleanup mission proposal with designated GPS sectors and vessel configurations. The system performs automated pre-audit diagnostics, followed by external recycling auditor verification, faculty mentor assessment, and final departmental HOD authorization. Once deployed, the system tracks the 14-week patrol cycle, verifies weekly logs, handles container offloading at harbor docks, computes earned eco-credits, and collects operational feedback.</p>

      <h3>Mathematical Petri-Net Token Transition Semantics</h3>
      <p>UML 2.0 Activity models adhere to formal Petri-net firing semantics. An activity node \(A\) executes if and only if all incoming control edges \(E_{\text{in}}\) hold valid tokens condition \(T_c\):</p>
      \[
      T_c = \bigwedge_{e \in E_{\text{in}}} \text{TokenPresent}(e) \implies \text{FireAction}(A) \implies \forall e' \in E_{\text{out}}, \text{EmitToken}(e')
      \]
      <p>For Decision nodes, control routing is governed by mutually exclusive, exhaustive boolean guard predicates:</p>
      \[
      \sum_{i=1}^{n} P(\text{Guard}_i) = 1 \quad \text{where} \quad \text{Guard}_j \cap \text{Guard}_k = \emptyset \quad (\forall j \neq k)
      \]
    </div>

    <!-- ==================== PAGE 2: MAIN ELEMENTS OF ACTIVITY DIAGRAM (ITEMS 1-4) ==================== -->
    <div class="page">
      <h2>Main Elements of an Activity Diagram</h2>
      <p>UML 2.0 standardizes graphical symbols to describe system dynamics, data transformations, and decision paths without ambiguity. Below are the primary atomic notations:</p>

      <h3>1. Initial Node</h3>
      <p>The initial node represents the starting point of the workflow. It is graphically denoted as a solid black circle (⚫). An activity diagram can have only one primary initial node per structured control flow. In OceanCleanFlow, the process starts when the student/operator begins the mission application process.</p>
      <div class="diagram-box">
        <img src="notation_initial.svg" alt="Initial Node Diagram" style="max-height: 105px;">
      </div>

      <h3>2. Action / Activity Node</h3>
      <p>An action represents an atomic, non-interruptible step or computational task performed by a user or software service. It is represented by a rectangle with rounded corners. Examples in OceanCleanFlow include <em>Login to OceanCleanFlow</em>, <em>Submit Mission Request</em>, <em>Upload Mission Documents</em>, and <em>Calculate Credits</em>.</p>
      <div class="diagram-box">
        <img src="notation_action.svg" alt="Action Node Diagram" style="max-height: 105px;">
      </div>

      <h3>3. Control Flow</h3>
      <p>Control flow represents the sequence and direction of activities. It is rendered as a directed line with an open arrowhead pointing from the source activity to the target activity. For example: <code>Login → Verify Login Details → Submit Mission Request → Upload Documents</code>.</p>
      <div class="diagram-box">
        <img src="notation_control_flow.svg" alt="Control Flow Diagram" style="max-height: 105px;">
      </div>

      <h3>4. Decision Node</h3>
      <p>A decision node routes workflow execution based on evaluated conditions. It is represented by a diamond shape with one incoming flow and two or more outgoing flows labeled with mutually exclusive guard conditions (e.g., <code>[Yes]</code> / <code>[No]</code> or <code>[Valid]</code> / <code>[Invalid]</code>).</p>
      <div class="diagram-box">
        <img src="notation_decision.svg" alt="Decision Node Diagram" style="max-height: 110px;">
      </div>
    </div>

    <!-- ==================== PAGE 3: MAIN ELEMENTS CONTINUED (ITEMS 5-9) ==================== -->
    <div class="page">
      <h2>Main Elements of an Activity Diagram (Contd.)</h2>

      <h3>5. Merge Node</h3>
      <p>A merge node unifies multiple alternative incoming control paths into a single outgoing flow without requiring synchronization. It is depicted as a diamond shape with multiple incoming arrows and one outgoing arrow. In OceanCleanFlow, merge nodes are used when an operator corrects and resubmits rejected documents, cleanly re-joining the verification stream.</p>
      <div class="diagram-box">
        <img src="notation_merge.svg" alt="Merge Node Diagram" style="max-height: 110px;">
      </div>

      <h3>6. Fork</h3>
      <p>A fork divides one incoming flow into two or more parallel concurrent activities. It is represented by a thick horizontal or vertical bar. In OceanCleanFlow, a fork is used during vessel pre-launch diagnostics to trigger concurrent propulsion spin-up, sensor calibration, and satellite telemetry synchronization.</p>
      <div class="diagram-box">
        <img src="notation_fork.svg" alt="Fork Node Diagram" style="max-height: 120px;">
      </div>

      <h3>7. Join</h3>
      <p>A join combines two or more concurrent parallel activities into a single synchronized flow. It is represented by a thick horizontal or vertical bar. Control halts at the join bar until all incoming concurrent branches have finished execution and delivered their tokens.</p>
      <div class="diagram-box">
        <img src="notation_join.svg" alt="Join Node Diagram" style="max-height: 120px;">
      </div>

      <h3>8. Swimlanes (Activity Partitions)</h3>
      <p>Swimlanes partition the activity diagram according to the organizational or architectural responsibilities of participants. Each activity is placed strictly inside the column of the actor or system tier responsible for performing it (e.g., Operator, System, Faculty Mentor, HOD).</p>
      <div class="diagram-box">
        <img src="notation_swimlanes.svg" alt="Swimlanes Diagram" style="max-height: 115px; width: auto;">
      </div>

      <h3>9. Activity Final Node</h3>
      <p>The activity final node represents the permanent completion of the workflow. It is represented by a circle containing a smaller filled black circle (bullseye ◉). In OceanCleanFlow, execution terminates when the 14-week mission is verified, credits are minted, and debriefing feedback is submitted.</p>
      <div class="diagram-box">
        <img src="notation_final.svg" alt="Activity Final Node Diagram" style="max-height: 100px;">
      </div>
    </div>

    <!-- ==================== PAGE 4: SWIMLANES & 19 IDENTIFIED ACTIVITIES ==================== -->
    <div class="page">
      <h2>Swimlane Responsibilities &amp; Identified Activities</h2>
      <p>Swimlanes partition the model to establish clear boundaries of responsibility across the four core stakeholders:</p>

      <table class="styled-table">
        <thead>
          <tr>
            <th style="width: 24%;">Swimlane / Actor</th>
            <th style="width: 36%;">Core Responsibilities</th>
            <th style="width: 40%;">Primary Activities Handled</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>1. Operator / Player</strong><br><span class="badge" style="background:#e0f2fe; color:#0369a1;">Student Researcher</span></td>
            <td>Initiates mission applications, inputs vessel configurations, uploads compliance documentation, submits weekly patrol records, and uploads final waste offloading reports.</td>
            <td>Login, Submit Mission Request, Submit Vessel Details, Upload Documents, Correct Parameters, Submit Weekly Logs, Upload Manifest, Submit Feedback.</td>
          </tr>
          <tr>
            <td><strong>2. OceanCleanFlow System</strong><br><span class="badge" style="background:#f1f5f9; color:#334155;">Autonomous Platform</span></td>
            <td>Executes credential validation, performs automated telemetry pre-audits, tracks the 14-week timeline, coordinates external auditor tokens, and calculates eco-credits.</td>
            <td>Verify Login, Pre-Audit Checks, Dispatch Auditor Link, Record Timeline, Track Weekly Logs, Calculate Eco-Credits, Lock System Logs.</td>
          </tr>
          <tr>
            <td><strong>3. Faculty Mentor</strong><br><span class="badge" style="background:#fef3c7; color:#92400e;">Marine Supervisor</span></td>
            <td>Reviews mission route feasibility, assesses flagged environmental risks, approves/rejects requests with remarks, audits weekly logs, and inspects final recycling receipts.</td>
            <td>Review Mission Request, Evaluate Environmental Flags, Approve/Reject Request, Review Weekly Logs, Inspect Waste Offload Manifest.</td>
          </tr>
          <tr>
            <td><strong>4. Harbor Director (HOD)</strong><br><span class="badge" style="background:#f3e8ff; color:#6b21a8;">Station Chief</span></td>
            <td>Exercises final institutional authority for vessel departure, manages berth allocation, reviews department-wide cleanup impact analytics, and enforces marine compliance.</td>
            <td>Review Institutional Departure Requests, Grant Harbor Clearance, Issue Official Rejections, Monitor Departmental Eco-Metrics.</td>
          </tr>
        </tbody>
      </table>

      <h2>The 19 Identified Activities in OceanCleanFlow</h2>
      <ol style="font-size: 9.5pt; line-height: 1.4;">
        <li><strong>Login to OceanCleanFlow:</strong> Student operator inputs cryptographic credentials to access the command terminal.</li>
        <li><strong>Submit Mission Request:</strong> Operator initiates a formal cleanup proposal for a designated ocean sector.</li>
        <li><strong>Submit Vessel &amp; Sector Details:</strong> Operator specifies vessel tonnage, battery capacity, sensor payload, and GPS waypoints.</li>
        <li><strong>Upload Mission Documents:</strong> Operator uploads vessel seaworthiness certificates, insurance, and emergency protocols.</li>
        <li><strong>Verify Login Details:</strong> System validates operator authentication tokens and checks security credentials.</li>
        <li><strong>Perform Pre-Audit Checks:</strong> System executes automated checks on telemetry streams, file formats, and sensor bounds.</li>
        <li><strong>Verify Environmental Compliance:</strong> External Recycling/Environmental Auditor validates facility authenticity via a one-time link.</li>
        <li><strong>Review Mission Request:</strong> Faculty Mentor conducts academic and operational evaluation of proposed mission routes.</li>
        <li><strong>Approve or Reject Request:</strong> Faculty Mentor issues formal endorsement or rejects with specific corrective remarks.</li>
        <li><strong>Forward Request to Harbor HOD:</strong> System automatically elevates faculty-approved requests for institutional clearance.</li>
        <li><strong>Final Harbor Approval or Rejection:</strong> Harbor Operations Director (HOD) issues official departure authorization.</li>
        <li><strong>Start Ocean Cleanup Mission:</strong> Approved vessel activates navigation autopilot and departs harbor for ocean patrol.</li>
        <li><strong>Submit Weekly Patrol Log:</strong> Operator transmits weekly debris tonnage, battery telemetry, and marine wildlife encounters.</li>
        <li><strong>Review Weekly Patrol Log:</strong> Faculty Mentor reviews submitted telemetry, verifies zero bycatch, and logs operational remarks.</li>
        <li><strong>Upload Completion Documents:</strong> Operator uploads final harbor docking receipts, weighbridge slips, and recycling manifests.</li>
        <li><strong>Verify Completion Documents:</strong> Faculty Mentor audits offloaded plastic tonnage against recycling facility verification.</li>
        <li><strong>Mark Mission Completed:</strong> System transitions mission state to "Completed", locking operational records in persistent storage.</li>
        <li><strong>Calculate Eco-Credits:</strong> System algorithmically computes token rewards based on kilograms of ocean plastic removed.</li>
        <li><strong>Submit Final Feedback:</strong> Operator completes a debriefing survey evaluating vessel efficiency and system performance.</li>
      </ol>
    </div>

    <!-- ==================== PAGE 5: STEP-BY-STEP ACTIVITY FLOWS (6.1 TO 6.3) ==================== -->
    <div class="page">
      <h2>Step-by-Step Activity Flows (Phases 6.1 to 6.3)</h2>

      <h3>6.1 Operator Login and Mission Application</h3>
      <p>The lifecycle begins when the operator accesses the OceanCleanFlow client. The system checks login credentials. If invalid, an error is displayed and the operator is prompted to retry. Upon successful authentication, the operator submits mission parameters, enters vessel specifications, and uploads seaworthiness documentation.</p>
      
      <div class="flow-box">
        <img src="flow_6_1_login.svg" alt="Activity Flow 6.1: Login & Application">
      </div>

      <h3>6.2 Pre-Audit Checks and External Auditor Verification</h3>
      <p>Upon submission, the system executes automated pre-audit diagnostics. If telemetry or documentation is invalid, the operator must revise and re-upload. If valid, an automated one-time verification link is transmitted to the External Recycling Auditor. If the auditor approves, the request moves to faculty review; if flagged for environmental hazards, special safety flags are appended.</p>

      <div class="flow-box">
        <img src="flow_6_2_preaudit.svg" alt="Activity Flow 6.2: Pre-Audit & Auditor Verification">
      </div>

      <h3>6.3 Faculty Mentor and HOD Institutional Approval</h3>
      <p>The Faculty Mentor reviews the mission route and environmental flags. If rejected, the student receives detailed corrective feedback to revise the proposal. If approved, the request is forwarded to the Harbor Operations Director (HOD) for institutional berth and departure clearance. Upon HOD approval, the vessel schedule is officially activated.</p>

      <div class="flow-box">
        <img src="flow_6_3_approval.svg" alt="Activity Flow 6.3: Faculty and HOD Approval Hierarchy">
      </div>
    </div>

    <!-- ==================== PAGE 6: STEP-BY-STEP ACTIVITY FLOWS (6.4 & 6.5) ==================== -->
    <div class="page">
      <h2>Step-by-Step Activity Flows (Phases 6.4 &amp; 6.5)</h2>

      <h3>6.4 Weekly Progress Tracking and 14-Week Patrol Milestone Loop</h3>
      <p>Once deployed, the vessel operates along autonomous patrol routes. Every week, the student operator submits a comprehensive progress log detailing extracted plastic mass, battery degradation, and marine life safety pings. The Faculty Mentor reviews each log and adds operational guidance. The system evaluates the 14-week duration milestone: if fewer than 14 weeks are complete, execution loops to the next weekly cycle; if all 14 weeks are satisfied, the workflow transitions to completion.</p>

      <div class="flow-box">
        <img src="flow_6_4_weekly.svg" alt="Activity Flow 6.4: 14-Week Patrol Progress Tracking Loop">
      </div>

      <h3>6.5 Mission Completion, Recycling Verification &amp; Eco-Credit Calculation</h3>
      <p>Upon completing the 14-week patrol duration, the vessel docks at the harbor recycling terminal. The operator uploads the official completion certificate, weighbridge receipt, and polymer sort manifest. The Faculty Mentor verifies the offload documentation. If rejected, the operator must rectify discrepancies; if approved, the system marks the mission completed, calculates eligible Eco-Credits based on verified tonnage, and the operator submits final feedback.</p>

      <div class="flow-box">
        <img src="flow_6_5_completion.svg" alt="Activity Flow 6.5: Mission Completion & Eco-Credit Settlement">
      </div>

      <h3>Formal Mathematical Credit Calculation Formulation</h3>
      <p>The system calculates total earned <em>Eco-Credits</em> (\(C_{\text{total}}\)) using verified plastic mass \(M_p\) (in kg), an environmental zone difficulty multiplier \(\mu_z\), and a bycatch penalty factor \(\beta\):</p>
      \[
      C_{\text{total}} = \left( \sum_{w=1}^{14} M_p(w) \times \mu_z \times (1 - \beta) \right) + B_{\text{compliance}}
      \]
      <p>where \(B_{\text{compliance}}\) is a bonus awarded for zero-incident safety ratings and timely weekly log submissions.</p>
    </div>

    <!-- ==================== PAGE 7: FULL MASTER ACTIVITY DIAGRAM VISUALIZATION ==================== -->
    <div class="page">
      <h2>Master UML 2.0 Activity Diagram &mdash; Full System View</h2>
      <p>The complete end-to-end activity model unites all four swimlanes, decision nodes, weekly feedback loops, and alternative correction paths into a cohesive, non-blocking workflow:</p>

      <div style="text-align: center; margin: 6px 0 10px 0;">
        <a href="Activity_Diagram_Assignment_7.html" class="interactive-link" contenteditable="false" target="_blank">
          🔗 Launch Full Screen Pan &amp; Zoom Interactive Canvas (Activity_Diagram_Assignment_7.html)
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

    <!-- ==================== PAGE 8: EXCEPTION HANDLING & CONCLUSION ==================== -->
    <div class="page">
      <h2>Alternative Flows, Exception Handling &amp; Verification</h2>
      <p>A resilient system model must account for operational anomalies, sensor faults, and administrative rejections without reaching permanent deadlock:</p>

      <table class="styled-table">
        <thead>
          <tr>
            <th style="width: 28%;">Failure Scenario</th>
            <th style="width: 32%;">System Detection Mechanism</th>
            <th style="width: 40%;">Alternative Control Flow &amp; Recovery Path</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Invalid Authentication</strong></td>
            <td>Credential hash mismatch / expired token.</td>
            <td>System routes flow to error action and loops back to login merge node.</td>
          </tr>
          <tr>
            <td><strong>Pre-Audit Document Failure</strong></td>
            <td>Corrupted file, expired seaworthiness permit.</td>
            <td>Request rejected; system highlights missing fields and loops to upload action.</td>
          </tr>
          <tr>
            <td><strong>Flagged Environmental Risk</strong></td>
            <td>Auditor detects marine sanctuary proximity.</td>
            <td>Request flagged with high priority; diverted to special faculty safety review.</td>
          </tr>
          <tr>
            <td><strong>Faculty / HOD Rejection</strong></td>
            <td>Unfavorable weather or hazardous route.</td>
            <td>Process generates formal rejection memo; operator edits sector waypoints.</td>
          </tr>
          <tr>
            <td><strong>Mid-Patrol Telemetry Loss</strong></td>
            <td>Satellite link timeout &gt; 15 minutes.</td>
            <td>Vessel switches to autonomous station-keeping until connection is re-established.</td>
          </tr>
          <tr>
            <td><strong>Manifest Discrepancy</strong></td>
            <td>Weighbridge reading differs from boat logs.</td>
            <td>Supervisor requests weighbridge re-calibration before credit calculation.</td>
          </tr>
        </tbody>
      </table>

      <h3>UML 2.0 Formal Verification Checklist</h3>
      <table class="styled-table">
        <thead>
          <tr>
            <th>Formal Modeling Criterion</th>
            <th>Verification Status</th>
            <th>Compliance Justification</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><strong>Deadlock Prevention</strong></td>
            <td><span class="badge" style="background:#dcfce7; color:#15803d;">Verified</span></td>
            <td>Every conditional branch either terminates in a valid merge node or reaches the Activity Final node.</td>
          </tr>
          <tr>
            <td><strong>Guard Mutex Property</strong></td>
            <td><span class="badge" style="background:#dcfce7; color:#15803d;">Verified</span></td>
            <td>Decision outputs evaluate mutually exclusive conditions (e.g., <code>[Yes]</code> vs. <code>[No]</code>).</td>
          </tr>
          <tr>
            <td><strong>Partition Isolation</strong></td>
            <td><span class="badge" style="background:#dcfce7; color:#15803d;">Verified</span></td>
            <td>Actions are strictly localized within the responsible swimlane column.</td>
          </tr>
          <tr>
            <td><strong>Cyclic Termination</strong></td>
            <td><span class="badge" style="background:#dcfce7; color:#15803d;">Verified</span></td>
            <td>The 14-week patrol loop possesses a strictly bounded decrementing counter ensuring loop exit.</td>
          </tr>
        </tbody>
      </table>

      <h2>Conclusion</h2>
      <p>Through this assignment, we successfully formulated, designed, and verified a comprehensive <strong>UML 2.0 Activity Diagram</strong> with four structured swimlanes for the <strong>OceanCleanFlow &ndash; Department Marine Cleanup Management System</strong>. The model captures the complete operational lifecycle from initial operator authentication, proposal submission, and pre-audit telemetry checks, through external recycling auditor verification, faculty mentor review, and institutional HOD authorization. Furthermore, the 14-week iterative patrol tracking loop, harbor docking verification, algorithmic eco-credit settlement, and exception recovery paths were thoroughly formalized. This provides a clear, robust behavioral blueprint for engineering the platform's backend workflow and autonomous marine vessel operations.</p>
    </div>

  </div>
</body>
</html>
"""

with open(output_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Assignment_7.html successfully updated and written to {output_path}!")
