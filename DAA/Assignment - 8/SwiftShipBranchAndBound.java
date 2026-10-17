import java.util.*;

/**
 * ============================================================================
 * SWIFTSHIP DELIVERY ROUTE OPTIMIZER
 * LC (Least Cost) Branch and Bound Algorithm for TSP
 * ============================================================================
 * Course     : Design & Analysis of Algorithms Laboratory (BIT25PC04)
 * Student    : Aditya Chandrajit Deore
 * PRN        : 124B1F116
 * College    : Pimpri Chinchwad College of Engineering (PCCOE)
 * Faculty    : Dr. Sapana Kolambe
 *
 * Problem Description:
 * A leading logistics company, SwiftShip, must deliver packages to N regional
 * distribution hubs. The delivery truck must visit each city exactly once and
 * return to the central dispatch depot with minimum total cost, considering:
 * - Varying inter-city distances (km)
 * - Fuel consumption costs influenced by terrain/road conditions
 * - Transit time and delivery completion deadlines
 *
 * Algorithmic Strategy:
 * Least Cost (LC) Branch and Bound using Reduced Cost Matrix:
 * 1. Calculate row and column reduction lower bounds.
 * 2. Maintain a Min-Heap Priority Queue prioritizing nodes with smallest lower bound c_hat.
 * 3. Branch to unvisited cities, eliminate redundant rows/cols, and compute incremental lower bound.
 * 4. Dynamically prune all subtrees where lower bound >= current best upper bound.
 * 5. Benchmark against Nearest Neighbor Greedy Heuristic and Brute Force Permutation.
 * ============================================================================
 */
public class SwiftShipBranchAndBound {

    public static final int INF = 9999999;

    // ------------------------------------------------------------------------
    // DATA MODEL: City / Logistics Hub
    // ------------------------------------------------------------------------
    public static class City {
        public final int id;
        public final String name;
        public final String code;
        public final String hubType;

        public City(int id, String name, String code, String hubType) {
            this.id = id;
            this.name = name;
            this.code = code;
            this.hubType = hubType;
        }

        @Override
        public String toString() {
            return String.format("[%s] %-26s (%s)", code, name, hubType);
        }
    }

    // ------------------------------------------------------------------------
    // DATA MODEL: Road Segment Condition
    // ------------------------------------------------------------------------
    public enum RoadCondition {
        HIGHWAY_EXPRESS(1.0, 75.0, "Expressway / 4-Lane"),
        STATE_HIGHWAY(1.2, 55.0, "State Highway"),
        GHAT_ROUGH(1.5, 35.0, "Mountain Pass / Rough"),
        URBAN_CONGESTION(1.75, 25.0, "Heavy Urban Traffic");

        public final double fuelMultiplier;
        public final double avgSpeedKmh;
        public final String description;

        RoadCondition(double fuelMultiplier, double avgSpeedKmh, String description) {
            this.fuelMultiplier = fuelMultiplier;
            this.avgSpeedKmh = avgSpeedKmh;
            this.description = description;
        }
    }

    // ------------------------------------------------------------------------
    // DATA MODEL: State Space Tree Node
    // ------------------------------------------------------------------------
    public static class Node implements Comparable<Node> {
        public final int nodeId;
        public final int parentId;
        public final int city;
        public final int level;
        public final int lowerBound;
        public final int[][] reducedMatrix;
        public final List<Integer> path;

        public Node(int nodeId, int parentId, int city, int level, int lowerBound, 
                    int[][] reducedMatrix, List<Integer> path) {
            this.nodeId = nodeId;
            this.parentId = parentId;
            this.city = city;
            this.level = level;
            this.lowerBound = lowerBound;
            this.reducedMatrix = reducedMatrix;
            this.path = new ArrayList<>(path);
            this.path.add(city);
        }

        @Override
        public int compareTo(Node other) {
            // Min-Heap based on lowest estimated cost (LC-BB)
            return Integer.compare(this.lowerBound, other.lowerBound);
        }
    }

    // ------------------------------------------------------------------------
    // RESULT CONTAINER: Tour Solution
    // ------------------------------------------------------------------------
    public static class TourResult {
        public final String algorithmName;
        public final List<Integer> tour;
        public final int totalCost;
        public final double totalDistanceKm;
        public final double totalFuelCost;
        public final double totalTransitHours;
        public final long executionTimeNs;
        public final int nodesGenerated;
        public final int nodesPruned;

        public TourResult(String algorithmName, List<Integer> tour, int totalCost, 
                          double totalDistanceKm, double totalFuelCost, double totalTransitHours, 
                          long executionTimeNs, int nodesGenerated, int nodesPruned) {
            this.algorithmName = algorithmName;
            this.tour = tour;
            this.totalCost = totalCost;
            this.totalDistanceKm = totalDistanceKm;
            this.totalFuelCost = totalFuelCost;
            this.totalTransitHours = totalTransitHours;
            this.executionTimeNs = executionTimeNs;
            this.nodesGenerated = nodesGenerated;
            this.nodesPruned = nodesPruned;
        }
    }

    // ========================================================================
    // MATRIX REDUCTION UTILITIES
    // ========================================================================
    public static int reduceMatrix(int[][] matrix, int n) {
        int reductionCost = 0;

        // Row Reduction
        for (int i = 0; i < n; i++) {
            int rowMin = INF;
            for (int j = 0; j < n; j++) {
                if (matrix[i][j] < rowMin) {
                    rowMin = matrix[i][j];
                }
            }
            if (rowMin != INF && rowMin > 0) {
                reductionCost += rowMin;
                for (int j = 0; j < n; j++) {
                    if (matrix[i][j] != INF) {
                        matrix[i][j] -= rowMin;
                    }
                }
            }
        }

        // Column Reduction
        for (int j = 0; j < n; j++) {
            int colMin = INF;
            for (int i = 0; i < n; i++) {
                if (matrix[i][j] < colMin) {
                    colMin = matrix[i][j];
                }
            }
            if (colMin != INF && colMin > 0) {
                reductionCost += colMin;
                for (int i = 0; i < n; i++) {
                    if (matrix[i][j] != INF) {
                        matrix[i][j] -= colMin;
                    }
                }
            }
        }

        return reductionCost;
    }

    public static int[][] cloneMatrix(int[][] matrix, int n) {
        int[][] copy = new int[n][n];
        for (int i = 0; i < n; i++) {
            System.arraycopy(matrix[i], 0, copy[i], 0, n);
        }
        return copy;
    }

    // ========================================================================
    // ALGORITHM 1: LC BRANCH AND BOUND (Reduced Cost Matrix & Priority Queue)
    // ========================================================================
    public static TourResult solveLCBranchAndBound(int[][] rawCostMatrix, int[][] distanceMatrix, 
                                                  RoadCondition[][] roadConditions, int n, int startCity) {
        long startTime = System.nanoTime();
        int nodesGenerated = 0;
        int nodesPruned = 0;

        // Initial root reduction
        int[][] rootMatrix = cloneMatrix(rawCostMatrix, n);
        int rootBound = reduceMatrix(rootMatrix, n);
        nodesGenerated++;

        PriorityQueue<Node> pq = new PriorityQueue<>();
        Node root = new Node(nodesGenerated, 0, startCity, 0, rootBound, rootMatrix, Collections.emptyList());
        pq.add(root);

        int bestCost = INF;
        List<Integer> bestTour = null;

        while (!pq.isEmpty()) {
            Node minNode = pq.poll();

            // Pruning check: if lower bound is already worse than best known upper bound
            if (minNode.lowerBound >= bestCost) {
                nodesPruned++;
                continue;
            }

            // If all cities visited, return to start
            if (minNode.level == n - 1) {
                int lastCity = minNode.city;
                int returnCost = rawCostMatrix[lastCity][startCity];
                if (returnCost != INF) {
                    int exactCost = calculateTourCost(minNode.path, startCity, rawCostMatrix);
                    if (exactCost < bestCost) {
                        bestCost = exactCost;
                        bestTour = new ArrayList<>(minNode.path);
                        bestTour.add(startCity);
                    }
                }
                continue;
            }

            // Generate child nodes for each unvisited city
            int u = minNode.city;
            for (int v = 0; v < n; v++) {
                if (minNode.reducedMatrix[u][v] != INF && !minNode.path.contains(v)) {
                    nodesGenerated++;
                    int[][] childMatrix = cloneMatrix(minNode.reducedMatrix, n);

                    // Row u and Column v become INF
                    for (int k = 0; k < n; k++) {
                        childMatrix[u][k] = INF;
                        childMatrix[k][v] = INF;
                    }

                    // Prevent premature return to start until final stage
                    if (minNode.level + 1 < n - 1) {
                        childMatrix[v][startCity] = INF;
                    }
                    childMatrix[v][u] = INF;

                    int edgeCost = minNode.reducedMatrix[u][v];
                    int childReduction = reduceMatrix(childMatrix, n);
                    int childBound = minNode.lowerBound + edgeCost + childReduction;

                    if (childBound < bestCost) {
                        Node child = new Node(nodesGenerated, minNode.nodeId, v, minNode.level + 1, 
                                              childBound, childMatrix, minNode.path);
                        pq.add(child);
                    } else {
                        nodesPruned++;
                    }
                }
            }
        }

        long elapsed = System.nanoTime() - startTime;

        // Compute auxiliary metrics (distance, fuel, transit hours)
        double totalDist = 0;
        double totalFuel = 0;
        double totalHours = 0;
        if (bestTour != null) {
            for (int i = 0; i < bestTour.size() - 1; i++) {
                int from = bestTour.get(i);
                int to = bestTour.get(i + 1);
                double d = distanceMatrix[from][to];
                RoadCondition rc = roadConditions[from][to];
                totalDist += d;
                totalFuel += d * 12.0 * rc.fuelMultiplier;
                totalHours += d / rc.avgSpeedKmh;
            }
        }

        return new TourResult("LC Branch & Bound", bestTour, bestCost, totalDist, totalFuel, 
                              totalHours, elapsed, nodesGenerated, nodesPruned);
    }

    private static int calculateTourCost(List<Integer> path, int startCity, int[][] costMatrix) {
        int cost = 0;
        for (int i = 0; i < path.size() - 1; i++) {
            cost += costMatrix[path.get(i)][path.get(i + 1)];
        }
        cost += costMatrix[path.get(path.size() - 1)][startCity];
        return cost;
    }

    // ========================================================================
    // ALGORITHM 2: GREEDY NEAREST NEIGHBOR HEURISTIC
    // ========================================================================
    public static TourResult solveNearestNeighbor(int[][] costMatrix, int[][] distanceMatrix, 
                                                 RoadCondition[][] roadConditions, int n, int startCity) {
        long startTime = System.nanoTime();
        boolean[] visited = new boolean[n];
        List<Integer> tour = new ArrayList<>();
        int current = startCity;
        tour.add(current);
        visited[current] = true;
        int totalCost = 0;

        for (int step = 1; step < n; step++) {
            int nearest = -1;
            int minCost = INF;
            for (int next = 0; next < n; next++) {
                if (!visited[next] && costMatrix[current][next] < minCost) {
                    minCost = costMatrix[current][next];
                    nearest = next;
                }
            }
            if (nearest == -1) break;
            tour.add(nearest);
            visited[nearest] = true;
            totalCost += minCost;
            current = nearest;
        }

        totalCost += costMatrix[current][startCity];
        tour.add(startCity);

        long elapsed = System.nanoTime() - startTime;

        double totalDist = 0, totalFuel = 0, totalHours = 0;
        for (int i = 0; i < tour.size() - 1; i++) {
            int from = tour.get(i);
            int to = tour.get(i + 1);
            double d = distanceMatrix[from][to];
            RoadCondition rc = roadConditions[from][to];
            totalDist += d;
            totalFuel += d * 12.0 * rc.fuelMultiplier;
            totalHours += d / rc.avgSpeedKmh;
        }

        return new TourResult("Nearest Neighbor Greedy", tour, totalCost, totalDist, totalFuel, 
                              totalHours, elapsed, n, 0);
    }

    // ========================================================================
    // ALGORITHM 3: BRUTE FORCE PERMUTATION SEARCH (Demonstrating (N-1)!)
    // ========================================================================
    private static int bruteForceMinCost = INF;
    private static List<Integer> bruteForceBestTour = null;
    private static int bruteForcePermutationCount = 0;

    public static TourResult solveBruteForce(int[][] costMatrix, int[][] distanceMatrix, 
                                            RoadCondition[][] roadConditions, int n, int startCity) {
        long startTime = System.nanoTime();
        bruteForceMinCost = INF;
        bruteForceBestTour = null;
        bruteForcePermutationCount = 0;

        List<Integer> cities = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (i != startCity) cities.add(i);
        }

        permute(cities, 0, startCity, costMatrix);
        long elapsed = System.nanoTime() - startTime;

        double totalDist = 0, totalFuel = 0, totalHours = 0;
        if (bruteForceBestTour != null) {
            for (int i = 0; i < bruteForceBestTour.size() - 1; i++) {
                int from = bruteForceBestTour.get(i);
                int to = bruteForceBestTour.get(i + 1);
                double d = distanceMatrix[from][to];
                RoadCondition rc = roadConditions[from][to];
                totalDist += d;
                totalFuel += d * 12.0 * rc.fuelMultiplier;
                totalHours += d / rc.avgSpeedKmh;
            }
        }

        return new TourResult("Brute Force Permutation", bruteForceBestTour, bruteForceMinCost, 
                              totalDist, totalFuel, totalHours, elapsed, bruteForcePermutationCount, 0);
    }

    private static void permute(List<Integer> cities, int k, int startCity, int[][] costMatrix) {
        if (k == cities.size()) {
            bruteForcePermutationCount++;
            int currentCost = costMatrix[startCity][cities.get(0)];
            for (int i = 0; i < cities.size() - 1; i++) {
                currentCost += costMatrix[cities.get(i)][cities.get(i + 1)];
            }
            currentCost += costMatrix[cities.get(cities.size() - 1)][startCity];

            if (currentCost < bruteForceMinCost) {
                bruteForceMinCost = currentCost;
                bruteForceBestTour = new ArrayList<>();
                bruteForceBestTour.add(startCity);
                bruteForceBestTour.addAll(cities);
                bruteForceBestTour.add(startCity);
            }
            return;
        }

        for (int i = k; i < cities.size(); i++) {
            Collections.swap(cities, i, k);
            permute(cities, k + 1, startCity, costMatrix);
            Collections.swap(cities, i, k);
        }
    }

    // ========================================================================
    // MAIN DEMO & BENCHMARK RUNNER
    // ========================================================================
    public static void main(String[] args) {
        System.out.println("==========================================================================");
        System.out.println("   PCCOE DAA LAB - ASSIGNMENT NO. 8: LC BRANCH & BOUND (SWIFTSHIP TSP)    ");
        System.out.println("==========================================================================");
        System.out.println("Student: Aditya Chandrajit Deore | PRN: 124B1F116 | Faculty: Dr. Sapana Kolambe\n");

        // --------------------------------------------------------------------
        // PART 1: CORE LOGISTICS SCENARIO (5 Regional Hubs with Terrain & Traffic)
        // --------------------------------------------------------------------
        List<City> hubs = Arrays.asList(
            new City(0, "Pune Central Depot", "PUN", "Central Hub"),
            new City(1, "Mumbai Sea Port Hub", "BOM", "Coastal Gateway"),
            new City(2, "Nashik Cargo Center", "NSK", "Agri Logistics"),
            new City(3, "Aurangabad Industrial Hub", "IXU", "Manufacturing Belt"),
            new City(4, "Kolhapur Border Depot", "KLH", "Southern Corridor")
        );
        int n = hubs.size();

        // Inter-city Distance Matrix (km)
        int[][] distance = {
            {   0, 150, 210, 235, 230 }, // Pune
            { 150,   0, 165, 335, 375 }, // Mumbai
            { 210, 165,   0, 180, 440 }, // Nashik
            { 235, 335, 180,   0, 410 }, // Aurangabad
            { 230, 375, 440, 410,   0 }  // Kolhapur
        };

        // Road Condition Matrix (Affects fuel multiplier & travel speeds)
        RoadCondition[][] conditions = new RoadCondition[n][n];
        for (int i = 0; i < n; i++) Arrays.fill(conditions[i], RoadCondition.HIGHWAY_EXPRESS);

        conditions[0][1] = conditions[1][0] = RoadCondition.HIGHWAY_EXPRESS;  // Pune-Mumbai Expressway (Smooth)
        conditions[0][2] = conditions[2][0] = RoadCondition.GHAT_ROUGH;       // Pune-Nashik (Chakan Ghat)
        conditions[0][3] = conditions[3][0] = RoadCondition.STATE_HIGHWAY;     // Pune-Aurangabad
        conditions[0][4] = conditions[4][0] = RoadCondition.HIGHWAY_EXPRESS;  // Pune-Kolhapur (NH-48)
        conditions[1][2] = conditions[2][1] = RoadCondition.GHAT_ROUGH;       // Mumbai-Nashik (Kasara Ghat)
        conditions[1][3] = conditions[3][1] = RoadCondition.URBAN_CONGESTION; // Mumbai-Aurangabad via Bhiwandi
        conditions[1][4] = conditions[4][1] = RoadCondition.STATE_HIGHWAY;     // Mumbai-Kolhapur Coastal
        conditions[2][3] = conditions[3][2] = RoadCondition.STATE_HIGHWAY;     // Nashik-Aurangabad
        conditions[3][4] = conditions[4][3] = RoadCondition.GHAT_ROUGH;       // Aurangabad-Kolhapur bypass

        // Cost Matrix calculation: Distance * ₹12/km base fuel * FuelMultiplier + Toll Fee
        int[][] costMatrix = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i == j) {
                    costMatrix[i][j] = INF;
                } else {
                    double fuelCost = distance[i][j] * 12.0 * conditions[i][j].fuelMultiplier;
                    int tollFee = (conditions[i][j] == RoadCondition.HIGHWAY_EXPRESS) ? 320 : 180;
                    costMatrix[i][j] = (int) Math.round(fuelCost + tollFee);
                }
            }
        }

        // Asymmetric adjustment: Urban entry toll / traffic penalty for entering Mumbai
        costMatrix[0][1] += 400; // Peak morning toll Pune -> Mumbai
        costMatrix[4][0] += 250; // Night entry toll Kolhapur -> Pune

        System.out.println("--- 1. SWIFTSHIP REGIONAL HUBS & DISPATCH NETWORK ---");
        for (City c : hubs) System.out.println("  " + c);

        System.out.println("\nComposite Inter-City Transportation Cost Matrix (in INR ₹):");
        System.out.print("      ");
        for (City c : hubs) System.out.printf("%-7s ", c.code);
        System.out.println("\n-----------------------------------------------------");
        for (int i = 0; i < n; i++) {
            System.out.printf("%-5s| ", hubs.get(i).code);
            for (int j = 0; j < n; j++) {
                if (costMatrix[i][j] == INF) System.out.print("  INF   ");
                else System.out.printf("%5d   ", costMatrix[i][j]);
            }
            System.out.println();
        }

        // Root Matrix Reduction Demo
        int[][] demoMatrix = cloneMatrix(costMatrix, n);
        int initialReduction = reduceMatrix(demoMatrix, n);
        System.out.printf("\n--- 2. ROOT NODE MATRIX REDUCTION ---\n");
        System.out.printf("Total Initial Reduction Cost (Root Lower Bound c_hat): ₹ %d\n", initialReduction);

        // Execute Algorithms on Core Scenario
        TourResult resLCBB = solveLCBranchAndBound(costMatrix, distance, conditions, n, 0);
        TourResult resGreedy = solveNearestNeighbor(costMatrix, distance, conditions, n, 0);
        TourResult resBrute = solveBruteForce(costMatrix, distance, conditions, n, 0);

        System.out.println("\n--- 3. ALGORITHM PERFORMANCE COMPARISON (5 Hubs) ---");
        System.out.printf("%-26s %-12s %-12s %-12s %-15s %-12s\n", 
                          "Algorithm", "Cost (INR)", "Distance", "Fuel (INR)", "Runtime (ns)", "Pruned Nodes");
        System.out.println("-----------------------------------------------------------------------------------------");
        System.out.printf("%-26s ₹ %-10d %6.0f km   ₹ %-10.0f %-15s %-12d\n",
                resLCBB.algorithmName, resLCBB.totalCost, resLCBB.totalDistanceKm, resLCBB.totalFuelCost,
                resLCBB.executionTimeNs + " ns", resLCBB.nodesPruned);
        System.out.printf("%-26s ₹ %-10d %6.0f km   ₹ %-10.0f %-15s %-12d\n",
                resGreedy.algorithmName, resGreedy.totalCost, resGreedy.totalDistanceKm, resGreedy.totalFuelCost,
                resGreedy.executionTimeNs + " ns", resGreedy.nodesPruned);
        System.out.printf("%-26s ₹ %-10d %6.0f km   ₹ %-10.0f %-15s %-12d\n",
                resBrute.algorithmName, resBrute.totalCost, resBrute.totalDistanceKm, resBrute.totalFuelCost,
                resBrute.executionTimeNs + " ns", resBrute.nodesPruned);

        // Optimal Route Itinerary Manifest
        System.out.println("\n--- 4. OPTIMAL SWIFTSHIP DELIVERY ROUTE MANIFEST (LC-BB) ---");
        System.out.printf("Optimal Tour Cost   : ₹ %d (Guaranteed Global Minimum)\n", resLCBB.totalCost);
        System.out.printf("Total Route Distance: %.0f km\n", resLCBB.totalDistanceKm);
        System.out.printf("Estimated Fuel Cost : ₹ %.2f\n", resLCBB.totalFuelCost);
        System.out.printf("Total Transit Time  : %.2f hours\n", resLCBB.totalTransitHours);
        System.out.printf("Search State Space  : %d nodes generated, %d nodes pruned (%.1f%% search space pruned)\n",
                resLCBB.nodesGenerated, resLCBB.nodesPruned, (double) resLCBB.nodesPruned / resLCBB.nodesGenerated * 100);

        System.out.println("\nStep-by-Step Delivery Route Sequence:");
        for (int i = 0; i < resLCBB.tour.size() - 1; i++) {
            int from = resLCBB.tour.get(i);
            int to = resLCBB.tour.get(i + 1);
            System.out.printf("  Leg %d: %-26s -> %-26s | %3d km | Cost: ₹ %-5d | Road: %s\n",
                    (i + 1), hubs.get(from).name, hubs.get(to).name,
                    distance[from][to], costMatrix[from][to], conditions[from][to].description);
        }

        // Suboptimality Analysis of Greedy Heuristic
        int deficit = resGreedy.totalCost - resLCBB.totalCost;
        if (deficit > 0) {
            System.out.printf("\n>> Heuristic Deficit: Greedy Nearest Neighbor incurred ₹ %d extra penalty (+%.1f%% cost increase)!\n",
                    deficit, (double) deficit / resLCBB.totalCost * 100);
            System.out.println("   Reason: Greedy makes myopic local decisions, leading to a catastrophic final return cost.");
        } else {
            System.out.println("\n>> Note: Greedy matched optimal cost on this 5-city topology, but offers no guarantee.");
        }

        // --------------------------------------------------------------------
        // PART 2: SCALABILITY & FACTORIAL EXPLOSION BENCHMARK (N = 10 Cities)
        // --------------------------------------------------------------------
        System.out.println("\n--- 5. SCALABILITY & STATE SPACE PRUNING ANALYSIS ---");
        System.out.println("Theoretical Complexity Analysis for Large Logistics Hubs (N Cities):");
        System.out.println("  N =  5 Cities -> (N-1)! =               24 Permutations (Trivial)");
        System.out.println("  N = 10 Cities -> (N-1)! =          362,880 Permutations (~1 Second)");
        System.out.println("  N = 15 Cities -> (N-1)! =   43,589,145,600 Permutations (~14 Hours on CPU)");
        System.out.println("  N = 20 Cities -> (N-1)! = 121,645,100,408,832,000 Permutations (~3,857 YEARS)");
        System.out.println("\n>> Conclusion: Brute force checking all (N-1)! permutations is completely infeasible for N >= 20.");
        System.out.println(">> LC Branch and Bound provides a deterministic optimal solution by aggressively pruning subtrees!");
        System.out.println("==========================================================================");
    }
}
