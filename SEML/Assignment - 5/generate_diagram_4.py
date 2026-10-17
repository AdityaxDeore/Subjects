import json

lifelines = [
    {"name": "Player", "x": 150, "is_actor": True},
    {"name": ":Game UI", "x": 410, "is_actor": False},
    {"name": ":Game", "x": 670, "is_actor": False},
    {"name": ":Boat", "x": 930, "is_actor": False},
    {"name": ":Ocean", "x": 1190, "is_actor": False},
    {"name": ":Waste", "x": 1450, "is_actor": False},
    {"name": ":Marine Life", "x": 1710, "is_actor": False},
    {"name": ":Database", "x": 1970, "is_actor": False}
]

def get_x(name):
    for l in lifelines:
        if name in l["name"] or (name == "Player" and l["name"] == "Player"):
            return l["x"]
    return 0

svg_elements = []

y = 150
y_step = 50

def add_msg(sender, receiver, text, is_return=False, self_msg=False):
    global y
    sx = get_x(sender)
    rx = get_x(receiver)
    
    if self_msg:
        svg_elements.append(f'<!-- {sender} -> {sender} : {text} -->')
        svg_elements.append(f'<polyline points="{sx},{y} {sx+35},{y} {sx+35},{y+25} {sx},{y+25}" fill="none" stroke="#333" stroke-width="1.5" marker-end="url(#arrow_sync)"/>')
        svg_elements.append(f'<text x="{sx+40}" y="{y+15}" class="msg-text" text-anchor="start">{text}</text>')
        y += y_step
    else:
        svg_elements.append(f'<!-- {sender} -> {receiver} : {text} -->')
        if not is_return:
            svg_elements.append(f'<line x1="{sx}" y1="{y}" x2="{rx}" y2="{y}" class="msg-line" marker-end="url(#arrow_sync)"/>')
        else:
            svg_elements.append(f'<line x1="{sx}" y1="{y}" x2="{rx}" y2="{y}" class="msg-return" marker-end="url(#arrow_return)"/>')
        
        mid_x = (sx + rx) / 2
        text_y = y - 8
        svg_elements.append(f'<text x="{mid_x}" y="{text_y}" text-anchor="middle" class="msg-text">{text}</text>')
        y += y_step

def start_fragment(frag_type, condition, width, height, start_y, left_x):
    svg_elements.append(f'<!-- Fragment: {frag_type} [{condition}] -->')
    svg_elements.append(f'<rect x="{left_x}" y="{start_y}" width="{width}" height="{height}" class="frag-box" />')
    svg_elements.append(f'<path d="M {left_x},{start_y} L {left_x+60},{start_y} L {left_x+70},{start_y+15} L {left_x},{start_y+15} Z" class="frag-tab" />')
    svg_elements.append(f'<text x="{left_x+5}" y="{start_y+12}" class="frag-text">{frag_type}</text>')
    if condition:
        svg_elements.append(f'<text x="{left_x+80}" y="{start_y+12}" class="frag-cond">[{condition}]</text>')

def add_divider(condition, start_y, left_x, width):
    svg_elements.append(f'<line x1="{left_x}" y1="{start_y}" x2="{left_x+width}" y2="{start_y}" stroke="#333" stroke-width="1.5" stroke-dasharray="4 4" />')
    if condition:
        svg_elements.append(f'<text x="{left_x+10}" y="{start_y+20}" class="frag-cond">[{condition}]</text>')

def generate_html():
    global y
    html_top = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Part 4 — Start Game & Ocean Exploration - Sequence Diagram</title>
    <script src="https://unpkg.com/@panzoom/panzoom@4.5.1/dist/panzoom.min.js"></script>
    <style>
        body, html { margin: 0; padding: 0; width: 100vw; height: 100vh; overflow: hidden; font-family: "Segoe UI", Arial, sans-serif; background-color: #ffffff; }
        .grid-bg { background-image: linear-gradient(to right, #f3f3f3 1px, transparent 1px), linear-gradient(to bottom, #f3f3f3 1px, transparent 1px); background-size: 20px 20px; width: 100%; height: 100%; position: absolute; top: 0; left: 0; display: flex; justify-content: center; align-items: center; }
        .diagram { width: 100%; height: 100%; position: relative; }
        text { user-select: none; font-family: "Arial", sans-serif; }
        .obj-box { fill: #ffffff; stroke: #333; stroke-width: 1.5; }
        .lifeline { stroke: #333; stroke-width: 1.5; stroke-dasharray: 6 6; }
        .activation { fill: #ffffff; stroke: #333; stroke-width: 1.5; }
        .msg-line { stroke: #333; stroke-width: 1.5; }
        .msg-return { stroke: #333; stroke-width: 1.5; stroke-dasharray: 6 6; }
        .msg-text { font-size: 13px; fill: #111; }
        .obj-text { font-size: 14px; font-weight: bold; fill: #111; }
        .frag-box { fill: none; stroke: #333; stroke-width: 1.5; }
        .frag-tab { fill: #ffffff; stroke: #333; stroke-width: 1.5; }
        .frag-text { font-size: 12px; font-weight: bold; fill: #111; }
        .frag-cond { font-size: 12px; fill: #111; font-weight: bold; }
        .diag-header { font-size: 18px; font-weight: bold; fill: #222; }
    </style>
</head>
<body>
    <div class="grid-bg" id="seq-diagram">
        <div class="diagram" style="width: 2200px; height: 6800px;" id="pan-seq">
            <svg width="100%" height="100%" viewBox="0 0 2200 6800" xmlns="http://www.w3.org/2000/svg" style="background-color: white;">
                <style>
                    text { user-select: none; font-family: "Arial", sans-serif; }
                    .obj-box { fill: #ffffff; stroke: #333; stroke-width: 1.5; }
                    .lifeline { stroke: #333; stroke-width: 1.5; stroke-dasharray: 6 6; }
                    .activation { fill: #ffffff; stroke: #333; stroke-width: 1.5; }
                    .msg-line { stroke: #333; stroke-width: 1.5; }
                    .msg-return { stroke: #333; stroke-width: 1.5; stroke-dasharray: 6 6; }
                    .msg-text { font-size: 13px; fill: #111; }
                    .obj-text { font-size: 14px; font-weight: bold; fill: #111; }
                    .frag-box { fill: none; stroke: #333; stroke-width: 1.5; }
                    .frag-tab { fill: #ffffff; stroke: #333; stroke-width: 1.5; }
                    .frag-text { font-size: 12px; font-weight: bold; fill: #111; }
                    .frag-cond { font-size: 12px; fill: #111; font-weight: bold; }
                    .diag-header { font-size: 18px; font-weight: bold; fill: #222; }
                </style>
                <defs>
                  <marker id="arrow_sync" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" orient="auto">
                    <path d="M 0 0 L 10 5 L 0 10 Z" fill="#222" />
                  </marker>
                  <marker id="arrow_return" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" markerHeight="10" orient="auto">
                    <path d="M 0 2 L 10 5 L 0 8" fill="none" stroke="#222" stroke-width="1.5"/>
                  </marker>
                </defs>

                <!-- Diagram Title -->
                <text x="40" y="45" class="diag-header">Part 4 — Start Game &amp; Ocean Exploration</text>
"""
    
    # Draw Lifelines
    for l in lifelines:
        lx = l["x"]
        svg_elements.append(f'<line x1="{lx}" y1="140" x2="{lx}" y2="6660" class="lifeline"/>')
        
        # Top header
        if l["is_actor"]:
            svg_elements.append(f'<circle cx="{lx}" cy="70" r="8" fill="none" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx}" y1="78" x2="{lx}" y2="95" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx-12}" y1="85" x2="{lx+12}" y2="85" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx}" y1="95" x2="{lx-10}" y2="108" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx}" y1="95" x2="{lx+10}" y2="108" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<text x="{lx}" y="125" text-anchor="middle" class="obj-text">{l["name"]}</text>')
        else:
            svg_elements.append(f'<rect x="{lx-80}" y="80" width="160" height="40" class="obj-box" />')
            svg_elements.append(f'<text x="{lx}" y="105" text-anchor="middle" class="obj-text">{l["name"]}</text>')

        # Bottom header
        if l["is_actor"]:
            svg_elements.append(f'<circle cx="{lx}" cy="6670" r="8" fill="none" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx}" y1="6678" x2="{lx}" y2="6695" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx-12}" y1="6685" x2="{lx+12}" y2="6685" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx}" y1="6695" x2="{lx-10}" y2="6708" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<line x1="{lx}" y1="6695" x2="{lx+10}" y2="6708" stroke="#222" stroke-width="1.5"/>')
            svg_elements.append(f'<text x="{lx}" y="6725" text-anchor="middle" class="obj-text">{l["name"]}</text>')
        else:
            svg_elements.append(f'<rect x="{lx-80}" y="6680" width="160" height="40" class="obj-box" />')
            svg_elements.append(f'<text x="{lx}" y="6705" text-anchor="middle" class="obj-text">{l["name"]}</text>')

    # PART A
    add_msg("Player", "Game UI", "clickStartGame()")
    add_msg("Game UI", "Game", "startGame(playerId)")
    add_msg("Game", "Database", "loadPlayerData(playerId)")
    add_msg("Database", "Game", "playerData", is_return=True)
    add_msg("Game", "Game", "initializeGameState()", self_msg=True)
    add_msg("Game", "Database", "loadPlayerProgress(playerId)")
    add_msg("Database", "Game", "playerProgress", is_return=True)
    add_msg("Game", "Boat", "getCurrentBoat(playerId)")
    add_msg("Boat", "Database", "fetchBoatData(playerId)")
    add_msg("Database", "Boat", "boatData", is_return=True)
    add_msg("Boat", "Game", "currentBoat", is_return=True)
    add_msg("Game", "Game UI", "gameInitialized()", is_return=True)
    add_msg("Game UI", "Player", "displayGameMap()", is_return=True)

    y += 20
    start_y = y - 20
    add_msg("Game", "Game UI", "showTutorial()")
    add_msg("Game UI", "Player", "displayControlsAndObjectives()", is_return=True)
    add_msg("Player", "Game UI", "closeTutorial()")
    start_fragment("opt", "First time player", 700, y - start_y, start_y, 80)
    
    y += 40

    # PART B
    add_msg("Player", "Game UI", "selectExploreOcean()")
    add_msg("Game UI", "Ocean", "loadExplorationZones()")
    add_msg("Ocean", "Database", "fetchAvailableZones(playerId)")
    add_msg("Database", "Ocean", "zoneList", is_return=True)
    add_msg("Ocean", "Ocean", "filterUnlockedZones()", self_msg=True)
    add_msg("Ocean", "Game UI", "availableZones", is_return=True)
    add_msg("Game UI", "Player", "displayOceanZones()", is_return=True)
    add_msg("Player", "Game UI", "selectZone(zoneId)")
    add_msg("Game UI", "Ocean", "loadZone(zoneId)")
    add_msg("Ocean", "Database", "fetchZoneDetails(zoneId)")
    add_msg("Database", "Ocean", "zoneDetails", is_return=True)
    add_msg("Ocean", "Ocean", "validateZoneAccess()", self_msg=True)

    y += 20
    start_y = y - 20
    add_msg("Ocean", "Ocean", "initializeZone()", self_msg=True)
    add_msg("Ocean", "Game UI", "zoneLoaded()", is_return=True)
    add_msg("Game UI", "Player", "displayZoneDetails()", is_return=True)
    
    div_y = y + 10
    add_divider("Zone locked", div_y, 80, 1200)
    y += 40
    
    add_msg("Ocean", "Game UI", "zoneLocked()", is_return=True)
    add_msg("Game UI", "Player", "displayLockedZoneMessage()", is_return=True)
    start_fragment("alt", "Zone unlocked", 1200, y - start_y, start_y, 80)

    y += 40

    # PART C
    add_msg("Player", "Game UI", "launchBoat()")
    add_msg("Game UI", "Boat", "prepareForLaunch()")
    add_msg("Boat", "Database", "checkBoatStatus(playerId)")
    add_msg("Database", "Boat", "boatStatus", is_return=True)
    add_msg("Boat", "Boat", "validateBoatCondition()", self_msg=True)

    y += 20
    start_y = y - 20
    add_msg("Boat", "Game UI", "launchApproved()", is_return=True)
    add_msg("Game UI", "Player", "startOceanJourney()", is_return=True)
    add_msg("Game UI", "Boat", "moveToOcean()")
    add_msg("Boat", "Ocean", "enterZone(zoneId)")
    add_msg("Ocean", "Boat", "zoneEntryConfirmed()", is_return=True)
    add_msg("Boat", "Game UI", "boatReadyForExploration()", is_return=True)
    add_msg("Game UI", "Player", "displayExplorationView()", is_return=True)

    div_y = y + 10
    add_divider("Boat requires repair", div_y, 80, 1200)
    y += 40

    add_msg("Boat", "Game UI", "launchRejected()", is_return=True)
    add_msg("Game UI", "Player", "showBoatRepairMessage()", is_return=True)
    start_fragment("alt", "Boat ready", 1200, y - start_y, start_y, 80)
    
    y += 40

    # PART D Loop
    loop_start_y = y - 20
    add_msg("Player", "Game UI", "controlBoat(input)")
    add_msg("Game UI", "Boat", "processMovement(input)")
    add_msg("Boat", "Boat", "updatePosition()", self_msg=True)
    add_msg("Boat", "Ocean", "updateBoatPosition(position)")
    add_msg("Ocean", "Ocean", "detectNearbyObjects()", self_msg=True)
    add_msg("Ocean", "Game UI", "environmentUpdate()", is_return=True)
    add_msg("Game UI", "Player", "displayOceanEnvironment()", is_return=True)

    # Nested ALT
    y += 20
    alt_start_y = y - 20
    
    # Waste detected
    add_msg("Ocean", "Waste", "detectWaste()")
    add_msg("Waste", "Ocean", "wasteLocation", is_return=True)
    add_msg("Ocean", "Game UI", "displayWasteTarget()", is_return=True)
    add_msg("Player", "Game UI", "collectWaste(wasteId)")
    add_msg("Game UI", "Waste", "collect()")
    add_msg("Waste", "Database", "updateWasteStatus(wasteId)")
    add_msg("Database", "Waste", "wasteCollected", is_return=True)
    add_msg("Waste", "Game UI", "collectionConfirmed()", is_return=True)
    add_msg("Game", "Game", "updateScore()", self_msg=True)
    add_msg("Game", "Game UI", "scoreUpdated()", is_return=True)

    div_y = y + 10
    add_divider("Marine life detected", div_y, 100, 1920)
    y += 40

    # Marine life
    add_msg("Ocean", "Marine Life", "detectMarineLife()")
    add_msg("Marine Life", "Ocean", "marineLifeStatus", is_return=True)
    add_msg("Ocean", "Game UI", "displayMarineLife()", is_return=True)
    add_msg("Player", "Game UI", "rescueMarineLife(lifeId)")
    add_msg("Game UI", "Marine Life", "rescue()")
    add_msg("Marine Life", "Database", "updateHealthStatus()")
    add_msg("Database", "Marine Life", "healthUpdated()", is_return=True)
    add_msg("Marine Life", "Game UI", "rescueSuccessful()", is_return=True)
    add_msg("Game", "Game", "updateScore()", self_msg=True)
    add_msg("Game", "Game UI", "scoreUpdated()", is_return=True)

    div_y = y + 10
    add_divider("Obstacle detected", div_y, 100, 1920)
    y += 40

    # Obstacle
    add_msg("Ocean", "Boat", "detectObstacle()")
    add_msg("Boat", "Boat", "avoidObstacle()", self_msg=True)
    add_msg("Boat", "Game UI", "obstacleAvoided()", is_return=True)
    add_msg("Game UI", "Player", "displayObstacleWarning()", is_return=True)

    div_y = y + 10
    add_divider("Nothing detected", div_y, 100, 1920)
    y += 40

    # Nothing
    add_msg("Ocean", "Game UI", "continueExploration()", is_return=True)
    add_msg("Game UI", "Player", "continueJourney()", is_return=True)

    start_fragment("alt", "Waste detected", 1920, y - alt_start_y, alt_start_y, 100)
    
    y += 20
    start_fragment("loop", "While player continues exploring", 1960, y - loop_start_y, loop_start_y, 80)
    
    y += 60

    # PART E
    opt_start_1 = y - 20
    add_msg("Boat", "Boat", "checkDurability()", self_msg=True)
    add_msg("Boat", "Game UI", "durabilityWarning()", is_return=True)
    add_msg("Game UI", "Player", "displayLowDurabilityWarning()", is_return=True)
    start_fragment("opt", "Boat durability below threshold", 1000, y - opt_start_1, opt_start_1, 80)

    y += 40

    opt_start_2 = y - 20
    add_msg("Boat", "Game UI", "capacityReached()", is_return=True)
    add_msg("Game UI", "Player", "showReturnToBaseMessage()", is_return=True)
    start_fragment("opt", "Boat capacity full", 1000, y - opt_start_2, opt_start_2, 80)

    y += 60

    # PART F
    add_msg("Player", "Game UI", "endExploration()")
    add_msg("Game UI", "Ocean", "completeExploration()")
    add_msg("Ocean", "Ocean", "calculateZoneCleanup()", self_msg=True)
    add_msg("Ocean", "Database", "saveExplorationProgress(playerId,zoneId)")
    add_msg("Database", "Ocean", "progressSaved()", is_return=True)
    add_msg("Ocean", "Game UI", "explorationCompleted()", is_return=True)
    add_msg("Game UI", "Player", "displayExplorationSummary()", is_return=True)

    y += 20
    alt_start_f = y - 20
    add_msg("Game", "Game", "calculateFinalScore()", self_msg=True)
    add_msg("Game", "Database", "saveGameScore(playerId)")
    add_msg("Database", "Game", "scoreSaved()", is_return=True)
    add_msg("Game", "Game UI", "objectivesCompleted()", is_return=True)
    add_msg("Game UI", "Player", "displayZoneCompletion()", is_return=True)

    div_y = y + 10
    add_divider("Objectives incomplete", div_y, 80, 1920)
    y += 40

    add_msg("Game", "Game UI", "objectivesIncomplete()", is_return=True)
    add_msg("Game UI", "Player", "displayRemainingObjectives()", is_return=True)
    start_fragment("alt", "Zone objectives completed", 1920, y - alt_start_f, alt_start_f, 80)

    y += 60

    # PART G
    add_msg("Player", "Game UI", "returnToBase()")
    add_msg("Game UI", "Boat", "returnToPort()")
    add_msg("Boat", "Ocean", "exitExplorationZone()")
    add_msg("Ocean", "Boat", "routeCleared()", is_return=True)
    add_msg("Boat", "Boat", "navigateToPort()", self_msg=True)
    add_msg("Boat", "Game UI", "arrivedAtPort()", is_return=True)
    add_msg("Game UI", "Player", "displayHomeBase()", is_return=True)

    add_msg("Game UI", "Game", "saveGameSession()")
    add_msg("Game", "Database", "savePlayerSession(playerId)")
    add_msg("Database", "Game", "sessionSaved()", is_return=True)
    add_msg("Game", "Game UI", "sessionSaveComplete()", is_return=True)
    add_msg("Game UI", "Player", "explorationSummary()", is_return=True)

    # HTML Bottom
    html_bottom = """
            </svg>
        </div>
    </div>
    <button id="download-svg-btn" style="position: fixed; bottom: 20px; right: 20px; padding: 10px 20px; background-color: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; font-family: sans-serif; font-size: 14px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); z-index: 1000;">Download SVG</button>
    <script>
        document.addEventListener("DOMContentLoaded", function() {
            const wrapper = document.getElementById('seq-diagram');
            const p = Panzoom(document.getElementById('pan-seq'), { maxScale: 3, minScale: 0.1, step: 0.1 });
            
            wrapper.addEventListener('wheel', p.zoomWithWheel, { passive: false });

            p.zoom(0.40);
            p.pan(0, 0);

            // Download SVG functionality
            document.getElementById('download-svg-btn').addEventListener('click', function() {
                const svgElement = document.querySelector('svg');
                const serializer = new XMLSerializer();
                let source = serializer.serializeToString(svgElement);
                // Ensure SVG namespace is present
                if(!source.match(/^<svg[^>]+xmlns="http\:\/\/www\.w3\.org\/2000\/svg"/)){
                    source = source.replace(/^<svg/, '<svg xmlns="http://www.w3.org/2000/svg"');
                }
                const svgBlob = new Blob(['<?xml version="1.0" standalone="no"?>\\r\\n' + source], {type: 'image/svg+xml;charset=utf-8'});
                const url = URL.createObjectURL(svgBlob);
                const link = document.createElement('a');
                link.href = url;
                link.download = 'Start_Game_Sequence.svg';
                document.body.appendChild(link);
                link.click();
                document.body.removeChild(link);
            });
        });
    </script>
</body>
</html>
"""
    
    with open("c:/Users/adity/Desktop/Subjects/SEML/Assignment - 5/Start_Game_Sequence.html", "w", encoding='utf-8') as f:
        f.write(html_top)
        f.write("\n".join(svg_elements))
        f.write(html_bottom)

generate_html()
