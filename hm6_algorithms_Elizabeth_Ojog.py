import matplotlib.pyplot as plt
import networkx as nx
import random
from collections import deque  

# ============================================================================
# TASK 1: Create and Analyze Graph
# ============================================================================

# Route 102: Dublin Airport → Sutton Station
route_102 = [
    "Dublin Airport", "Maldron Hotel", "Airport Roundabout", "Stockhole Lane",
    "Forrest Little Golf", "Forest Road", "Rathingle Road", "Cherry Avenue",
    "Forest View", "Forest Crescent", "Rathingle Road", "Hilltown Road",
    "River Valley Heights", "River Valley Drive", "Ballintrane Wood",
    "Highfield Green", "Swords Main Street", "Swords Pavilions Sc",
    "Swords Road", "Seamount View", "Feltrim Business Pk", "Feltrim Business Pk",
    "Waterside", "Chamley Park", "Estuary Road", "Sacred Heart Church",
    "Yellow Walls Rd", "St Sylvesters School", "Cricket Club", "Malahide Station",
    "Malahide", "The Old Golf Links", "Sea Park", "Muldowney Court", "Biscayne",
    "Robswall Crescent", "Monks Meadow", "Strand Road", "Portmarnock Hotel",
    "Blackberry Lane", "Blackberry Rise", "The Dunes", "Portmarnock",
    "Hazel Court", "Coast Road", "St Rita's House", "Moyne Bridge",
    "Moyne Cottages", "Red Arches Rd", "Baldoyle Church", "Baldoyle",
    "Strand Road", "Burrowfield Road", "Station Road", "Sutton Station"
]

# Route 102A: St Fintan's Church → Swords Pavilions Sc
route_102a = [
    "St Fintan's Church", "Sutton Station", "Station Road", "Strand Road",
    "Baldoyle", "Willie Nolan Road", "Red Arches Rd", "Moyne Cottages",
    "Moyne Bridge", "St Rita's House", "Portmarnock Bridge", "Hazel Grove",
    "Portmarnock", "Carrickhill Rd Lower", "Ardilaun", "Hillcourt",
    "Community School", "Redfern Avenue", "Briar Walk", "Wendell Avenue",
    "Monks Meadow", "Robswall Crescent", "Biscayne", "Sea Park", "Mayfair",
    "Malahide Village", "Malahide Station", "Cricket Club", "St Sylvesters School",
    "Yellow Walls Road", "Seabury Road", "Estuary Road", "Chamley Park",
    "Waterside", "Feltrim Business Pk", "Feltrim Business Pk", "Seamount View",
    "Ashley Drive", "Malahide Road", "Swords Pavilions Sc"
]

# Route 102C: Balgriffin Cottages → Sutton Park School
route_102c = [
    "Balgriffin Cottages", "Fingal Cemetery", "St Doulagh's Church",
    "St Doolagh's Park", "Posey Row", "St Nicholas Ns", "Chapel Road",
    "Copperbush", "Myra Manor", "Streamstown Lane", "Streamstown Lane",
    "Auburn House", "Malahide Demense", "St Sylvesters School", "Cricket Club",
    "Malahide Station", "Malahide", "The Old Golf Links", "Sea Park",
    "Muldowney Court", "Biscayne", "Robswall Crescent", "Monks Meadow",
    "Wendell Avenue", "Kelvin Close", "Redfern Avenue", "Hillcourt",
    "Carrickhill Rd Lower", "Portmarnock", "Hazel Court", "Coast Road",
    "St Rita's House", "Moyne Bridge", "Moyne Cottages", "The Coast",
    "Baldoyle", "Strand Road", "Burrowfield Road", "Station Road",
    "Sutton Station", "Santa Sabina", "Sutton Park School"
]

# Create Directed Graph with Weights
G = nx.DiGraph()

def generate_weights():
    distance = round(random.uniform(0.3, 2.5), 1)  # km
    time = round((distance / 25) * 60 + random.uniform(0.5, 1.5), 1)  # minutes
    return distance, time

random.seed(42)  

# Add edges for route 102
for i in range(len(route_102) - 1):
    distance, time = generate_weights()
    G.add_edge(route_102[i], route_102[i + 1], 
               route='102', distance=distance, time=time, weight=time)

# Add edges for route 102A
for i in range(len(route_102a) - 1):
    distance, time = generate_weights()
    G.add_edge(route_102a[i], route_102a[i + 1], 
               route='102A', distance=distance, time=time, weight=time)

# Add edges for route 102C
for i in range(len(route_102c) - 1):
    distance, time = generate_weights()
    G.add_edge(route_102c[i], route_102c[i + 1], 
               route='102C', distance=distance, time=time, weight=time)

# Add node attributes
s102 = set(route_102)
s102a = set(route_102a)
s102c = set(route_102c)

for node in G.nodes():
    route_count = sum([node in s102, node in s102a, node in s102c])
    G.nodes[node]['route_count'] = route_count
    G.nodes[node]['importance'] = route_count

# ============================================================================
# TASK 1: Analysis
# ============================================================================

print("=" * 80)
print("TASK 1: Graph Analysis")
print("=" * 80)

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"\n📊 Basic Characteristics:")
print(f"   • Graph Type: Directed (DiGraph)")
print(f"   • Number of nodes (stops): {num_nodes}")
print(f"   • Number of edges (connections): {num_edges}")

in_degrees = dict(G.in_degree())
out_degrees = dict(G.out_degree())

avg_in_degree = sum(in_degrees.values()) / num_nodes
avg_out_degree = sum(out_degrees.values()) / num_nodes

print(f"\n📈 Node Degrees:")
print(f"   • Average in-degree: {avg_in_degree:.2f}")
print(f"   • Average out-degree: {avg_out_degree:.2f}")

top_in = sorted(in_degrees.items(), key=lambda x: x[1], reverse=True)[:5]
top_out = sorted(out_degrees.items(), key=lambda x: x[1], reverse=True)[:5]

print(f"\n🚏 Top 5 Stops by In-Degree:")
for stop, degree in top_in:
    print(f"   • {stop}: {degree}")

print(f"\n🚏 Top 5 Stops by Out-Degree:")
for stop, degree in top_out:
    print(f"   • {stop}: {degree}")

all_distances = [G[u][v]['distance'] for u, v in G.edges()]
all_times = [G[u][v]['time'] for u, v in G.edges()]

print(f"\n⏱️ Edge Weight Analysis (Time):")
print(f"   • Average time between stops: {sum(all_times)/len(all_times):.1f} min")
print(f"   • Minimum time: {min(all_times):.1f} min")
print(f"   • Maximum time: {max(all_times):.1f} min")

print(f"\n📏 Edge Weight Analysis (Distance):")
print(f"   • Average distance between stops: {sum(all_distances)/len(all_distances):.1f} km")
print(f"   • Minimum distance: {min(all_distances):.1f} km")
print(f"   • Maximum distance: {max(all_distances):.1f} km")

common_all = s102 & s102a & s102c
common_102_102a = (s102 & s102a) - common_all
common_102_102c = (s102 & s102c) - common_all
common_102a_102c = (s102a & s102c) - common_all

unique_102 = s102 - (s102a | s102c)
unique_102a = s102a - (s102 | s102c)
unique_102c = s102c - (s102 | s102a)

print(f"\n🔀 Shared Stops Analysis:")
print(f"   • Common to all 3 routes: {len(common_all)}")
if common_all:
    print(f"     {common_all}")
print(f"   • Common to 102 & 102A only: {len(common_102_102a)}")
print(f"   • Common to 102 & 102C only: {len(common_102_102c)}")
print(f"   • Common to 102A & 102C only: {len(common_102a_102c)}")
print(f"   • Unique to 102: {len(unique_102)}")
print(f"   • Unique to 102A: {len(unique_102a)}")
print(f"   • Unique to 102C: {len(unique_102c)}")

print(f"\n🚌 Route Characteristics:")
for route_name, route_stops in [('102', route_102), ('102A', route_102a), ('102C', route_102c)]:
    total_time = 0
    total_distance = 0
    for i in range(len(route_stops) - 1):
        if G.has_edge(route_stops[i], route_stops[i+1]):
            edge_data = G[route_stops[i]][route_stops[i+1]]
            total_time += edge_data['time']
            total_distance += edge_data['distance']
    
    print(f"\n   Route {route_name}:")
    print(f"      • Number of stops: {len(route_stops)}")
    print(f"      • Total distance: {total_distance:.1f} km")
    print(f"      • Total time: {total_time:.1f} min ({total_time/60:.1f} hours)")
    print(f"      • Average speed: {(total_distance/(total_time/60)):.1f} km/h")

# Visualization
plt.figure(figsize=(20, 14))
pos = nx.spring_layout(G, k=0.5, iterations=50, seed=42)

node_colors = []
for node in G.nodes():
    route_count = G.nodes[node]['route_count']
    if route_count == 3:
        node_colors.append('#FFD700')
    elif route_count == 2:
        node_colors.append('#FF8C00')
    elif node in s102:
        node_colors.append('#4169E1')
    elif node in s102a:
        node_colors.append('#32CD32')
    elif node in s102c:
        node_colors.append('#DC143C')
    else:
        node_colors.append('#808080')

edge_colors = []
for u, v in G.edges():
    route = G[u][v]['route']
    if route == '102':
        edge_colors.append('#4169E1')
    elif route == '102A':
        edge_colors.append('#32CD32')
    elif route == '102C':
        edge_colors.append('#DC143C')
    else:
        edge_colors.append('#808080')

nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=250, alpha=0.9)
nx.draw_networkx_edges(G, pos, edge_color=edge_colors, arrows=True, 
                        arrowsize=8, width=1.5, alpha=0.6,
                        connectionstyle="arc3,rad=0.1")

important_stops = list(common_all) + [
    route_102[0], route_102[-1],
    route_102a[0], route_102a[-1],
    route_102c[0], route_102c[-1]
]
labels = {node: node for node in G.nodes() if node in important_stops}
nx.draw_networkx_labels(G, pos, labels, font_size=8, font_weight='bold')

legend_elements = [
    plt.Line2D([0], [0], color='#4169E1', lw=3, label='Route 102'),
    plt.Line2D([0], [0], color='#32CD32', lw=3, label='Route 102A'),
    plt.Line2D([0], [0], color='#DC143C', lw=3, label='Route 102C'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FFD700', 
               markersize=12, label='3 routes (hub)'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='#FF8C00', 
               markersize=12, label='2 routes (transfer)')
]

plt.legend(handles=legend_elements, loc='upper left', fontsize=11)
plt.title("Dublin Bus Network Graph\n(Routes 102, 102A, 102C)\nWeighted Directed Graph", 
          fontsize=16, fontweight='bold', pad=20)
plt.axis('off')
plt.tight_layout()
plt.show()

# ============================================================================
# TASK 2: DFS and BFS Path Finding
# ============================================================================

print("\n" + "=" * 80)
print("TASK 2: DFS vs BFS Comparison")
print("=" * 80)

# DFS with path tracking
def dfs_path(graph, start, goal, path=None, visited=None):
    """DFS to find path from start to goal"""
    if path is None:
        path = []
    if visited is None:
        visited = set()
    
    path = path + [start]
    visited.add(start)
    
    if start == goal:
        return path
    
    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    
    return None

# BFS with path tracking
def bfs_path(graph, start, goal):
    """BFS to find path from start to goal"""
    if start == goal:
        return [start]
    
    visited = {start}
    queue = deque([[start]])
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        
        for neighbor in graph.neighbors(node):
            if neighbor not in visited:
                new_path = path + [neighbor]
                
                if neighbor == goal:
                    return new_path
                
                visited.add(neighbor)
                queue.append(new_path)
    
    return None

# Test examples
print("\n🔍 Example 1: Dublin Airport → Malahide Station")
print("-" * 80)

start = "Dublin Airport"
goal = "Malahide Station"

dfs_result = dfs_path(G, start, goal)
bfs_result = bfs_path(G, start, goal)

print(f"\n✅ DFS Path ({len(dfs_result)} stops):")
print(" → ".join(dfs_result))

print(f"\n✅ BFS Path ({len(bfs_result)} stops):")
print(" → ".join(bfs_result))

print(f"\n📊 Comparison:")
print(f"   • DFS found path with {len(dfs_result)} stops")
print(f"   • BFS found path with {len(bfs_result)} stops")
print(f"   • Difference: {abs(len(dfs_result) - len(bfs_result))} stops")

print("\n" + "=" * 80)
print("🔍 Example 2: Dublin Airport → Sutton Station")
print("-" * 80)

start = "Dublin Airport"
goal = "Sutton Station"

dfs_result2 = dfs_path(G, start, goal)
bfs_result2 = bfs_path(G, start, goal)

print(f"\n✅ DFS Path ({len(dfs_result2)} stops):")
print(" → ".join(dfs_result2))

print(f"\n✅ BFS Path ({len(bfs_result2)} stops):")
print(" → ".join(bfs_result2))

print(f"\n📊 Comparison:")
print(f"   • DFS found path with {len(dfs_result2)} stops")
print(f"   • BFS found path with {len(bfs_result2)} stops")
print(f"   • Difference: {abs(len(dfs_result2) - len(bfs_result2))} stops")

print("\n" + "=" * 80)
print("💡 Explanation of Differences")
print("=" * 80)
print("""
DFS (Depth-First Search):
   • Goes as deep as possible along one branch before backtracking
   • Uses stack (recursion)
   • May find LONGER path, but finds any path quickly
   • Good for traversing entire graph

BFS (Breadth-First Search):
   • Explores all neighbors at current level before going deeper
   • Uses queue
   • ALWAYS finds SHORTEST path (by number of stops)
   • Good for finding minimum transfers

Why paths are different:
   • DFS follows first available direction to the end
   • BFS checks all possibilities at each step
   • Our graph has multiple paths to destinations
   • DFS may go through all stops on route 102
   • BFS finds minimum number of stops
""")

# ============================================================================
# TASK 3: Dijkstra's Algorithm
# ============================================================================

print("\n" + "=" * 80)
print("TASK 3: Dijkstra's Algorithm for Shortest Paths")
print("=" * 80)

print("\n🎯 Dijkstra finds shortest path considering WEIGHTS (time)")
print("   Unlike BFS which counts stops, Dijkstra finds minimum TIME route\n")

print("=" * 80)
print("🚀 Example 1: Shortest Paths from Dublin Airport")
print("=" * 80)

start = "Dublin Airport"
destinations = ["Malahide Station", "Sutton Station", "Swords Pavilions Sc"]

for dest in destinations:
    try:
        # Shortest path by time
        path_time = nx.shortest_path(G, start, dest, weight='weight')
        length_time = nx.shortest_path_length(G, start, dest, weight='weight')
        
        # Shortest path by distance
        path_dist = nx.shortest_path(G, start, dest, weight='distance')
        length_dist = nx.shortest_path_length(G, start, dest, weight='distance')
        
        print(f"\n📍 {start} → {dest}:")
        print(f"   ⏱️  By time: {length_time:.1f} min ({len(path_time)} stops)")
        print(f"      Path: {' → '.join(path_time[:3])} ... {' → '.join(path_time[-2:])}")
        print(f"   📏 By distance: {length_dist:.1f} km ({len(path_dist)} stops)")
        
    except nx.NetworkXNoPath:
        print(f"\n❌ No path from {start} to {dest}")

print("\n" + "=" * 80)
print("🚀 Example 2: Comparing Different Algorithms")
print("=" * 80)

routes_to_compare = [
    ("Dublin Airport", "Baldoyle"),
    ("Malahide Station", "Sutton Station")
]

for start, end in routes_to_compare:
    try:
        # Dijkstra (shortest by time)
        dijkstra_path = nx.shortest_path(G, start, end, weight='weight')
        dijkstra_time = nx.shortest_path_length(G, start, end, weight='weight')
        
        # BFS (shortest by number of stops)
        bfs_result = bfs_path(G, start, end)
        
        # Calculate time for BFS path
        bfs_time = 0
        if bfs_result:
            for i in range(len(bfs_result) - 1):
                if G.has_edge(bfs_result[i], bfs_result[i+1]):
                    bfs_time += G[bfs_result[i]][bfs_result[i+1]]['weight']
        
        print(f"\n📍 {start} → {end}:")
        print(f"   🏆 Dijkstra (optimal by time):")
        print(f"      • Time: {dijkstra_time:.1f} min")
        print(f"      • Stops: {len(dijkstra_path)}")
        print(f"   🔵 BFS (fewest stops):")
        print(f"      • Time: {bfs_time:.1f} min")
        print(f"      • Stops: {len(bfs_result)}")
        print(f"   ⚡ Time saved: {bfs_time - dijkstra_time:.1f} min")
        
    except (nx.NetworkXNoPath, TypeError) as e:
        print(f"\n❌ Error for route {start} → {end}")

print("\n" + "=" * 80)
print("✅ Summary")
print("=" * 80)
print("""
1️⃣ DFS (Depth-First Search):
   • Quickly finds ANY path
   • May find longer route
   • Good for complete graph traversal

2️⃣ BFS (Breadth-First Search):
   • Finds path with FEWEST stops
   • Doesn't consider time or distance
   • Guarantees minimum transfers

3️⃣ Dijkstra's Algorithm:
   • Finds OPTIMAL path by WEIGHT (time/distance)
   • Considers actual travel time
   • Best for planning real routes

🎯 For transport networks, Dijkstra is the best choice!
""")

