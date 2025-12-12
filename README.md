# GoIT Algo HW — Graphs (NetworkX): Dublin Bus Routes 102 / 102A / 102C

## Project Overview
This project models a real transport network using **NetworkX**.  
I created a **weighted directed graph (DiGraph)** based on three Dublin Bus routes:

- **102**: Dublin Airport → Sutton Station  
- **102A**: St Fintan's Church → Swords Pavilions  
- **102C**: Balgriffin Cottages → Sutton Park School  

Each stop is represented as a **node**, and each connection between consecutive stops is an **edge**.

The program performs:
1. Graph creation with edge weights (distance + travel time)
2. Graph analysis (nodes/edges, degrees, shared stops, route statistics)
3. Traversal comparison: **DFS vs BFS**
4. Shortest path search using **Dijkstra’s algorithm** (via NetworkX weighted shortest paths)
---

## Graph Model

### Nodes (Stops)
Each bus stop is a node.  
Each node has attributes:
- `route_count`: how many routes pass through this stop (1, 2, or 3)
- `importance`: same as route_count (used for visualization)

Stops shared by multiple routes become transfer points (higher importance).

### Edges (Connections)
Edges connect **consecutive stops** in a route.

Each edge has attributes:
- `route`: which bus route the edge belongs to (`102`, `102A`, or `102C`)
- `distance`: randomly generated distance in km (0.3–2.5 km)
- `time`: travel time in minutes (based on distance and average speed)
- `weight`: equals `time` (used for Dijkstra when finding fastest paths)

> Note: `random.seed(42)` is used so generated weights are reproducible.

---

## Algorithms Implemented

### DFS (Depth-First Search)
- Explores deep into one branch first (recursive)
- Finds *some* path, not guaranteed shortest

### BFS (Breadth-First Search)
- Explores level by level using a queue
- Guarantees the shortest path by **number of stops** (unweighted)

### Dijkstra (Weighted Shortest Path)
- Finds the optimal path based on **edge weights**
- In this project, weights represent **travel time**, so Dijkstra finds the **fastest route**

NetworkX is used internally for Dijkstra via:
- `nx.shortest_path(G, start, end, weight="weight")`
- `nx.shortest_path_length(G, start, end, weight="weight")`

---

## Results / Observations

### DFS vs BFS
- DFS may return a longer route because it follows the first available direction deeply.
- BFS finds a route with fewer stops because it checks all neighbors level-by-level.

### Dijkstra vs BFS
- BFS optimizes by number of stops only.
- Dijkstra optimizes by travel time (minutes), so it can choose a path with more stops if it is faster overall.

This shows why weighted shortest path algorithms (Dijkstra) are more suitable for real transport planning.

---

## Visualization
The program visualizes the graph with:
- Node colors depending on route membership and transfer importance:
  - Gold: stop shared by **3 routes**
  - Orange: stop shared by **2 routes**
  - Blue: stop only in **102**
  - Green: stop only in **102A**
  - Red: stop only in **102C**
- Edge colors based on route

Only the most important stops (shared stops + route start/end stops) are labeled to avoid clutter.

---

## How to Run

1. Install dependencies:
```bash
pip install networkx matplotlib
