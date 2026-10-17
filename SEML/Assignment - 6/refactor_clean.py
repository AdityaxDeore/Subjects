import re

def main():
    with open('generate_activity_diagram.py', 'r', encoding='utf-8') as f:
        code = f.read()

    # 1. Update body styling to clean pure white
    code = re.sub(
        r'body,\s*html\s*\{[^}]*background-color:\s*#[0-9a-fA-F]+;[^}]*\}',
        '''body, html { 
            width: 100vw; 
            height: 100vh; 
            margin: 0;
            padding: 0;
            overflow: hidden; 
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; 
            background-color: #ffffff; 
            color: #0f172a; 
        }''',
        code
    )

    # 2. Replace CSS from toolbar up to UML elements with clean white full-screen canvas
    start_css = code.find('/* Modern Floating Pill Toolbar */')
    end_css = code.find('/* Refined UML Diagram Elements */')
    if start_css != -1 and end_css != -1:
        clean_css = '''/* Clean Full Screen White Canvas */
        .canvas-container {
            width: 100vw;
            height: 100vh;
            position: absolute;
            top: 0;
            left: 0;
            background-color: #ffffff;
            overflow: hidden;
            display: flex;
            justify-content: center;
            align-items: center;
            cursor: grab;
        }
        .canvas-container:active {
            cursor: grabbing;
        }

        #pan-area {
            transform-origin: 0 0;
        }

        svg {
            display: block;
            user-select: none;
            background: #ffffff;
        }

        '''
        code = code[:start_css] + clean_css + code[end_css:]

    # 3. Remove toolbar and legend HTML elements in body
    body_idx = code.find('<body>')
    canvas_idx = code.find('<div class="canvas-container"')
    if body_idx != -1 and canvas_idx != -1:
        code = code[:body_idx + len('<body>')] + '\n\n    <!-- Clean Full Screen Panzoom Canvas -->\n    ' + code[canvas_idx:]

    # 4. Clean JS script - remove button listeners and export logic, keep smooth panzoom
    js_start = code.find('// Button actions')
    js_end = code.find('});\n        });\n    </script>')
    if js_start != -1 and js_end != -1:
        clean_js = '''// Double-click to reset view
            wrapper.addEventListener("dblclick", function() {
                panzoom.zoom(0.48);
                panzoom.pan(80, 20);
            });
        '''
        code = code[:js_start] + clean_js + code[js_end:]

    with open('generate_activity_diagram.py', 'w', encoding='utf-8') as f:
        f.write(code)

    print("Refactored generate_activity_diagram.py cleanly.")

if __name__ == '__main__':
    main()
