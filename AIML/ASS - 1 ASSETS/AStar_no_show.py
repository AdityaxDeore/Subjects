import os
import sys
import heapq
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Border = "-"*40

# Paths to CSV files relative to the script location
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CITIES_CSV = os.path.join(SCRIPT_DIR, "cities.csv")
CONNECTIONS_CSV = os.path.join(SCRIPT_DIR, "connections.csv")

#############################################
# STEP - 1 LOAD THE DATASET (CSV FILES)
#############################################
print(Border)
print("STEP - 1: LOAD THE DATASET")
print(Border)

if not os.path.exists(CITIES_CSV) or not os.path.exists(CONNECTIONS_CSV):
    print("Error: Dataset CSV files not found.", file=sys.stderr)
    sys.exit(1)

# Load dataframes using pandas
df_cities = pd.read_csv(CITIES_CSV)
df_connections = pd.read_csv(CONNECTIONS_CSV)

print("Dataset loaded Successfully")

print(Border)
print("\nInitial 5 entries in cities (Heuristics):")
print(df_cities.head())

print(Border)
print("\nInitial 5 entries in connections (Road Network):")
print(df_connections.head())


#############################################
# STEP - 2 DATA ANALYSIS (EDA)
#############################################
print(Border)
print("STEP - 2: DATA ANALYSIS (EDA)")
print(Border)

print("Cities dataset shape     :", df_cities.shape)
print("Connections dataset shape:", df_connections.shape)

print(Border)
print("Cities Column Names      :", list(df_cities.columns))
print("Connections Column Names :", list(df_connections.columns))

print(Border)
print("Missing values in Cities:")
print(df_cities.isnull().sum())
print("\nMissing values in Connections:")
print(df_connections.isnull().sum())

print(Border)
print("Statistical Summary of Cities (Heuristics):")
print(df_cities.describe())
print("\nStatistical Summary of Connections (Distances):")
print(df_connections.describe())


#############################################
# STEP - 3 BUILD THE GRAPH & HEURISTICS
#############################################
print(Border)
print("STEP - 3: BUILD THE GRAPH & HEURISTICS")
print(Border)

heuristic = {}
graph = {}

# Populate heuristic dictionary
for index, row in df_cities.iterrows():
    city = row['City'].strip()
    val = int(row['Heuristic'])
    heuristic[city] = val
    if city not in graph:
        graph[city] = []

# Populate graph adjacency list (bidirectional)
for index, row in df_connections.iterrows():
    src = row['Source'].strip()
    dest = row['Destination'].strip()
    dist = int(row['Distance'])

    if src not in graph:
        graph[src] = []
    if dest not in graph:
        graph[dest] = []

    graph[src].append((dest, dist))
    graph[dest].append((src, dist))

print("Graph and heuristic structures built successfully.")
print(f"Total Unique Nodes (Cities) in Graph: {len(graph)}")
print(f"Total Connections in Road Network   : {len(df_connections)}")


#############################################
# STEP - 4 DECIDE START AND GOAL CITIES
#############################################
print(Border)
print("STEP - 4: DECIDE START AND GOAL CITIES")
print(Border)

start = "Pune"
goal = "Sissu"

print(f"Starting City : {start}")
print(f"Destination   : {goal}")

# Verify existence
if start not in graph:
    print(f"Error: Start city '{start}' is not in the graph.")
    sys.exit(1)
if goal not in graph:
    print(f"Error: Goal city '{goal}' is not in the graph.")
    sys.exit(1)


#############################################
# STEP - 5 VISUALISATION OF DATASET
#############################################
print(Border)
print("STEP - 5: VISUALISATION OF DATASET")
print(Border)

print("Plotting heuristic values (straight-line distance to goal)...")
plt.figure(figsize=(12, 6))

# Sort cities by heuristic value descending to make a nice ordered chart
df_sorted_cities = df_cities.sort_values(by="Heuristic", ascending=False)

sns.barplot(
    data=df_sorted_cities,
    x="City",
    y="Heuristic",
    hue="City",
    palette="viridis",
    legend=False
)

plt.title("A* Search Heuristics: Straight-Line Distance to Sissu")
plt.xlabel("City")
plt.ylabel("Heuristic Value (km)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Save the plot image
plot_path = os.path.join(SCRIPT_DIR, "heuristics_visualization.png")
plt.savefig(plot_path)
print(f"Visualization plot saved successfully to: {plot_path}")
print("Displaying visualization plot window...")
pass


#############################################
# STEP - 6 DEFINE THE A* SEARCH ALGORITHM
#############################################

def reconstruct_path(parent, goal):
    path = []
    while goal is not None:
        path.append(goal)
        goal = parent[goal]
    return path[::-1]

def astar(start, goal):
    open_list = []
    closed_list = set()

    g_cost = {start: 0}
    parent = {start: None}

    heapq.heappush(open_list, (heuristic[start], start))

    print("\nNode Expansion Phase:")
    print(f"{'Current Node':15} | {'g_cost':6} | {'heuristic':9} | {'f_cost'}")
    print("-" * 45)

    while open_list:
        f_cost, current = heapq.heappop(open_list)

        if current in closed_list:
            continue

        print(f"{current:15} | g = {g_cost[current]:4} | h = {heuristic[current]:4} | f = {f_cost}")

        if current == goal:
            return reconstruct_path(parent, goal), g_cost[goal]

        closed_list.add(current)

        for neighbor, distance in graph[current]:
            tentative_g = g_cost[current] + distance

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                parent[neighbor] = current
                f = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f, neighbor))

    return None, None

print(Border)
print("STEP - 6: DEFINE THE A* SEARCH ALGORITHM")
print(Border)


#############################################
# STEP - 7 RUN THE SEARCH MODEL
#############################################
print(Border)
print("STEP - 7: RUN THE SEARCH MODEL")
print(Border)

path, distance = astar(start, goal)

print("\nA* Search completed successfully")
print(Border)


#############################################
# STEP - 8 EVALUATE MODEL PERFORMANCE
#############################################
print(Border)
print("STEP - 8: EVALUATE MODEL PERFORMANCE")
print(Border)

if path:
    print(f"Start City      : {start}")
    print(f"Destination     : {goal}")
    print(f"Total Distance  : {distance} km")
    print(f"Places Covered  : {len(path)}")

    print("\nOptimal Route:")
    for i, city in enumerate(path, 1):
        print(f"{i:2}. {city}")

    print("\nComplete Path:")
    print(" -> ".join(path))
else:
    print("No route found.")

print(Border)
