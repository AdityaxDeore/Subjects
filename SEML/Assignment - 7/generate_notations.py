import os

output_dir = r"c:\Users\adity\Desktop\Subjects\SEML\Assignment - 7"
os.makedirs(output_dir, exist_ok=True)

# 1. Initial Node SVG (Clean, textbook style)
initial_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 140" width="160" height="140" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arr_i" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
  </defs>
  <!-- Solid Black Circle -->
  <circle cx="80" cy="35" r="18" fill="#0f172a"/>
  <!-- Outgoing Flow -->
  <line x1="80" y1="53" x2="80" y2="105" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_i)"/>
  <!-- Label -->
  <text x="80" y="128" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Initial Node</text>
</svg>'''

with open(os.path.join(output_dir, "notation_initial.svg"), "w", encoding="utf-8") as f:
    f.write(initial_svg)

# 2. Action / Activity Node SVG (Rounded Rectangle with ample padding)
action_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 140" width="240" height="140" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arr_a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
  </defs>
  <!-- Incoming Flow -->
  <line x1="120" y1="10" x2="120" y2="35" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_a)"/>
  <!-- Action Rounded Rect -->
  <rect x="25" y="38" width="190" height="48" rx="12" ry="12" fill="#eff6ff" stroke="#1d4ed8" stroke-width="2"/>
  <text x="120" y="67" font-size="13" font-weight="bold" fill="#1e3a8a" text-anchor="middle">Submit Mission Request</text>
  <!-- Outgoing Flow -->
  <line x1="120" y1="86" x2="120" y2="115" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_a)"/>
  <!-- Label -->
  <text x="120" y="132" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Action / Activity</text>
</svg>'''

with open(os.path.join(output_dir, "notation_action.svg"), "w", encoding="utf-8") as f:
    f.write(action_svg)

# 3. Control Flow SVG (Directed connector)
control_flow_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 140" width="240" height="140" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arr_cf" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
  </defs>
  <!-- Activity A -->
  <rect x="50" y="12" width="140" height="34" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="1.8"/>
  <text x="120" y="34" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Activity A</text>
  <!-- Flow Arrow -->
  <line x1="120" y1="46" x2="120" y2="78" stroke="#0284c7" stroke-width="2.2" marker-end="url(#arr_cf)"/>
  <text x="145" y="66" font-size="10.5" font-weight="bold" fill="#0284c7">flow</text>
  <!-- Activity B -->
  <rect x="50" y="82" width="140" height="34" rx="8" fill="#f8fafc" stroke="#475569" stroke-width="1.8"/>
  <text x="120" y="104" font-size="12" font-weight="bold" fill="#334155" text-anchor="middle">Activity B</text>
  <!-- Label -->
  <text x="120" y="132" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Control Flow</text>
</svg>'''

with open(os.path.join(output_dir, "notation_control_flow.svg"), "w", encoding="utf-8") as f:
    f.write(control_flow_svg)

# 4. Decision Node SVG (Diamond with clean guard branches)
decision_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 150" width="240" height="150" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arr_d" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
  </defs>
  <!-- Incoming -->
  <line x1="120" y1="10" x2="120" y2="35" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_d)"/>
  <!-- Diamond -->
  <polygon points="120,40 155,68 120,96 85,68" fill="#fef9c3" stroke="#ca8a04" stroke-width="2"/>
  <text x="120" y="72" font-size="10.5" font-weight="bold" fill="#854d0e" text-anchor="middle">Valid?</text>
  <!-- Down branch [Yes] -->
  <line x1="120" y1="96" x2="120" y2="125" stroke="#16a34a" stroke-width="2.2" marker-end="url(#arr_d)"/>
  <text x="135" y="116" font-size="10" font-weight="bold" fill="#16a34a">[Yes]</text>
  <!-- Right branch [No] -->
  <line x1="155" y1="68" x2="205" y2="68" stroke="#dc2626" stroke-width="2.2" marker-end="url(#arr_d)"/>
  <text x="180" y="60" font-size="10" font-weight="bold" fill="#dc2626" text-anchor="middle">[No]</text>
  <!-- Label -->
  <text x="120" y="144" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Decision Node</text>
</svg>'''

with open(os.path.join(output_dir, "notation_decision.svg"), "w", encoding="utf-8") as f:
    f.write(decision_svg)

# 5. Merge Node SVG (Diamond unifying alternative flows)
merge_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 240 150" width="240" height="150" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arr_m" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
  </defs>
  <!-- Incoming Top -->
  <line x1="120" y1="10" x2="120" y2="38" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_m)"/>
  <!-- Incoming Left Alternative -->
  <line x1="45" y1="68" x2="85" y2="68" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_m)"/>
  <!-- Diamond -->
  <polygon points="120,40 155,68 120,96 85,68" fill="#f1f5f9" stroke="#475569" stroke-width="2"/>
  <text x="120" y="72" font-size="10.5" font-weight="bold" fill="#334155" text-anchor="middle">Merge</text>
  <!-- Unified Outgoing Flow -->
  <line x1="120" y1="96" x2="120" y2="125" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_m)"/>
  <!-- Label -->
  <text x="120" y="144" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Merge Node</text>
</svg>'''

with open(os.path.join(output_dir, "notation_merge.svg"), "w", encoding="utf-8") as f:
    f.write(merge_svg)

# 6. Fork Node SVG (EXACT MATCH to user's uploaded reference image)
fork_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="180" height="180" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arrow_f" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#1e293b"/>
    </marker>
  </defs>
  <!-- Incoming Arrow from Top -->
  <line x1="90" y1="18" x2="90" y2="60" stroke="#1e293b" stroke-width="3" marker-end="url(#arrow_f)"/>
  
  <!-- Thick Horizontal Bar -->
  <rect x="25" y="68" width="130" height="8" rx="2" fill="#0f172a"/>
  
  <!-- Outgoing Parallel Arrows -->
  <line x1="50" y1="76" x2="50" y2="128" stroke="#1e293b" stroke-width="3" marker-end="url(#arrow_f)"/>
  <line x1="130" y1="76" x2="130" y2="128" stroke="#1e293b" stroke-width="3" marker-end="url(#arrow_f)"/>
  
  <!-- Bold Centered Label -->
  <text x="90" y="162" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">Fork</text>
</svg>'''

with open(os.path.join(output_dir, "notation_fork.svg"), "w", encoding="utf-8") as f:
    f.write(fork_svg)

# 7. Join Node SVG (EXACT MATCH to user's uploaded reference image)
join_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 180 180" width="180" height="180" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arrow_j" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#1e293b"/>
    </marker>
  </defs>
  <!-- Two Incoming Angled Arrows -->
  <line x1="45" y1="20" x2="76" y2="62" stroke="#1e293b" stroke-width="3" marker-end="url(#arrow_j)"/>
  <line x1="135" y1="20" x2="104" y2="62" stroke="#1e293b" stroke-width="3" marker-end="url(#arrow_j)"/>
  
  <!-- Thick Horizontal Bar -->
  <rect x="25" y="70" width="130" height="8" rx="2" fill="#0f172a"/>
  
  <!-- Single Outgoing Arrow -->
  <line x1="90" y1="78" x2="90" y2="128" stroke="#1e293b" stroke-width="3" marker-end="url(#arrow_j)"/>
  
  <!-- Bold Centered Label -->
  <text x="90" y="162" font-size="20" font-weight="bold" fill="#0f172a" text-anchor="middle">Join</text>
</svg>'''

with open(os.path.join(output_dir, "notation_join.svg"), "w", encoding="utf-8") as f:
    f.write(join_svg)

# 8. Swimlanes Notation SVG (Spacious, beautifully laid out)
swimlanes_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 160" width="520" height="160" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arr_sl" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0284c7"/>
    </marker>
  </defs>
  <!-- Outer Box -->
  <rect x="15" y="10" width="490" height="115" fill="#f8fafc" stroke="#64748b" stroke-width="1.5"/>
  
  <!-- Dividers -->
  <line x1="137" y1="10" x2="137" y2="125" stroke="#94a3b8" stroke-width="1.2"/>
  <line x1="260" y1="10" x2="260" y2="125" stroke="#94a3b8" stroke-width="1.2"/>
  <line x1="382" y1="10" x2="382" y2="125" stroke="#94a3b8" stroke-width="1.2"/>
  
  <!-- Header Bar -->
  <line x1="15" y1="36" x2="505" y2="36" stroke="#64748b" stroke-width="1.2"/>
  
  <!-- Column Headers -->
  <rect x="15" y="10" width="122" height="26" fill="#e0f2fe"/>
  <text x="76" y="27" font-size="11" font-weight="bold" fill="#0369a1" text-anchor="middle">Operator / Player</text>
  
  <rect x="137" y="10" width="123" height="26" fill="#f1f5f9"/>
  <text x="198" y="27" font-size="11" font-weight="bold" fill="#334155" text-anchor="middle">System Backend</text>
  
  <rect x="260" y="10" width="122" height="26" fill="#fef3c7"/>
  <text x="321" y="27" font-size="11" font-weight="bold" fill="#92400e" text-anchor="middle">Faculty Mentor</text>
  
  <rect x="382" y="10" width="123" height="26" fill="#f3e8ff"/>
  <text x="443" y="27" font-size="11" font-weight="bold" fill="#6b21a8" text-anchor="middle">Harbor HOD</text>
  
  <!-- Example Action Blocks inside Swimlanes -->
  <rect x="25" y="55" width="102" height="30" rx="6" fill="#ffffff" stroke="#0284c7" stroke-width="1.5"/>
  <text x="76" y="74" font-size="9.5" font-weight="bold" fill="#0369a1" text-anchor="middle">Submit Request</text>
  
  <!-- Cross-lane flow -->
  <path d="M 127,70 L 155,70 L 155,90 L 165,90" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arr_sl)"/>
  
  <rect x="165" y="75" width="85" height="30" rx="6" fill="#ffffff" stroke="#475569" stroke-width="1.5"/>
  <text x="207" y="94" font-size="9.5" font-weight="bold" fill="#334155" text-anchor="middle">Pre-Audit Check</text>

  <!-- Cross-lane flow to Faculty -->
  <path d="M 250,90 L 285,90" fill="none" stroke="#0284c7" stroke-width="1.8" marker-end="url(#arr_sl)"/>

  <rect x="285" y="75" width="85" height="30" rx="6" fill="#ffffff" stroke="#d97706" stroke-width="1.5"/>
  <text x="327" y="94" font-size="9.5" font-weight="bold" fill="#92400e" text-anchor="middle">Faculty Review</text>

  <!-- Label -->
  <text x="260" y="148" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Swimlanes (Activity Partitions)</text>
</svg>'''

with open(os.path.join(output_dir, "notation_swimlanes.svg"), "w", encoding="utf-8") as f:
    f.write(swimlanes_svg)

# 9. Activity Final Node SVG
final_svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 160 140" width="160" height="140" style="background:#ffffff; font-family:Arial, sans-serif;">
  <defs>
    <marker id="arr_f" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 1 L 9 5 L 0 9 z" fill="#0f172a"/>
    </marker>
  </defs>
  <!-- Incoming Flow -->
  <line x1="80" y1="12" x2="80" y2="48" stroke="#0f172a" stroke-width="2.2" marker-end="url(#arr_f)"/>
  <!-- Bullseye circle -->
  <circle cx="80" cy="75" r="22" fill="none" stroke="#0f172a" stroke-width="2.5"/>
  <circle cx="80" cy="75" r="14" fill="#0f172a"/>
  <!-- Label -->
  <text x="80" y="125" font-size="13" font-weight="bold" fill="#0f172a" text-anchor="middle">Activity Final</text>
</svg>'''

with open(os.path.join(output_dir, "notation_final.svg"), "w", encoding="utf-8") as f:
    f.write(final_svg)

print("Redesigned notation SVGs successfully generated!")
