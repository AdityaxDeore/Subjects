import os

output_dir = r"c:\Users\adity\Desktop\Subjects\SEML\Assignment - 7"

# Master Diagram with 4 spacious, perfectly structured swimlanes (1140 x 1480)
svg_content = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1140 1480" width="1140" height="1480" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
    <marker id="arrow_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16a34a"/>
    </marker>
    <marker id="arrow_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arrow_amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#d97706"/>
    </marker>
  </defs>

  <!-- Title Banner -->
  <rect x="20" y="12" width="1100" height="42" rx="6" fill="#0f172a"/>
  <text x="570" y="38" font-size="17" font-weight="bold" fill="#ffffff" text-anchor="middle">
    UML 2.0 Activity Diagram &#8212; OceanCleanFlow Department Management System
  </text>

  <!-- Swimlane Columns (Each 275px wide) -->
  <!-- Col 1: Operator / Player -->
  <rect x="20" y="60" width="275" height="1400" fill="#f8fafc" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="20" y="60" width="275" height="38" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.5"/>
  <text x="157" y="84" font-size="13" font-weight="bold" fill="#0369a1" text-anchor="middle">1. Operator / Player (Student)</text>

  <!-- Col 2: OceanCleanFlow System -->
  <rect x="295" y="60" width="275" height="1400" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="295" y="60" width="275" height="38" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
  <text x="432" y="84" font-size="13" font-weight="bold" fill="#334155" text-anchor="middle">2. OceanCleanFlow System</text>

  <!-- Col 3: Faculty Mentor (Supervisor) -->
  <rect x="570" y="60" width="275" height="1400" fill="#fdfbf7" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="570" y="60" width="275" height="38" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
  <text x="707" y="84" font-size="13" font-weight="bold" fill="#92400e" text-anchor="middle">3. Faculty Mentor (Supervisor)</text>

  <!-- Col 4: Harbor Director (HOD) -->
  <rect x="845" y="60" width="275" height="1400" fill="#faf5ff" stroke="#94a3b8" stroke-width="1.5"/>
  <rect x="845" y="60" width="275" height="38" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="982" y="84" font-size="13" font-weight="bold" fill="#6b21a8" text-anchor="middle">4. Harbor Director (HOD)</text>

  <!-- ==================== PHASE 1: LOGIN & APPLICATION ==================== -->
  <!-- Initial Node (Col 1) -->
  <circle cx="157" cy="120" r="13" fill="#0f172a"/>
  <line x1="157" y1="133" x2="157" y2="155" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Merge Node for Login Retry -->
  <polygon points="157,155 168,165 157,175 146,165" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
  <line x1="157" y1="175" x2="157" y2="195" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Login to OceanCleanFlow -->
  <rect x="65" y="195" width="185" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
  <text x="157" y="213" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Login to</text>
  <text x="157" y="227" font-size="10" fill="#0369a1" text-anchor="middle">OceanCleanFlow Portal</text>

  <!-- Arrow to System: Verify Login -->
  <path d="M 250,216 L 335,216" fill="none" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Verify Login Credentials (Col 2) -->
  <rect x="335" y="195" width="195" height="42" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="1.8"/>
  <text x="432" y="213" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Verify Login</text>
  <text x="432" y="227" font-size="10" fill="#334155" text-anchor="middle">Credentials &amp; Session</text>

  <line x1="432" y1="237" x2="432" y2="260" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Decision: Login Valid? (Col 2) -->
  <polygon points="432,260 452,275 432,290 412,275" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.8"/>
  <text x="432" y="278" font-size="8.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Valid?</text>

  <!-- Invalid [No] -> Loop to Login Merge in Col 1 -->
  <path d="M 412,275 L 270,275 L 270,165 L 168,165" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow_red)"/>
  <text x="325" y="268" font-size="9.5" font-weight="bold" fill="#dc2626">[No: Retry]</text>

  <!-- Valid [Yes] -> Col 1 Action -->
  <path d="M 432,290 L 432,320 L 250,320" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <text x="437" y="308" font-size="9.5" font-weight="bold" fill="#16a34a">[Yes]</text>

  <!-- Action: Submit Mission Request & Details (Col 1) -->
  <rect x="55" y="302" width="195" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
  <text x="152" y="319" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Submit Mission Request</text>
  <text x="152" y="333" font-size="10" fill="#0369a1" text-anchor="middle">&amp; Vessel / Sector Details</text>

  <line x1="152" y1="344" x2="152" y2="368" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Upload Mission Documents (Col 1) -->
  <rect x="55" y="368" width="195" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
  <text x="152" y="386" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Upload Mission Docs</text>
  <text x="152" y="400" font-size="10" fill="#0369a1" text-anchor="middle">&amp; Seaworthiness Permits</text>

  <!-- ==================== PHASE 2: PRE-AUDIT & EXTERNAL AUDITOR ==================== -->
  <path d="M 250,389 L 335,389" fill="none" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Perform Pre-Audit Checks (Col 2) -->
  <rect x="335" y="368" width="195" height="42" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="1.8"/>
  <text x="432" y="386" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Perform Pre-Audit Checks</text>
  <text x="432" y="400" font-size="10" fill="#334155" text-anchor="middle">&amp; Telemetry Diagnostics</text>

  <line x1="432" y1="410" x2="432" y2="435" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Decision: Docs Valid? (Col 2) -->
  <polygon points="432,435 452,450 432,465 412,450" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.8"/>
  <text x="432" y="453" font-size="8.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Valid?</text>

  <!-- Invalid [No] -> Loop to Upload in Col 1 -->
  <path d="M 412,450 L 260,450 L 260,398 L 250,398" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow_red)"/>
  <text x="320" y="443" font-size="9.5" font-weight="bold" fill="#dc2626">[Invalid: Re-upload]</text>

  <!-- Valid [Yes] -> Auditor Verify -->
  <line x1="432" y1="465" x2="432" y2="492" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <text x="437" y="480" font-size="9.5" font-weight="bold" fill="#16a34a">[Valid]</text>

  <!-- Action: External Recycling Auditor Verification (Col 2) -->
  <rect x="335" y="492" width="195" height="42" rx="8" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="432" y="510" font-size="11" font-weight="bold" fill="#581c87" text-anchor="middle">External Recycling Auditor</text>
  <text x="432" y="524" font-size="10" fill="#581c87" text-anchor="middle">Verification (One-Time Link)</text>

  <line x1="432" y1="534" x2="432" y2="558" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Decision: Auditor Ok? (Col 2) -->
  <polygon points="432,558 452,573 432,588 412,573" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.8"/>
  <text x="432" y="576" font-size="7.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Auditor?</text>

  <!-- Flagged [Flagged] -> Mentor special review -->
  <path d="M 452,573 L 610,573 L 610,612" fill="none" stroke="#d97706" stroke-width="1.8" marker-end="url(#arrow_amber)"/>
  <text x="515" y="565" font-size="9.5" font-weight="bold" fill="#d97706">[Flagged Case]</text>

  <!-- Approved [Approved] -> Mentor review -->
  <path d="M 432,588 L 432,630 L 600,630" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <text x="437" y="610" font-size="9.5" font-weight="bold" fill="#16a34a">[Approved]</text>

  <!-- ==================== PHASE 3: FACULTY & HOD APPROVAL ==================== -->
  <!-- Merge in Faculty Lane -->
  <polygon points="610,630 620,622 630,630 620,638" fill="#f1f5f9" stroke="#475569" stroke-width="1.4"/>
  <line x1="630" y1="630" x2="650" y2="630" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Review Mission Request (Col 3) -->
  <rect x="650" y="609" width="180" height="42" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
  <text x="740" y="627" font-size="11" font-weight="bold" fill="#92400e" text-anchor="middle">Review Mission Request</text>
  <text x="740" y="641" font-size="10" fill="#92400e" text-anchor="middle">&amp; Environmental Risk</text>

  <line x1="740" y1="651" x2="740" y2="675" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Decision: Faculty Approves? (Col 3) -->
  <polygon points="740,675 760,690 740,705 720,690" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.8"/>
  <text x="740" y="693" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Faculty?</text>

  <!-- Faculty No -> Reject to Operator -->
  <path d="M 720,690 L 220,690 L 220,420 L 152,420 L 152,410" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow_red)"/>
  <text x="320" y="682" font-size="9.5" font-weight="bold" fill="#dc2626">[No: Revise Parameters]</text>

  <!-- Faculty Yes -> Forward to HOD -->
  <path d="M 760,690 L 890,690 L 890,732" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <text x="785" y="682" font-size="9.5" font-weight="bold" fill="#16a34a">[Yes]</text>

  <!-- Action: Review Institutional Request (Col 4) -->
  <rect x="890" y="712" width="185" height="42" rx="8" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="982" y="730" font-size="11" font-weight="bold" fill="#6b21a8" text-anchor="middle">Review Departmental</text>
  <text x="982" y="744" font-size="10" fill="#6b21a8" text-anchor="middle">Mission &amp; Dock Clearance</text>

  <line x1="982" y1="754" x2="982" y2="778" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Decision: HOD Approves? (Col 4) -->
  <polygon points="982,778 1002,793 982,808 962,793" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.8"/>
  <text x="982" y="796" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">HOD?</text>

  <!-- HOD No -> Return via Faculty -->
  <path d="M 962,793 L 740,793 L 740,705" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow_red)"/>
  <text x="860" y="785" font-size="9.5" font-weight="bold" fill="#dc2626">[No: Revise]</text>

  <!-- HOD Yes -> System Activates Mission -->
  <path d="M 982,808 L 982,845 L 530,845" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <text x="987" y="828" font-size="9.5" font-weight="bold" fill="#16a34a">[Yes: Approved]</text>

  <!-- Action: Mark Approved & Activate Vessel (Col 2) -->
  <rect x="335" y="824" width="195" height="42" rx="8" fill="#dcfce7" stroke="#15803d" stroke-width="1.8"/>
  <text x="432" y="842" font-size="11" font-weight="bold" fill="#14532d" text-anchor="middle">Mark Mission Approved</text>
  <text x="432" y="856" font-size="10" fill="#14532d" text-anchor="middle">&amp; Activate Vessel Schedule</text>

  <!-- ==================== PHASE 4: 14-WEEK PATROL LOOP ==================== -->
  <path d="M 335,845 L 245,845" fill="none" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Start Ocean Patrol Mission (Col 1) -->
  <rect x="55" y="824" width="190" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
  <text x="150" y="842" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Start Ocean Patrol Mission</text>
  <text x="150" y="856" font-size="10" fill="#0369a1" text-anchor="middle">(Vessel Enters Active Grid)</text>

  <line x1="150" y1="866" x2="150" y2="890" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Merge Node for 14-week patrol loop (Col 1) -->
  <polygon points="150,890 160,900 150,910 140,900" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
  <line x1="150" y1="910" x2="150" y2="935" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Submit Weekly Patrol Log (Col 1) -->
  <rect x="55" y="935" width="190" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
  <text x="150" y="953" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Submit Weekly Patrol Log</text>
  <text x="150" y="967" font-size="10" fill="#0369a1" text-anchor="middle">(Plastic Tonnage &amp; Health)</text>

  <line x1="245" y1="956" x2="335" y2="956" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Record Weekly Progress (Col 2) -->
  <rect x="335" y="935" width="195" height="42" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="1.8"/>
  <text x="432" y="953" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Record Weekly Progress</text>
  <text x="432" y="967" font-size="10" fill="#334155" text-anchor="middle">&amp; Track 14-Week Mission</text>

  <line x1="530" y1="956" x2="650" y2="956" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Review Weekly Progress (Col 3) -->
  <rect x="650" y="935" width="180" height="42" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
  <text x="740" y="953" font-size="11" font-weight="bold" fill="#92400e" text-anchor="middle">Review Weekly Progress</text>
  <text x="740" y="967" font-size="10" fill="#92400e" text-anchor="middle">&amp; Add Operational Remarks</text>

  <!-- Arrow from Faculty back to System Duration Check -->
  <path d="M 740,977 L 740,1015 L 432,1015 L 432,1035" fill="none" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Decision: 14 Weeks Completed? (Col 2) -->
  <polygon points="432,1035 452,1050 432,1065 412,1050" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.8"/>
  <text x="432" y="1053" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">14 Wks?</text>

  <!-- Loop back path [No] -->
  <path d="M 412,1050 L 40,1050 L 40,900 L 140,900" fill="none" stroke="#d97706" stroke-width="2" marker-end="url(#arrow_amber)"/>
  <text x="210" y="1042" font-size="9.5" font-weight="bold" fill="#d97706">[No: Week &lt; 14 &#8212; Continue Patrol]</text>

  <!-- Proceed [Yes] -> Col 1 -->
  <path d="M 432,1065 L 432,1105 L 245,1105" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <text x="437" y="1085" font-size="9.5" font-weight="bold" fill="#16a34a">[Yes: 14 Weeks Complete]</text>

  <!-- ==================== PHASE 5: COMPLETION & ECO-CREDITS ==================== -->
  <!-- Merge for Completion Docs Correction -->
  <polygon points="150,1118 160,1128 150,1138 140,1128" fill="#f1f5f9" stroke="#475569" stroke-width="1.5"/>
  <line x1="200" y1="1105" x2="150" y2="1105" stroke="#16a34a" stroke-width="1.8"/>
  <line x1="150" y1="1105" x2="150" y2="1118" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <line x1="150" y1="1138" x2="150" y2="1160" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Upload Completion Docs (Col 1) -->
  <rect x="55" y="1160" width="190" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
  <text x="150" y="1178" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Upload Completion Certificate</text>
  <text x="150" y="1192" font-size="10" fill="#0369a1" text-anchor="middle">&amp; Final Waste Manifest Report</text>

  <path d="M 245,1181 L 650,1181" fill="none" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Review Completion Documents (Col 3) -->
  <rect x="650" y="1160" width="180" height="42" rx="8" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
  <text x="740" y="1178" font-size="11" font-weight="bold" fill="#92400e" text-anchor="middle">Review Completion Documents</text>
  <text x="740" y="1192" font-size="10" fill="#92400e" text-anchor="middle">&amp; Offloaded Recycling Slips</text>

  <line x1="740" y1="1202" x2="740" y2="1225" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Decision: Completion Docs Approved? (Col 3) -->
  <polygon points="740,1225 760,1240 740,1255 720,1240" fill="#fef9c3" stroke="#ca8a04" stroke-width="1.8"/>
  <text x="740" y="1243" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Approved?</text>

  <!-- No -> Resubmit manifest -->
  <path d="M 720,1240 L 265,1240 L 265,1128 L 160,1128" fill="none" stroke="#dc2626" stroke-width="1.8" marker-end="url(#arrow_red)"/>
  <text x="440" y="1232" font-size="9.5" font-weight="bold" fill="#dc2626">[No: Resubmit Manifest]</text>

  <!-- Yes -> System Mark Completed -->
  <path d="M 740,1255 L 740,1292 L 530,1292" fill="none" stroke="#16a34a" stroke-width="1.8" marker-end="url(#arrow_green)"/>
  <text x="745" y="1275" font-size="9.5" font-weight="bold" fill="#16a34a">[Yes: Approved]</text>

  <!-- Action: Mark Mission Completed (Col 2) -->
  <rect x="335" y="1271" width="195" height="42" rx="8" fill="#f1f5f9" stroke="#475569" stroke-width="1.8"/>
  <text x="432" y="1289" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">Mark Mission Completed</text>
  <text x="432" y="1303" font-size="10" fill="#334155" text-anchor="middle">&amp; Lock Logbook Records</text>

  <line x1="432" y1="1313" x2="432" y2="1340" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Calculate Credits (Col 2) -->
  <rect x="335" y="1340" width="195" height="42" rx="8" fill="#dcfce7" stroke="#15803d" stroke-width="1.8"/>
  <text x="432" y="1358" font-size="11" font-weight="bold" fill="#14532d" text-anchor="middle">Calculate Eco-Credits</text>
  <text x="432" y="1372" font-size="10" fill="#14532d" text-anchor="middle">&amp; Diverted Plastic Footprint</text>

  <!-- Arrow to Operator Submit Feedback -->
  <path d="M 335,1361 L 245,1361" fill="none" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Action: Submit Final Feedback (Col 1) -->
  <rect x="55" y="1340" width="190" height="42" rx="8" fill="#e0f2fe" stroke="#0284c7" stroke-width="1.8"/>
  <text x="150" y="1358" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Submit Final Feedback</text>
  <text x="150" y="1372" font-size="10" fill="#0369a1" text-anchor="middle">&amp; Vessel Debrief</text>

  <line x1="150" y1="1382" x2="150" y2="1415" stroke="#0f172a" stroke-width="2" marker-end="url(#arrow)"/>

  <!-- Final Node (Col 1) -->
  <circle cx="150" cy="1432" r="16" fill="none" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="150" cy="1432" r="10" fill="#0f172a"/>
  <text x="150" y="1462" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Activity Final</text>

</svg>'''

with open(os.path.join(output_dir, "master_activity_diagram.svg"), "w", encoding="utf-8") as f:
    f.write(svg_content)

# Update the interactive Panzoom HTML viewer
viewer_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OceanCleanFlow &mdash; Master UML 2.0 Activity Diagram</title>
    <script src="https://unpkg.com/@panzoom/panzoom@4.5.1/dist/panzoom.min.js"></script>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body, html {
            width: 100vw;
            height: 100vh;
            margin: 0;
            padding: 0;
            overflow: hidden;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            background-color: #f1f5f9;
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
            background-size: 24px 24px;
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

        .toolbar {
            position: fixed;
            bottom: 24px;
            left: 50%;
            transform: translateX(-50%);
            display: flex;
            gap: 12px;
            background: rgba(15, 23, 42, 0.9);
            backdrop-filter: blur(8px);
            padding: 10px 18px;
            border-radius: 40px;
            box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.3);
            z-index: 100;
        }

        .btn {
            background: #1e293b;
            color: #f8fafc;
            border: 1px solid #334155;
            padding: 8px 16px;
            font-size: 13px;
            font-weight: 600;
            border-radius: 20px;
            cursor: pointer;
            display: flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
        }

        .btn:hover {
            background: #0284c7;
            border-color: #38bdf8;
            color: #ffffff;
            transform: translateY(-1px);
        }

        .btn-primary {
            background: #0284c7;
            border-color: #38bdf8;
        }
        .btn-primary:hover {
            background: #0369a1;
        }

        .info-pill {
            position: fixed;
            top: 20px;
            left: 24px;
            background: rgba(255, 255, 255, 0.95);
            padding: 12px 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #e2e8f0;
            z-index: 100;
            font-size: 13px;
            color: #334155;
        }
        .info-pill h1 {
            font-size: 15px;
            font-weight: 700;
            color: #0f172a;
            margin-bottom: 4px;
        }
    </style>
</head>
<body>

    <div class="info-pill">
        <h1>OceanCleanFlow &mdash; UML 2.0 Activity Diagram</h1>
        <span>Interactive Canvas &bull; Drag to Pan &bull; Scroll to Zoom</span>
    </div>

    <div class="canvas-container" id="container">
        <div id="pan-viewport">
''' + svg_content + '''
        </div>
    </div>

    <div class="toolbar">
        <button class="btn" id="zoom-in">➕ Zoom In</button>
        <button class="btn" id="zoom-out">➖ Zoom Out</button>
        <button class="btn" id="reset">↺ Reset View</button>
        <button class="btn btn-primary" id="download">💾 Download SVG</button>
    </div>

    <script>
        const viewport = document.getElementById('pan-viewport');
        const container = document.getElementById('container');
        
        const panzoom = Panzoom(viewport, {
            maxScale: 3,
            minScale: 0.3,
            initialScale: 0.65,
            contain: 'outside'
        });

        container.addEventListener('wheel', panzoom.zoomWithWheel);

        document.getElementById('zoom-in').addEventListener('click', panzoom.zoomIn);
        document.getElementById('zoom-out').addEventListener('click', panzoom.zoomOut);
        document.getElementById('reset').addEventListener('click', () => {
            panzoom.reset();
        });

        document.getElementById('download').addEventListener('click', () => {
            const svgData = document.querySelector('svg').outerHTML;
            const blob = new Blob([svgData], { type: 'image/svg+xml;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = url;
            a.download = 'oceancleanflow_master_activity_diagram.svg';
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        });
    </script>
</body>
</html>'''

with open(os.path.join(output_dir, "Activity_Diagram_Assignment_7.html"), "w", encoding="utf-8") as f:
    f.write(viewer_html)

print("Master SVG and interactive viewer regenerated!")
