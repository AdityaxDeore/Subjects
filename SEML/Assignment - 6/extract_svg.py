with open('Activity_Diagram.html', 'r', encoding='utf-8') as f:
    content = f.read()

marker = 'id="activity-diagram-svg"'
pos = content.find(marker)
start_pos = content.rfind('<svg', 0, pos)
end_pos = content.rfind('</svg>') + 6

svg_code = content[start_pos:end_pos]

# Extract styles used by svg
style_start = content.find('<style>') + 7
style_end = content.find('</style>')
styles = content[style_start:style_end]

# Inject styles into SVG so it can render standalone in <img> or <object>
svg_with_style = svg_code.replace('<defs>', f'<defs><style>{styles}</style>')

with open('activity_diagram.svg', 'w', encoding='utf-8') as f:
    f.write(svg_with_style)

print(f"Successfully wrote activity_diagram.svg with {len(svg_with_style)} characters.")
