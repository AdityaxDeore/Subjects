import os

output_dir = r"c:\Users\adity\Desktop\Subjects\SEML\Assignment - 7"
os.makedirs(output_dir, exist_ok=True)

# 1. Flow 6.1: Operator Authentication & Application Initiation Flow
flow_6_1 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 230" width="100%" height="auto" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <marker id="arr1" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
    <marker id="arr1_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arr1_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16a34a"/>
    </marker>
  </defs>

  <!-- Initial Node -->
  <circle cx="35" cy="115" r="14" fill="#0f172a"/>
  <line x1="49" y1="115" x2="80" y2="115" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr1)"/>
  
  <!-- Merge Node for Login Retry (Point 8) -->
  <polygon points="95,115 110,100 125,115 110,130" fill="#f1f5f9" stroke="#475569" stroke-width="1.8"/>
  <line x1="125" y1="115" x2="155" y2="115" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr1)"/>

  <!-- Action: Login to OceanCleanFlow -->
  <rect x="155" y="89" width="165" height="52" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="237" y="112" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Login to</text>
  <text x="237" y="128" font-size="11" fill="#0369a1" text-anchor="middle">OceanCleanFlow Portal</text>

  <line x1="320" y1="115" x2="355" y2="115" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr1)"/>

  <!-- Action: Verify Login Credentials & Session -->
  <rect x="355" y="89" width="165" height="52" rx="10" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
  <text x="437" y="112" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Verify Login</text>
  <text x="437" y="128" font-size="11" fill="#334155" text-anchor="middle">Credentials &amp; Session</text>

  <line x1="520" y1="115" x2="555" y2="115" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr1)"/>

  <!-- Decision: Credentials Valid? -->
  <polygon points="575,115 595,95 615,115 595,135" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="595" y="119" font-size="9" font-weight="bold" fill="#854d0e" text-anchor="middle">Valid?</text>

  <!-- [Invalid Credentials] -> Clean Loop back to Merge Node (Point 8) -->
  <path d="M 595,95 L 595,45 L 110,45 L 110,100" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arr1_red)"/>
  <text x="350" y="38" font-size="10.5" font-weight="bold" fill="#dc2626">[Invalid Credentials: Prompt Retry]</text>

  <!-- [Valid Credentials] -> Submit Mission Request -->
  <line x1="615" y1="115" x2="665" y2="115" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr1_green)"/>
  <text x="640" y="106" font-size="10" font-weight="bold" fill="#16a34a">[Valid]</text>

  <!-- Action: Submit Mission Request & Vessel Specs -->
  <rect x="665" y="89" width="145" height="52" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="737" y="112" font-size="11.5" font-weight="bold" fill="#0369a1" text-anchor="middle">Submit Request &amp;</text>
  <text x="737" y="128" font-size="10.5" fill="#0369a1" text-anchor="middle">Vessel / Sector Specs</text>

  <line x1="810" y1="115" x2="840" y2="115" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr1)"/>

  <!-- Action: Upload Seaworthiness Permits -->
  <rect x="840" y="89" width="125" height="52" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="902" y="112" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Upload Permits &amp;</text>
  <text x="902" y="128" font-size="10" fill="#0369a1" text-anchor="middle">Insurance PDFs</text>

  <text x="490" y="200" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 6.1: Operator Authentication &amp; Application Initiation Flow</text>
</svg>'''

with open(os.path.join(output_dir, "flow_6_1_login.svg"), "w", encoding="utf-8") as f:
    f.write(flow_6_1)

# 2. Flow 6.2: Pre-Audit Telemetry Check & External Environmental Verification Flow
flow_6_2 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 230" width="100%" height="auto" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <marker id="arr2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
    <marker id="arr2_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arr2_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16a34a"/>
    </marker>
    <marker id="arr2_amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#d97706"/>
    </marker>
  </defs>

  <!-- Incoming Flow from Upload -->
  <line x1="15" y1="95" x2="45" y2="95" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr2)"/>

  <!-- Action: Pre-Audit Checks -->
  <rect x="45" y="68" width="195" height="54" rx="10" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
  <text x="142" y="92" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Execute Automated</text>
  <text x="142" y="108" font-size="11" fill="#334155" text-anchor="middle">Pre-Audit Diagnostics</text>

  <line x1="240" y1="95" x2="275" y2="95" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr2)"/>

  <!-- Decision: Pre-Audit Passed? -->
  <polygon points="295,95 315,75 335,95 315,115" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="315" y="99" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Pre-Audit?</text>

  <!-- Invalid branch -> loop back to correct -->
  <path d="M 315,75 L 315,30 L 142,30 L 142,68" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arr2_red)"/>
  <text x="228" y="24" font-size="10" font-weight="bold" fill="#dc2626">[Pre-Audit Failed: Re-upload Docs]</text>

  <!-- Valid branch -> Forward to External Auditor (Point 9) -->
  <line x1="335" y1="95" x2="380" y2="95" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr2_green)"/>
  <text x="355" y="87" font-size="9.5" font-weight="bold" fill="#16a34a">[Passed]</text>

  <!-- Action: Verify with External Auditor (Swimlane 3) -->
  <rect x="380" y="68" width="225" height="54" rx="10" fill="#ccfbf1" stroke="#0d9488" stroke-width="2"/>
  <text x="492" y="92" font-size="12" font-weight="bold" fill="#0f766e" text-anchor="middle">Verify Recycling Partner</text>
  <text x="492" y="108" font-size="10.5" fill="#0f766e" text-anchor="middle">&amp; Marine Sanctuaries (Auditor)</text>

  <line x1="605" y1="95" x2="640" y2="95" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr2)"/>

  <!-- Decision: Compliant? -->
  <polygon points="660,95 680,75 700,95 680,115" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="680" y="99" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Compliant?</text>

  <!-- Flagged / Reject branch -->
  <path d="M 680,115 L 680,158 L 745,158" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arr2_red)"/>
  <text x="698" y="145" font-size="9.5" font-weight="bold" fill="#dc2626">[Hazard Flagged: Adjust Bounds]</text>

  <rect x="745" y="136" width="215" height="46" rx="8" fill="#fee2e2" stroke="#ef4444" stroke-width="1.6"/>
  <text x="852" y="156" font-size="11" font-weight="bold" fill="#b91c1c" text-anchor="middle">Return to Operator</text>
  <text x="852" y="171" font-size="10" fill="#b91c1c" text-anchor="middle">Adjust Grid Coordinates</text>

  <!-- Approved branch -->
  <line x1="700" y1="95" x2="745" y2="95" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr2_green)"/>
  <text x="720" y="87" font-size="10" font-weight="bold" fill="#16a34a">[Certified]</text>

  <rect x="745" y="68" width="215" height="54" rx="10" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <text x="852" y="92" font-size="12" font-weight="bold" fill="#78350f" text-anchor="middle">Proceed to Faculty Mentor</text>
  <text x="852" y="108" font-size="11" fill="#78350f" text-anchor="middle">Proposal Review</text>

  <text x="490" y="212" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 6.2: Pre-Audit Telemetry Check &amp; External Environmental Verification</text>
</svg>'''

with open(os.path.join(output_dir, "flow_6_2_preaudit.svg"), "w", encoding="utf-8") as f:
    f.write(flow_6_2)

# 3. Flow 6.3: Supervisor and HOD Approval Workflow (Priority Fix #6)
flow_6_3 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 240" width="100%" height="auto" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <marker id="arr3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
    <marker id="arr3_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
    </marker>
    <marker id="arr3_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16a34a"/>
    </marker>
  </defs>

  <line x1="15" y1="90" x2="45" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr3)"/>

  <!-- Priority Fix #6: Merge Node for Faculty Review -->
  <polygon points="55,90 68,78 81,90 68,102" fill="#f1f5f9" stroke="#475569" stroke-width="1.6"/>
  <line x1="81" y1="90" x2="105" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr3)"/>

  <!-- Action: Faculty Supervisor Review -->
  <rect x="105" y="65" width="185" height="52" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="197" y="88" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">Review Mission Proposal</text>
  <text x="197" y="104" font-size="11" fill="#92400e" text-anchor="middle">&amp; Route Safety Dossier</text>

  <line x1="290" y1="90" x2="325" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr3)"/>

  <!-- Decision: Faculty Endorsed? -->
  <polygon points="345,90 365,70 385,90 365,110" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="365" y="94" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Endorsed?</text>

  <!-- Faculty No -> Return to Proposal Resubmission -->
  <path d="M 365,70 L 365,30 L 450,30" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arr3_red)"/>
  <text x="375" y="48" font-size="9.5" font-weight="bold" fill="#dc2626">[Faculty Rejected]</text>
  <rect x="450" y="14" width="175" height="34" rx="6" fill="#fee2e2" stroke="#ef4444" stroke-width="1.4"/>
  <text x="537" y="35" font-size="10.5" font-weight="bold" fill="#b91c1c" text-anchor="middle">Return to Operator Proposal</text>

  <!-- Faculty Yes -> Forward to Harbor Director HOD -->
  <line x1="385" y1="90" x2="435" y2="90" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr3_green)"/>
  <text x="410" y="82" font-size="10" font-weight="bold" fill="#16a34a">[Approved]</text>

  <!-- Action: Harbor Director Berth & Traffic Clearance -->
  <rect x="435" y="65" width="185" height="52" rx="10" fill="#f3e8ff" stroke="#7c3aed" stroke-width="2"/>
  <text x="527" y="88" font-size="12" font-weight="bold" fill="#6b21a8" text-anchor="middle">Review Berth Allocation</text>
  <text x="527" y="104" font-size="11" fill="#6b21a8" text-anchor="middle">&amp; Harbor Traffic Clearance</text>

  <line x1="620" y1="90" x2="655" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr3)"/>

  <!-- Decision: Harbor Cleared? -->
  <polygon points="675,90 695,70 715,90 695,110" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="695" y="94" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Cleared?</text>

  <!-- Priority Fix #6: HOD Clearance Denied -> Loops back directly to Faculty Review Merge Node! -->
  <path d="M 695,110 L 695,160 L 68,160 L 68,102" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arr3_red)"/>
  <text x="400" y="152" font-size="10" font-weight="bold" fill="#dc2626">[Clearance Denied: Re-evaluate Route via Faculty Review]</text>

  <!-- HOD Yes -> Activate Vessel -->
  <line x1="715" y1="90" x2="770" y2="90" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr3_green)"/>
  <text x="740" y="82" font-size="10" font-weight="bold" fill="#16a34a">[Approved]</text>

  <rect x="770" y="65" width="195" height="52" rx="10" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
  <text x="867" y="88" font-size="12" font-weight="bold" fill="#14532d" text-anchor="middle">Activate Vessel Schedule</text>
  <text x="867" y="104" font-size="11" fill="#14532d" text-anchor="middle">&amp; Issue Departure Token</text>

  <text x="490" y="220" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 6.3: Institutional Faculty Mentor &amp; Harbor Director Authorization Hierarchy</text>
</svg>'''

with open(os.path.join(output_dir, "flow_6_3_approval.svg"), "w", encoding="utf-8") as f:
    f.write(flow_6_3)

# 4. Flow 6.4: 14-Week Patrol Progress Tracking Loop Flow (Priority Fix #3 & #4)
flow_6_4 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 230" width="100%" height="auto" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <marker id="arr4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
    <marker id="arr4_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16a34a"/>
    </marker>
    <marker id="arr4_amber" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#d97706"/>
    </marker>
  </defs>

  <line x1="15" y1="90" x2="50" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr4)"/>

  <!-- Priority Fix #3 & #4: Merge Node for Weekly Loop -->
  <polygon points="65,90 80,75 95,90 80,105" fill="#f1f5f9" stroke="#475569" stroke-width="1.8"/>
  <line x1="95" y1="90" x2="125" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr4)"/>

  <!-- Action: Submit Weekly Progress -->
  <rect x="125" y="65" width="195" height="52" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="222" y="88" font-size="12" font-weight="bold" fill="#0369a1" text-anchor="middle">Submit Weekly Patrol Log</text>
  <text x="222" y="104" font-size="11" fill="#0369a1" text-anchor="middle">(Plastic Tonnage &amp; Telemetry)</text>

  <line x1="320" y1="90" x2="355" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr4)"/>

  <!-- Action: Record Telemetry & Increment Week -->
  <rect x="355" y="65" width="195" height="52" rx="10" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
  <text x="452" y="88" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Record Weekly Telemetry</text>
  <text x="452" y="104" font-size="11" fill="#334155" text-anchor="middle">&amp; Increment Week Counter</text>

  <line x1="550" y1="90" x2="585" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr4)"/>

  <!-- Action: Review Weekly Progress -->
  <rect x="585" y="65" width="195" height="52" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="682" y="88" font-size="12" font-weight="bold" fill="#92400e" text-anchor="middle">Review Weekly Progress Log</text>
  <text x="682" y="104" font-size="11" fill="#92400e" text-anchor="middle">&amp; Sign Off Wildlife Safety</text>

  <line x1="780" y1="90" x2="815" y2="90" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr4)"/>

  <!-- Decision: 14 Weeks Completed? -->
  <polygon points="835,90 855,70 875,90 855,110" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="855" y="94" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">14 Wks?</text>

  <!-- Deterministic Loop back path [Week < 14] -->
  <path d="M 855,110 L 855,158 L 80,158 L 80,105" fill="none" stroke="#d97706" stroke-width="2.2" marker-end="url(#arr4_amber)"/>
  <text x="460" y="150" font-size="11" font-weight="bold" fill="#d97706">[Week &lt; 14: Continue Patrol Loop]</text>

  <!-- Deterministic Exit loop path [Week = 14] -->
  <line x1="875" y1="90" x2="915" y2="90" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr4_green)"/>
  <text x="895" y="82" font-size="9" font-weight="bold" fill="#16a34a">[= 14]</text>

  <!-- Proceed to Docking -->
  <circle cx="940" cy="90" r="14" fill="#15803d"/>
  <text x="940" y="94" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">Dock</text>

  <text x="490" y="212" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 6.4: Iterative 14-Week Patrol Progress Tracking &amp; Milestone Verification Loop</text>
</svg>'''

with open(os.path.join(output_dir, "flow_6_4_weekly.svg"), "w", encoding="utf-8") as f:
    f.write(flow_6_4)

# 5. Flow 6.5: Mission Completion, Recycling Verification & Settlement (Priority Fix #5, #7, #12)
flow_6_5 = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 980 240" width="100%" height="auto" style="background:#ffffff; font-family:'Segoe UI', Arial, sans-serif;">
  <defs>
    <marker id="arr5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
    <marker id="arr5_green" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#16a34a"/>
    </marker>
    <marker id="arr5_red" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#dc2626"/>
    </marker>
  </defs>

  <line x1="15" y1="85" x2="35" y2="85" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr5)"/>

  <!-- Priority Fix #7: Merge Node for Manifest Resubmission -->
  <polygon points="45,85 58,73 71,85 58,97" fill="#f1f5f9" stroke="#475569" stroke-width="1.6"/>
  <line x1="71" y1="85" x2="95" y2="85" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr5)"/>

  <!-- Action: Upload Final Waste Manifest -->
  <rect x="95" y="60" width="180" height="50" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="185" y="82" font-size="11.5" font-weight="bold" fill="#0369a1" text-anchor="middle">Upload Final Waste Manifest</text>
  <text x="185" y="98" font-size="10.5" fill="#0369a1" text-anchor="middle">&amp; Shore Weighbridge Receipts</text>

  <line x1="275" y1="85" x2="305" y2="85" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr5)"/>

  <!-- Action: Audit Weighbridge Receipts & Records -->
  <rect x="305" y="60" width="185" height="50" rx="10" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
  <text x="397" y="82" font-size="11.5" font-weight="bold" fill="#92400e" text-anchor="middle">Audit Weighbridge Receipts</text>
  <text x="397" y="98" font-size="10.5" fill="#92400e" text-anchor="middle">&amp; NIR Polymer Sorting Records</text>

  <line x1="490" y1="85" x2="520" y2="85" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr5)"/>

  <!-- Decision: Manifest Verified? -->
  <polygon points="535,85 555,65 575,85 555,105" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="555" y="89" font-size="8" font-weight="bold" fill="#854d0e" text-anchor="middle">Verified?</text>

  <!-- Priority Fix #7: Discrepancy > 2%: Resubmit Manifest directly loops back to Manifest Merge Node! -->
  <path d="M 555,65 L 555,25 L 58,25 L 58,73" fill="none" stroke="#dc2626" stroke-width="2" marker-end="url(#arr5_red)"/>
  <text x="305" y="19" font-size="10" font-weight="bold" fill="#dc2626">[Discrepancy &gt; 2%: Resubmit Manifest &amp; Reconcile Weight]</text>

  <!-- Yes branch -> Mark Completed -->
  <line x1="575" y1="85" x2="610" y2="85" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr5_green)"/>
  <text x="592" y="77" font-size="10" font-weight="bold" fill="#16a34a">[Verified]</text>

  <rect x="610" y="60" width="165" height="50" rx="10" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
  <text x="692" y="82" font-size="11.5" font-weight="bold" fill="#334155" text-anchor="middle">Mark Mission COMPLETED</text>
  <text x="692" y="98" font-size="10.5" fill="#334155" text-anchor="middle">&amp; Lock Persistent Logbooks</text>

  <line x1="775" y1="85" x2="805" y2="85" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr5)"/>

  <!-- Action: Record Diverted Plastic Mass & Issue Digital Certificate (Priority Fix #5, #12) -->
  <rect x="805" y="60" width="165" height="50" rx="10" fill="#dcfce7" stroke="#15803d" stroke-width="2"/>
  <text x="887" y="82" font-size="11" font-weight="bold" fill="#14532d" text-anchor="middle">Record Diverted Plastic Mass</text>
  <text x="887" y="98" font-size="10" fill="#14532d" text-anchor="middle">&amp; Issue Digital Certificate</text>

  <!-- Downwards to feedback and final -->
  <path d="M 887,110 L 887,155 L 755,155" fill="none" stroke="#0f172a" stroke-width="2" marker-end="url(#arr5)"/>

  <rect x="540" y="132" width="215" height="46" rx="10" fill="#e0f2fe" stroke="#0284c7" stroke-width="2"/>
  <text x="647" y="152" font-size="11.5" font-weight="bold" fill="#0369a1" text-anchor="middle">Submit Final Debriefing</text>
  <text x="647" y="167" font-size="10.5" fill="#0369a1" text-anchor="middle">&amp; Platform Feedback Survey</text>

  <line x1="540" y1="155" x2="480" y2="155" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr5)"/>

  <!-- Activity Final Node -->
  <circle cx="450" cy="155" r="16" fill="none" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="450" cy="155" r="10" fill="#0f172a"/>
  <text x="450" y="188" font-size="11" font-weight="bold" fill="#0f172a" text-anchor="middle">Activity Final</text>

  <text x="490" y="222" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Figure 6.5: Mission Completion, Recycling Verification &amp; Closeout Settlement</text>
</svg>'''

with open(os.path.join(output_dir, "flow_6_5_completion.svg"), "w", encoding="utf-8") as f:
    f.write(flow_6_5)

print("Redesigned subflow diagrams generated with exact master diagram alignments!")
