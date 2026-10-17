import java.util.*;

/**
 * SwiftCargo - Optimal Delivery Routing over a Multistage Graph
 * Assignment 5 :: Design & Analysis of Algorithms Laboratory (BIT25PC04)
 * Aditya Chandrajit Deore | PRN 124B1F116
 *
 * Technique  : Dynamic Programming, BACKWARD approach, on a directed,
 *              weighted, stage-partitioned (multistage) graph.
 * Complexity : Theta(V + E) time, Theta(V) auxiliary space.
 */
public class SwiftCargo {

    static final int INF = Integer.MAX_VALUE / 4;

    /** A directed transport link joining two CONSECUTIVE stages. */
    static class Edge {
        int to, base;                // base cost = fuel + toll + handling
        double traffic, weather;     // live penalty factors, range [0, 1]
        boolean open = true;         // false => road closure / blockade

        Edge(int to, int base) { this.to = to; this.base = base; }

        /** Effective real-time cost = base * (1 + 0.50*traffic + 0.30*weather). */
        int cost() {
            if (!open) return INF;
            return (int) Math.round(base * (1 + 0.50 * traffic + 0.30 * weather));
        }
    }

    final int n, stages;
    final int[] stageOf;
    final String[] code, city;
    final List<Edge>[] adj;
    final List<List<Integer>> byStage = new ArrayList<>();

    int[] cost;   // cost[v] = minimum cost to travel from v to the sink
    int[] next;   // next[v] = successor of v on that optimal route
    int routes = 0;

    @SuppressWarnings("unchecked")
    SwiftCargo(int n, int stages) {
        this.n = n; this.stages = stages;
        stageOf = new int[n];
        code = new String[n];
        city = new String[n];
        adj = new List[n];
        for (int i = 0; i < n; i++) adj[i] = new ArrayList<>();
        for (int s = 0; s < stages; s++) byStage.add(new ArrayList<>());
    }

    void addCity(int v, int stage, String cd, String nm) {
        stageOf[v] = stage; code[v] = cd; city[v] = nm;
        byStage.get(stage).add(v);
    }

    void addRoute(int u, int v, int base) {
        if (stageOf[v] != stageOf[u] + 1)
            throw new IllegalArgumentException("Routes must span consecutive stages");
        adj[u].add(new Edge(v, base));
        routes++;
    }

    Edge find(int u, int v) {
        for (Edge e : adj[u]) if (e.to == v) return e;
        return null;
    }

    /** Real-time constraint injection: traffic density and weather delay. */
    void setLiveConditions(int u, int v, double traffic, double weather) {
        Edge e = find(u, v);
        if (e != null) { e.traffic = traffic; e.weather = weather; }
    }

    /** Real-time road closure -- the edge is logically removed. */
    void closeRoute(int u, int v) {
        Edge e = find(u, v);
        if (e != null) e.open = false;
    }

    /**
     * BACKWARD-APPROACH DYNAMIC PROGRAMMING.
     * Recurrence:  cost(v) = 0                              , v in last stage
     *              cost(u) = min { w(u,v) + cost(v) }        , (u,v) in E
     * A single Theta(V+E) sweep solves EVERY possible source simultaneously,
     * which is exactly what makes batch processing cheap.
     */
    void solve() {
        cost = new int[n];
        next = new int[n];
        Arrays.fill(cost, INF);
        Arrays.fill(next, -1);

        for (int t : byStage.get(stages - 1)) cost[t] = 0;      // sink stage

        for (int s = stages - 2; s >= 0; s--)                   // right to left
            for (int u : byStage.get(s))
                for (Edge e : adj[u]) {
                    int w = e.cost();
                    if (w >= INF || cost[e.to] >= INF) continue;
                    if (w + cost[e.to] < cost[u]) {
                        cost[u] = w + cost[e.to];
                        next[u] = e.to;
                    }
                }
    }

    /** Route reconstruction in Theta(stages) using the next[] pointers. */
    List<Integer> route(int src) {
        List<Integer> p = new ArrayList<>();
        if (cost[src] >= INF) return p;
        for (int v = src; v != -1; v = next[v]) p.add(v);
        return p;
    }

    String routeText(int src) {
        List<Integer> p = route(src);
        if (p.isEmpty()) return "UNREACHABLE";
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < p.size(); i++) {
            sb.append(code[p.get(i)]);
            if (i < p.size() - 1) sb.append(" -> ");
        }
        return sb.toString();
    }

    public static void main(String[] args) {
        System.out.println("=== SwiftCargo Logistics Optimization ===");
        
        // 1. Model the transportation network (4 stages: Source -> Hub 1 -> Hub 2 -> Destination)
        SwiftCargo network = new SwiftCargo(8, 4);
        
        // Stage 0: Sources (Warehouses)
        network.addCity(0, 0, "WH1", "Warehouse 1");
        network.addCity(1, 0, "WH2", "Warehouse 2");
        
        // Stage 1: Transit Hubs A
        network.addCity(2, 1, "HA1", "Hub A1");
        network.addCity(3, 1, "HA2", "Hub A2");
        network.addCity(4, 1, "HA3", "Hub A3");
        
        // Stage 2: Transit Hubs B
        network.addCity(5, 2, "HB1", "Hub B1");
        network.addCity(6, 2, "HB2", "Hub B2");
        
        // Stage 3: Destinations (Final Delivery Points)
        network.addCity(7, 3, "DEST", "Destination");
        
        // Add routes with base costs
        network.addRoute(0, 2, 100);
        network.addRoute(0, 3, 150);
        network.addRoute(1, 3, 120);
        network.addRoute(1, 4, 130);
        
        network.addRoute(2, 5, 200);
        network.addRoute(2, 6, 250);
        network.addRoute(3, 5, 180);
        network.addRoute(3, 6, 220);
        network.addRoute(4, 6, 190);
        
        network.addRoute(5, 7, 300);
        network.addRoute(6, 7, 280);
        
        System.out.println("\n[+] Initial Optimal Routes:");
        network.solve(); // Batch processing: solves for all nodes in one pass
        System.out.println("WH1 Route: " + network.routeText(0) + " | Cost: " + network.cost[0]);
        System.out.println("WH2 Route: " + network.routeText(1) + " | Cost: " + network.cost[1]);
        
        System.out.println("\n[+] Real-time constraints applied (Traffic delay on HA2->HB1, Weather on HB1->DEST)");
        network.setLiveConditions(3, 5, 0.8, 0.0); // High traffic
        network.setLiveConditions(5, 7, 0.0, 0.9); // Bad weather
        
        network.solve();
        System.out.println("WH1 Route: " + network.routeText(0) + " | Cost: " + network.cost[0]);
        System.out.println("WH2 Route: " + network.routeText(1) + " | Cost: " + network.cost[1]);
        
        System.out.println("\n[+] Road Closure (Hub B2 -> Destination)");
        network.closeRoute(6, 7);
        
        network.solve();
        System.out.println("WH1 Route: " + network.routeText(0) + " | Cost: " + network.cost[0]);
        System.out.println("WH2 Route: " + network.routeText(1) + " | Cost: " + network.cost[1]);
        
        // Scalability test
        System.out.println("\n[+] Testing Scalability (Large Dataset: 10,000 cities, 5 stages)");
        testScalability();
    }
    
    static void testScalability() {
        int n = 10000;
        int stages = 5;
        SwiftCargo largeNetwork = new SwiftCargo(n, stages);
        
        int nodesPerStage = n / stages;
        for (int i = 0; i < n; i++) {
            largeNetwork.addCity(i, i / nodesPerStage, "C" + i, "City " + i);
        }
        
        Random rand = new Random(42);
        for (int s = 0; s < stages - 1; s++) {
            for (int u = s * nodesPerStage; u < (s + 1) * nodesPerStage; u++) {
                // Add 10 random edges to next stage
                for (int k = 0; k < 10; k++) {
                    int v = (s + 1) * nodesPerStage + rand.nextInt(nodesPerStage);
                    largeNetwork.addRoute(u, v, 50 + rand.nextInt(100));
                }
            }
        }
        
        long start = System.currentTimeMillis();
        largeNetwork.solve();
        long end = System.currentTimeMillis();
        System.out.println("Optimal routes calculated for 10,000 cities and " + largeNetwork.routes + " routes in " + (end - start) + " ms.");
    }
}
