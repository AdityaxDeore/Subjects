import os

def build_files():
    base_dir = "C:/Users/adity/Desktop/Subjects/AIML"
    
    # ---------------------------------------------------------
    # HTML 1: Main Assignment (Theory & Algorithm)
    # ---------------------------------------------------------
    html_1 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIML Assignment No. 1</title>
    <style>
        body {{
            font-family: Calibri, "Segoe UI", Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.5;
            color: #1a1a1a;
            background: #e5e7eb;
            padding: 20px;
        }}
        .container {{
            max-width: 8.5in;
            margin: 0 auto;
        }}
        .page {{
            min-height: 11in;
            width: 8.5in;
            padding: 0.8in;
            background: #ffffff;
            margin: 0 auto 20px auto;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border-radius: 4px;
            position: relative;
            box-sizing: border-box;
        }}
        @media print {{
            body {{ background: #ffffff; padding: 0; }}
            .container {{ max-width: 100%; margin: 0; box-shadow: none; }}
            .page {{ width: 100%; min-height: auto; margin: 0; padding: 0.2in; box-shadow: none; border: none; border-radius: 0; page-break-after: always; }}
        }}
        .cover-table {{
            width: 100%; border-collapse: collapse; margin-bottom: 20px; font-family: "Times New Roman", Times, serif;
        }}
        .cover-table td {{ border: 1px solid #000; padding: 8px 10px; }}
        .cover-table .college-info {{ text-align: center; font-weight: bold; font-size: 16pt; line-height: 1.4; color: #000; }}
        .cover-table .row-centered {{ text-align: center; font-weight: bold; font-size: 13pt; color: #000; }}
        .cover-table .row-left {{ text-align: left; font-weight: bold; font-size: 13pt; color: #000; }}
        .logo-container {{ text-align: center; width: 18%; padding: 5px !important; }}
        .logo-container img {{ max-width: 90px; height: auto; display: block; margin: 0 auto; }}

        h2 {{ font-family: "Times New Roman", Times, serif; font-weight: bold; font-size: 18pt; color: #1e3a8a; margin-top: 32px; margin-bottom: 12px; border-bottom: 1.5px solid #bfdbfe; padding-bottom: 6px; }}
        h3 {{ font-family: "Times New Roman", Times, serif; font-weight: bold; font-size: 15pt; color: #000; margin-top: 28px; margin-bottom: 8px; }}
        h4 {{ font-family: Calibri, sans-serif; font-weight: bold; font-size: 13pt; color: #000; margin-top: 18px; margin-bottom: 6px; }}
        p {{ font-size: 12pt; text-align: justify; margin-bottom: 12px; color: #1a1a1a; }}
        ul, ol {{ margin-left: 20px; font-size: 12pt; margin-bottom: 12px; color: #1a1a1a; }}
        li {{ margin-bottom: 6px; text-align: justify; }}
    </style>
</head>
<body>
    <div class="container" contenteditable="true">
        <!-- PAGE 1: Cover & Intro -->
        <div class="page">
            <table class="cover-table">
                <tr>
                    <td class="logo-container"><img src="pccoelogo.jfif" /></td>
                    <td class="college-info">Pimpri Chinchwad Education Trust's<br>Pimpri Chinchwad College of Engineering</td>
                </tr>
                <tr><td colspan="2" class="row-centered">Assignment No. 1</td></tr>
                <tr><td colspan="2" class="row-left">Course:- Artificial Intelligence and Machine Learning</td></tr>
                <tr><td colspan="2" class="row-left">Name:- Aditya Chandrajit Deore</td></tr>
                <tr><td colspan="2" class="row-left">PRN:- 124B1F116</td></tr>
                <tr><td colspan="2" class="row-left">Batch:- B3</td></tr>
            </table>

            <p style="margin-top: 20px;"><strong>Aim:</strong> To implement an Informed Search algorithm for solving a real-world route optimization problem using the A* (A-star) search algorithm.</p>
            
            <h2>Problem Statement</h2>
            <p>In a large road network, finding a suitable route between two cities can require searching through a large number of possible connections. An efficient search strategy is therefore required to avoid exploring unnecessary routes.</p>
            <p>The objective of this experiment is to find a distance-efficient route between a selected source city and a destination city using the A* Informed Search algorithm. The road network is represented as a graph in which cities are treated as nodes and available road connections are treated as edges. The road distance between cities is used as the edge cost, while the estimated straight-line distance from the current city to the destination is used as the heuristic.</p>
            <p>For this experiment, <strong>Pune</strong> is considered as the source and <strong>Sissu</strong> is considered as the destination.</p>

            <h2>Objectives</h2>
            <ul>
                <li>To understand the concept of informed search.</li>
                <li>To study the working of the A* search algorithm.</li>
                <li>To represent a real-world route network as a graph.</li>
                <li>To design a suitable heuristic for A* based on straight-line distances.</li>
                <li>To implement A* using a priority queue in Python.</li>
                <li>To determine a distance-efficient route between two cities.</li>
            </ul>
        </div>

        <!-- PAGE 2: Theory -->
        <div class="page">
            <h2>Theory</h2>
            <h3>1. Artificial Intelligence and Search Problems</h3>
            <p>Artificial Intelligence often requires an agent to determine a sequence of actions that leads from an initial state to a desired goal state. Such problems can be represented as search problems. A search problem generally consists of:</p>
            <ul>
                <li><strong>Initial state</strong> – the state from which the search begins.</li>
                <li><strong>Goal state</strong> – the desired final state.</li>
                <li><strong>Actions</strong> – possible transitions from one state to another.</li>
                <li><strong>State space</strong> – all possible states that can be reached.</li>
                <li><strong>Path cost</strong> – the cost associated with following a particular sequence of actions.</li>
            </ul>
            <p>In this experiment, the cities form the states and the road connections form the possible transitions.</p>
            
            <h3>2. Informed Search</h3>
            <p>Informed search algorithms use additional knowledge about the problem to guide the search toward the goal. This additional information is represented using a heuristic function. Unlike uninformed search methods, which explore the search space without knowing which direction is more promising, informed search attempts to estimate how close a state is to the goal. For this experiment, A* is selected because it combines the cost already incurred with an estimate of the remaining cost.</p>

            <h3>3. A* Search Algorithm</h3>
            <p>A* is a widely used informed search algorithm for finding a least-cost path between a starting node and a goal node in a weighted graph. The main idea behind A* is to evaluate each node using two types of information:</p>
            <ul>
                <li>The cost required to reach the current node.</li>
                <li>An estimate of the cost required to reach the goal.</li>
            </ul>
            <p>These values are combined using the evaluation function: <strong>f(n) = g(n) + h(n)</strong></p>
            <p>where:</p>
            <ul>
                <li><strong>g(n)</strong> = actual cost from the starting node to node n.</li>
                <li><strong>h(n)</strong> = estimated cost from node n to the goal.</li>
                <li><strong>f(n)</strong> = estimated total cost of a solution passing through node n.</li>
            </ul>
            <p>A* always gives preference to the node having the smallest estimated total cost.</p>
        </div>

        <!-- PAGE 3: Theory Contd & Implementation -->
        <div class="page">
            <h3>4. Optimality of A* and Heuristics</h3>
            <p>A* can produce an optimal least-cost path when the heuristic is admissible. An admissible heuristic does not overestimate the actual minimum cost required to reach the goal. In this experiment, the straight-line distance provides a direct geographical lower-bound estimate of the remaining distance. Therefore, it provides a useful distance-based heuristic for guiding the search.</p>
            
            <h2>Dataset Description</h2>
            <p>The dataset used for this experiment consists of two local CSV files:</p>
            <ul>
                <li><strong>cities.csv (Heuristics Data):</strong> Contains the names of 30 unique cities and their corresponding heuristic value (estimated straight-line distance to Sissu).</li>
                <li><strong>connections.csv (Road Network):</strong> Contains 43 road connections (edges) indicating the source city, destination city, and the actual driving distance in km.</li>
            </ul>

            <h2>Problem Formulation</h2>
            <p>The route problem was converted into a graph-search problem.</p>
            <ul>
                <li><strong>State:</strong> Each city is treated as a state.</li>
                <li><strong>Initial State:</strong> The search starts at Pune.</li>
                <li><strong>Goal State:</strong> The search terminates at Sissu.</li>
                <li><strong>Successor Function:</strong> The successor states of a city are the cities directly connected to it by a road route in the dataset.</li>
                <li><strong>Edge Cost:</strong> The driving distance between two connected cities.</li>
                <li><strong>Heuristic h(n):</strong> The estimated straight-line distance between the current city and Sissu.</li>
            </ul>

            <h2>Algorithm Steps</h2>
            <ol>
                <li>Create an empty priority queue.</li>
                <li>Insert the source city into the priority queue with path cost g(n) = 0.</li>
                <li>Calculate f(n) = g(n) + h(n).</li>
                <li>Remove the city with the minimum f-value.</li>
                <li>Check whether it is the destination. If so, reconstruct the path and terminate.</li>
                <li>Otherwise, obtain all connected neighbouring cities.</li>
                <li>Calculate the new path cost for each neighbour. If cheaper than its previously recorded path, update its cost.</li>
                <li>Calculate the neighbour's heuristic and f-value, and add it to the priority queue.</li>
                <li>Continue until the destination is reached.</li>
            </ol>
            
            <h2 style="border-bottom: 1.5px solid #bfdbfe; margin-top: 40px; color: #1e3a8a;">Conclusion</h2>
            <p>This experiment successfully demonstrated the use of A* Informed Search for solving a real-world route optimization problem. The road network was modelled as a weighted graph, where cities represented nodes and available road connections represented edges. Straight-line distances were used as the heuristic for guiding the search. For the selected Pune to Sissu problem, A* successfully balanced the distance already travelled with the estimated distance to the destination, arriving at the optimal path of 2215 km spanning 14 total nodes.</p>
        </div>
    </div>
</body>
</html>"""

    # ---------------------------------------------------------
    # HTML 2: Output & AI Usage
    # ---------------------------------------------------------
    html_2 = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AIML Assignment No. 1 - Output</title>
    <style>
        body {{
            font-family: Calibri, "Segoe UI", Arial, sans-serif;
            font-size: 12pt;
            line-height: 1.5;
            color: #1a1a1a;
            background: #e5e7eb;
            padding: 20px;
        }}
        .container {{
            max-width: 8.5in;
            margin: 0 auto;
        }}
        .page {{
            min-height: 11in;
            width: 8.5in;
            padding: 0.8in;
            background: #ffffff;
            margin: 0 auto 20px auto;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border-radius: 4px;
            position: relative;
            box-sizing: border-box;
        }}
        @media print {{
            body {{ background: #ffffff; padding: 0; }}
            .container {{ max-width: 100%; margin: 0; box-shadow: none; }}
            .page {{ width: 100%; min-height: auto; margin: 0; padding: 0.2in; box-shadow: none; border: none; border-radius: 0; page-break-after: always; }}
        }}
        h2 {{ font-family: "Times New Roman", Times, serif; font-weight: bold; font-size: 18pt; color: #1e3a8a; margin-top: 32px; margin-bottom: 12px; border-bottom: 1.5px solid #bfdbfe; padding-bottom: 6px; }}
        
        .terminal {{
            background-color: #1e1e1e;
            color: #d4d4d4;
            border-radius: 8px;
            margin: 15px 0;
            overflow: hidden;
            box-shadow: 0 4px 10px rgba(0,0,0,0.3);
            font-family: Consolas, "Courier New", monospace;
            font-size: 10pt;
        }}
        .terminal-header {{
            background-color: #333333;
            padding: 8px 15px;
            display: flex;
            align-items: center;
        }}
        .terminal-header-dots {{ display: flex; gap: 6px; }}
        .dot {{ width: 12px; height: 12px; border-radius: 50%; }}
        .dot-red {{ background-color: #ff5f56; }}
        .dot-yellow {{ background-color: #ffbd2e; }}
        .dot-green {{ background-color: #27c93f; }}
        .terminal-header-title {{ color: #999999; font-size: 10pt; margin-left: auto; margin-right: auto; font-family: sans-serif; }}
        .terminal-body {{ padding: 15px; white-space: pre-wrap; line-height: 1.4; }}
        .terminal-command {{ color: #569cd6; font-weight: bold; }}

        .image-box {{ text-align: center; margin: 20px 0; }}
        .image-box img {{ max-width: 100%; height: auto; border: 1px solid #ccc; border-radius: 4px; box-shadow: 0 2px 6px rgba(0,0,0,0.1); }}
        .image-caption {{ font-size: 10.5pt; color: #475569; font-family: "Times New Roman", Times, serif; font-style: italic; margin-top: 10px; }}
        
        table.ai-table {{ width: 100%; border-collapse: collapse; margin-top: 15px; }}
        table.ai-table th, table.ai-table td {{ border: 1px solid #ccc; padding: 10px; text-align: left; }}
        table.ai-table th {{ background: #f8fafc; font-weight: bold; }}
    </style>
</head>
<body>
    <div class="container" contenteditable="true">
        <!-- PAGE 1: Terminal Output & Visualization -->
        <div class="page">
            <h2>Assignment No. 1 - Execution Output</h2>
            
            <div class="image-box">
                <img src="ASS - 1 ASSETS/heuristics_visualization.png" />
                <div class="image-caption">Figure 1: Heuristic Distribution (Straight-Line Distance to Sissu)</div>
            </div>

            <div class="terminal">
                <div class="terminal-header">
                    <div class="terminal-header-dots">
                        <div class="dot dot-red"></div>
                        <div class="dot dot-yellow"></div>
                        <div class="dot dot-green"></div>
                    </div>
                    <div class="terminal-header-title">aditya@aiml-lab:~/astar</div>
                </div>
                <div class="terminal-body">
<span class="terminal-command">$ python AStar.py</span>
----------------------------------------
STEP - 1: LOAD THE DATASET
----------------------------------------
Dataset loaded Successfully
----------------------------------------

Initial 5 entries in cities (Heuristics):
       City  Heuristic
0      Pune       1650
1    Mumbai       1550
2    Nashik       1500
3     Surat       1350
4  Vadodara       1250
----------------------------------------

Initial 5 entries in connections (Road Network):
   Source Destination  Distance
0    Pune      Mumbai       150
1    Pune      Nashik       210
2  Mumbai       Surat       280
3  Mumbai      Nashik       170
4  Nashik       Surat       230
----------------------------------------
STEP - 2: DATA ANALYSIS (EDA)
----------------------------------------
Cities dataset shape     : (30, 2)
Connections dataset shape: (43, 3)
----------------------------------------
Cities Column Names      : ['City', 'Heuristic']
Connections Column Names : ['Source', 'Destination', 'Distance']
----------------------------------------
Missing values in Cities:
City         0
Heuristic    0
dtype: int64

Missing values in Connections:
Source         0
Destination    0
Distance       0
dtype: int64
----------------------------------------
Statistical Summary of Cities (Heuristics):
         Heuristic
count    30.000000
mean    656.066667
std     545.507984
min       0.000000
25%     145.000000
50%     515.000000
75%    1200.000000
max    1650.000000

Statistical Summary of Connections (Distances):
         Distance
count   43.000000
mean   182.976744
std    122.616997
min     12.000000
25%     52.500000
50%    210.000000
75%    255.000000
max    430.000000</div>
            </div>
        </div>

        <!-- PAGE 2: Execution Results Continued -->
        <div class="page">
            <div class="terminal">
                <div class="terminal-header">
                    <div class="terminal-header-dots">
                        <div class="dot dot-red"></div>
                        <div class="dot dot-yellow"></div>
                        <div class="dot dot-green"></div>
                    </div>
                    <div class="terminal-header-title">aditya@aiml-lab:~/astar</div>
                </div>
                <div class="terminal-body">
----------------------------------------
STEP - 3: BUILD THE GRAPH & HEURISTICS
----------------------------------------
Graph and heuristic structures built successfully.
Total Unique Nodes (Cities) in Graph: 30
Total Connections in Road Network   : 43
----------------------------------------
STEP - 4: DECIDE START AND GOAL CITIES
----------------------------------------
Starting City : Pune
Destination   : Sissu
----------------------------------------
STEP - 5: VISUALISATION OF DATASET
----------------------------------------
Plotting heuristic values (straight-line distance to goal)...
Visualization plot saved successfully to: heuristics_visualization.png
Displaying visualization plot window...
----------------------------------------
STEP - 6: DEFINE THE A* SEARCH ALGORITHM
----------------------------------------
----------------------------------------
STEP - 7: RUN THE SEARCH MODEL
----------------------------------------

Node Expansion Phase:
Current Node    | g_cost | heuristic | f_cost
---------------------------------------------
Pune            | g =    0 | h = 1650 | f = 1650
Mumbai          | g =  150 | h = 1550 | f = 1700
Nashik          | g =  210 | h = 1500 | f = 1710
Surat           | g =  430 | h = 1350 | f = 1780
Indore          | g =  620 | h = 1200 | f = 1820
Vadodara        | g =  580 | h = 1250 | f = 1830
Udaipur         | g =  910 | h =  950 | f = 1860
Ahmedabad       | g =  690 | h = 1200 | f = 1890
Jaipur          | g = 1305 | h =  700 | f = 2005
Bhopal          | g =  810 | h = 1250 | f = 2060
Gwalior         | g = 1240 | h =  800 | f = 2040
Agra            | g = 1360 | h =  680 | f = 2040
Mathura         | g = 1410 | h =  630 | f = 2040
Delhi           | g = 1560 | h =  500 | f = 2060
Chandigarh      | g = 1810 | h =  220 | f = 2030
Shimla          | g = 1925 | h =  120 | f = 2045
Kufri           | g = 1941 | h =  110 | f = 2051
Gurugram        | g = 1590 | h =  500 | f = 2090
Noida           | g = 1585 | h =  510 | f = 2095
Dehradun        | g = 1825 | h =  280 | f = 2105
Faridabad       | g = 1595 | h =  520 | f = 2115
Rishikesh       | g = 1870 | h =  295 | f = 2165
Kullu           | g = 2135 | h =   80 | f = 2215
Manali          | g = 2175 | h =   40 | f = 2215
Solang Valley   | g = 2188 | h =   25 | f = 2213
Atal Tunnel     | g = 2203 | h =   12 | f = 2215
Naggar          | g = 2155 | h =   60 | f = 2215
Sissu           | g = 2215 | h =    0 | f = 2215

A* Search completed successfully
----------------------------------------
----------------------------------------
STEP - 8: EVALUATE MODEL PERFORMANCE
----------------------------------------
Start City      : Pune
Destination     : Sissu
Total Distance  : 2215 km
Places Covered  : 14

Optimal Route:
 1. Pune
 2. Nashik
 3. Indore
 4. Bhopal
 5. Gwalior
 6. Mathura
 7. Delhi
 8. Chandigarh
 9. Shimla
10. Kullu
11. Manali
12. Solang Valley
13. Atal Tunnel
14. Sissu

Complete Path:
Pune -> Nashik -> Indore -> Bhopal -> Gwalior -> Mathura -> Delhi -> Chandigarh -> Shimla -> Kullu -> Manali -> Solang Valley -> Atal Tunnel -> Sissu
----------------------------------------</div>
            </div>
        </div>

        <!-- PAGE 3: AI Usage Report -->
        <div class="page">
            <h2>AI Usage Report</h2>
            <p>As part of modern software development practices, Artificial Intelligence (AI) tools were leveraged ethically to assist in the formatting, documentation, and logic verification of this assignment.</p>
            
            <table class="ai-table">
                <thead>
                    <tr>
                        <th style="width: 25%;">Task / Feature</th>
                        <th style="width: 75%;">AI Assistance Details</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><strong>Algorithm Implementation</strong></td>
                        <td>Used AI to verify the theoretical correctness of the A* heuristic logic (`f = g + h`) within the custom dataset constraints and to ensure the priority queue accurately evaluated the minimum cost.</td>
                    </tr>
                    <tr>
                        <td><strong>Data Visualization</strong></td>
                        <td>Leveraged AI to generate clean Matplotlib / Seaborn plotting code for visualizing the straight-line heuristic distance distribution to Sissu.</td>
                    </tr>
                    <tr>
                        <td><strong>Documentation Formatting</strong></td>
                        <td>Utilized generative tools to convert plain text theory notes into a highly structured, CSS-styled HTML assignment document suitable for A4 printing and professional presentation.</td>
                    </tr>
                    <tr>
                        <td><strong>Debugging</strong></td>
                        <td>Assisted in debugging dictionary mapping errors from the raw CSV edge-list datasets (<code>cities.csv</code>, <code>connections.csv</code>) to form a complete bidirectional graph.</td>
                    </tr>
                </tbody>
            </table>
            
            <p style="margin-top: 20px;"><strong>Conclusion on AI Usage:</strong> The AI tools successfully acted as an advanced pair-programmer. Core architectural decisions regarding the start/goal states and data preprocessing were engineered manually, while boilerplate code and layout styling were accelerated using intelligent generation, significantly boosting productivity.</p>
        </div>
    </div>
</body>
</html>"""

    with open(os.path.join(base_dir, "Assignment_1.html"), 'w', encoding='utf-8') as f:
        f.write(html_1)
        
    with open(os.path.join(base_dir, "Assignment_1_Output_and_AI_Usage.html"), 'w', encoding='utf-8') as f:
        f.write(html_2)

if __name__ == "__main__":
    build_files()
