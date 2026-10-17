with open('Activity_Diagram_New.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('Activity_Diagram.html', 'w', encoding='utf-8') as f:
    f.write(content)

marker = 'id="spacious-diagram"'
pos = content.find(marker)
start_pos = content.rfind('<svg', 0, pos)
end_pos = content.rfind('</svg>') + 6
svg_code = content[start_pos:end_pos]

style_start = content.find('<style>') + 7
style_end = content.find('</style>')
styles = content[style_start:style_end]

svg_with_style = svg_code.replace('<defs>', f'<defs><style>{styles}</style>')

with open('activity_diagram.svg', 'w', encoding='utf-8') as f:
    f.write(svg_with_style)

print('Updated Activity_Diagram.html and activity_diagram.svg successfully')
