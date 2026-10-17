import java.util.*;

/**
 * ============================================================================
 * DISASTER RELIEF RESOURCE ALLOCATION OPTIMIZER
 * 0/1 Knapsack Approach using Dynamic Programming
 * ============================================================================
 * Course     : Design & Analysis of Algorithms Laboratory (BIT25PC04)
 * Student    : Aditya Chandrajit Deore
 * PRN        : 124B1F116
 * College    : Pimpri Chinchwad College of Engineering (PCCOE)
 * Faculty    : Dr. Sapana Kolambe
 *
 * Problem Description:
 * A massive earthquake has struck a remote region. A relief truck with payload
 * capacity W kg must be loaded from N available relief supply items to maximize
 * total humanitarian life-saving utility without exceeding weight limits.
 *
 * Key Implementations:
 * 1. Classical 0/1 Knapsack 2D Dynamic Programming with exact item backtracking
 * 2. Space-Optimized 1D Dynamic Programming (Theta(W) auxiliary space)
 * 3. Greedy Value-to-Weight Ratio Heuristic (Demonstrating 0/1 suboptimality)
 * 4. Brute Force Exhaustive Recursive Search (Demonstrating O(2^N) complexity)
 * 5. Priority & Perishable Goods Constraint Optimization
 * 6. Multi-Truck Fleet Dispatch Allocation (Multiple Knapsack Problem Heuristic)
 * ============================================================================
 */
public class DisasterReliefKnapsack {

    // ------------------------------------------------------------------------
    // DATA MODEL: Relief Supply Item
    // ------------------------------------------------------------------------
    public static class ReliefItem {
        private final int id;
        private final String name;
        private final String category;
        private final int weight;      // in kg
        private final int utility;     // humanitarian life-saving score (1-100)
        private final boolean perishable; // requires immediate transport (plasma, baby milk)
        private final double urgencyMultiplier; // priority weight factor

        public ReliefItem(int id, String name, String category, int weight, int utility, 
                          boolean perishable, double urgencyMultiplier) {
            this.id = id;
            this.name = name;
            this.category = category;
            this.weight = weight;
            this.utility = utility;
            this.perishable = perishable;
            this.urgencyMultiplier = urgencyMultiplier;
        }

        public int getId() { return id; }
        public String getName() { return name; }
        public String getCategory() { return category; }
        public int getWeight() { return weight; }
        public int getUtility() { return utility; }
        public boolean isPerishable() { return perishable; }
        public double getUrgencyMultiplier() { return urgencyMultiplier; }

        public double getRatio() {
            return (double) utility / weight;
        }

        public int getEffectiveUtility() {
            return (int) Math.round(utility * urgencyMultiplier);
        }

        @Override
        public String toString() {
            return String.format("#%-2d %-34s [%-10s] | %2d kg | Util: %2d | P-Util: %3d | Perish: %s",
                    id, name, category, weight, utility, getEffectiveUtility(), perishable ? "YES" : "No ");
        }
    }

    // ------------------------------------------------------------------------
    // RESULT CONTAINER: Solution Metrics
    // ------------------------------------------------------------------------
    public static class SolutionReport {
        public final String algorithmName;
        public final int totalUtility;
        public final int totalWeight;
        public final int capacity;
        public final List<ReliefItem> packedItems;
        public final long executionTimeNs;
        public int recursiveCallsCount = 0;

        public SolutionReport(String algorithmName, int totalUtility, int totalWeight, 
                              int capacity, List<ReliefItem> packedItems, long executionTimeNs) {
            this.algorithmName = algorithmName;
            this.totalUtility = totalUtility;
            this.totalWeight = totalWeight;
            this.capacity = capacity;
            this.packedItems = packedItems;
            this.executionTimeNs = executionTimeNs;
        }

        public double getCapacityUtilization() {
            return (double) totalWeight / capacity * 100.0;
        }
    }

    // ========================================================================
    // ALGORITHM 1: 0/1 Knapsack 2D Dynamic Programming (Optimal Global Solver)
    // Time Complexity  : Theta(N * W)
    // Space Complexity : Theta(N * W)
    // ========================================================================
    public static SolutionReport solveDynamicProgramming(List<ReliefItem> items, int capacity, boolean applyPriority) {
        long startTime = System.nanoTime();
        int n = items.size();
        int[][] dp = new int[n + 1][capacity + 1];

        // 1. Build DP Matrix Tabular Bottom-Up
        for (int i = 1; i <= n; i++) {
            ReliefItem item = items.get(i - 1);
            int value = applyPriority ? item.getEffectiveUtility() : item.getUtility();
            int wt = item.getWeight();

            for (int w = 0; w <= capacity; w++) {
                if (wt <= w) {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - wt] + value);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        // 2. Backtrack to reconstruct exactly which items were included
        List<ReliefItem> selected = new ArrayList<>();
        int w = capacity;
        for (int i = n; i > 0 && dp[i][w] > 0; i--) {
            if (dp[i][w] != dp[i - 1][w]) {
                ReliefItem chosenItem = items.get(i - 1);
                selected.add(chosenItem);
                w -= chosenItem.getWeight();
            }
        }
        Collections.reverse(selected);

        long duration = System.nanoTime() - startTime;
        int packedWeight = capacity - w;
        int maxUtility = dp[n][capacity];

        return new SolutionReport("Dynamic Programming (0/1 DP)", maxUtility, packedWeight, capacity, selected, duration);
    }

    // ========================================================================
    // ALGORITHM 2: Space-Optimized Dynamic Programming
    // Time Complexity  : Theta(N * W)
    // Space Complexity : Theta(W)
    // ========================================================================
    public static int solveSpaceOptimizedDP(List<ReliefItem> items, int capacity) {
        int[] dp = new int[capacity + 1];
        for (ReliefItem item : items) {
            int wt = item.getWeight();
            int val = item.getUtility();
            // Traverse backward to preserve previous item state
            for (int w = capacity; w >= wt; w--) {
                dp[w] = Math.max(dp[w], dp[w - wt] + val);
            }
        }
        return dp[capacity];
    }

    // ========================================================================
    // ALGORITHM 3: Greedy Heuristic (Sorted by Value-to-Weight Ratio)
    // Time Complexity  : O(N log N)
    // Space Complexity : O(1) auxiliary
    // Note: Fails for 0/1 knapsack because fractional split is impossible!
    // ========================================================================
    public static SolutionReport solveGreedy(List<ReliefItem> items, int capacity) {
        long startTime = System.nanoTime();
        List<ReliefItem> sorted = new ArrayList<>(items);
        // Sort descending by ratio (v_i / w_i)
        sorted.sort((a, b) -> Double.compare(b.getRatio(), a.getRatio()));

        int currentWeight = 0;
        int currentUtility = 0;
        List<ReliefItem> selected = new ArrayList<>();

        for (ReliefItem item : sorted) {
            if (currentWeight + item.getWeight() <= capacity) {
                selected.add(item);
                currentWeight += item.getWeight();
                currentUtility += item.getUtility();
            }
        }

        long duration = System.nanoTime() - startTime;
        return new SolutionReport("Greedy (Utility/Weight Ratio)", currentUtility, currentWeight, capacity, selected, duration);
    }

    // ========================================================================
    // ALGORITHM 4: Brute Force Exhaustive Search
    // Time Complexity  : O(2^N)
    // Space Complexity : O(N) recursion stack
    // ========================================================================
    private static int bruteForceCallCount = 0;

    public static SolutionReport solveBruteForce(List<ReliefItem> items, int capacity) {
        long startTime = System.nanoTime();
        bruteForceCallCount = 0;
        List<ReliefItem> bestCombo = new ArrayList<>();
        int[] maxUtil = new int[]{0};

        branchAndBound(items, 0, capacity, 0, new ArrayList<>(), maxUtil, bestCombo);

        long duration = System.nanoTime() - startTime;
        int totalWeight = bestCombo.stream().mapToInt(ReliefItem::getWeight).sum();
        SolutionReport report = new SolutionReport("Brute Force (Exhaustive)", maxUtil[0], totalWeight, capacity, bestCombo, duration);
        report.recursiveCallsCount = bruteForceCallCount;
        return report;
    }

    private static void branchAndBound(List<ReliefItem> items, int index, int remCap, int curUtil,
                                       List<ReliefItem> currentList, int[] maxUtil, List<ReliefItem> bestCombo) {
        bruteForceCallCount++;
        if (index == items.size() || remCap == 0) {
            if (curUtil > maxUtil[0]) {
                maxUtil[0] = curUtil;
                bestCombo.clear();
                bestCombo.addAll(currentList);
            }
            return;
        }

        ReliefItem item = items.get(index);
        // Decision 1: Include item (if it fits)
        if (item.getWeight() <= remCap) {
            currentList.add(item);
            branchAndBound(items, index + 1, remCap - item.getWeight(), curUtil + item.getUtility(), currentList, maxUtil, bestCombo);
            currentList.remove(currentList.size() - 1); // backtrack
        }
        // Decision 2: Exclude item
        branchAndBound(items, index + 1, remCap, curUtil, currentList, maxUtil, bestCombo);
    }

    // ========================================================================
    // EXTENSION: Multi-Truck Fleet Dispatch (Multiple Knapsack Problem Heuristic)
    // ========================================================================
    public static Map<String, SolutionReport> solveMultiTruckFleet(List<ReliefItem> items, int[] fleetCapacities) {
        Map<String, SolutionReport> fleetManifest = new LinkedHashMap<>();
        List<ReliefItem> remainingStock = new ArrayList<>(items);

        for (int k = 0; k < fleetCapacities.length; k++) {
            int truckCap = fleetCapacities[k];
            String truckTitle = String.format("Relief Truck #%d [Cap: %d kg]", (k + 1), truckCap);
            SolutionReport truckPlan = solveDynamicProgramming(remainingStock, truckCap, false);
            fleetManifest.put(truckTitle, truckPlan);
            remainingStock.removeAll(truckPlan.packedItems);
        }
        return fleetManifest;
    }

    // ========================================================================
    // VISUAL CONSOLE PRINTER (Clean Dashboard with Box Drawing)
    // ========================================================================
    public static void printBoxHeader(String title) {
        System.out.println("+==============================================================================+");
        System.out.printf("| %-76s |\n", title);
        System.out.println("+==============================================================================+");
    }

    public static void printSectionDivider(String title) {
        System.out.println("\n--------------------------------------------------------------------------------");
        System.out.println("  " + title);
        System.out.println("--------------------------------------------------------------------------------");
    }

    // ========================================================================
    // CONCISE 0/1 KNAPSACK DP SOLVER (Matching Report Section 7 & 8)
    // ========================================================================
    public static void knapsack01DP(ReliefItem[] items, int capacity) {
        int n = items.length;
        int[][] dp = new int[n + 1][capacity + 1];

        // 1. Build DP Table Bottom-Up
        for (int i = 1; i <= n; i++) {
            int wt = items[i - 1].weight;
            int val = items[i - 1].utility;

            for (int w = 0; w <= capacity; w++) {
                if (wt <= w) {
                    dp[i][w] = Math.max(dp[i - 1][w], dp[i - 1][w - wt] + val);
                } else {
                    dp[i][w] = dp[i - 1][w];
                }
            }
        }

        // 2. Backtracking to identify selected items
        List<ReliefItem> selected = new ArrayList<>();
        int w = capacity;
        for (int i = n; i > 0 && dp[i][w] > 0; i--) {
            if (dp[i][w] != dp[i - 1][w]) {
                selected.add(items[i - 1]);
                w -= items[i - 1].weight;
            }
        }
        Collections.reverse(selected);

        // Display results
        int totalWeight = capacity - w;
        int totalUtility = dp[n][capacity];

        System.out.println("\n===== DISASTER RELIEF RESOURCE ALLOCATION (0/1 KNAPSACK DP) =====");
        System.out.println("Maximum Truck Payload Capacity : " + capacity + " kg\n");
        System.out.printf("%-4s %-34s %-12s %-10s %-10s\n", "ID", "Relief Item", "Category", "Weight", "Utility");
        System.out.println("--------------------------------------------------------------------------");
        for (ReliefItem item : selected) {
            System.out.printf("#%-3d %-34s %-12s %2d kg     %-10d\n",
                    item.id, item.name, item.category, item.weight, item.utility);
        }
        System.out.println("--------------------------------------------------------------------------");
        System.out.println("Payload Used          : " + totalWeight + " kg");
        System.out.println("Remaining Capacity    : " + (capacity - totalWeight) + " kg");
        System.out.printf("Capacity Utilization  : %.1f%%\n", (double) totalWeight / capacity * 100.0);
        System.out.println("Total Utility Value   : " + totalUtility);
    }

    // ========================================================================
    // MAIN BENCHMARK & DEMONSTRATION RUNNER
    // ========================================================================
    public static void main(String[] args) {
        int truckCapacity = 100; // Single emergency truck maximum weight limit

        // Array for Section 7 concise solver
        ReliefItem[] itemArray = {
            new ReliefItem(1, "Trauma & Surgical First Aid Kits", "Medical", 12, 50, false, 1.5),
            new ReliefItem(2, "Blood Plasma & Cold Vaccines", "Medical", 15, 70, true, 2.0),
            new ReliefItem(3, "Field Water Purification Units", "Sanitation", 25, 80, false, 1.4),
            new ReliefItem(4, "Ready-to-Eat Emergency Rations", "Nutrition", 20, 55, false, 1.2),
            new ReliefItem(5, "Infant Formula & Pediatric Milk", "Nutrition", 10, 45, true, 1.8),
            new ReliefItem(6, "Weatherproof Shelter Tents", "Shelter", 30, 60, false, 1.0),
            new ReliefItem(7, "Satellite Comms & GPS Transceiver", "Comms", 8, 40, false, 1.4),
            new ReliefItem(8, "Portable Generator & Fuel Canister", "Power", 35, 75, false, 1.1),
            new ReliefItem(9, "Thermal Emergency Blankets Pack", "Shelter", 18, 35, false, 1.0),
            new ReliefItem(10, "Hydraulic Rescue Extraction Cutter", "Rescue", 28, 65, false, 1.3)
        };

        // Primary 0/1 DP Execution
        knapsack01DP(itemArray, truckCapacity);

        printBoxHeader("DISASTER RELIEF LOGISTICS OPTIMIZATION (0/1 KNAPSACK SYSTEM)");
        System.out.println("Course  : Design & Analysis of Algorithms Laboratory (BIT25PC04)");
        System.out.println("Student : Aditya Chandrajit Deore | PRN: 124B1F116 | PCCOE Pune");
        System.out.println("Faculty : Dr. Sapana Kolambe");

        List<ReliefItem> inventory = Arrays.asList(itemArray);

        // 1. Inventory Catalog Display
        printSectionDivider("[STAGE 1] WAREHOUSE EMERGENCY INVENTORY (Capacity W = " + truckCapacity + " kg)");
        System.out.printf("%-4s %-36s %-12s %-8s %-8s %-8s %-11s %-8s\n",
                "ID", "Item Description", "Category", "Weight", "Utility", "Ratio", "Perishable", "Urgency");
        System.out.println("--------------------------------------------------------------------------------");
        for (ReliefItem item : inventory) {
            System.out.printf("#%-3d %-36s %-12s %2d kg   %-8d %-8.2f %-11s %3.1fx\n",
                    item.getId(), item.getName(), item.getCategory(), item.getWeight(), item.getUtility(),
                    item.getRatio(), item.isPerishable() ? "YES [CRIT]" : "No", item.getUrgencyMultiplier());
        }

        // 2. Dynamic Programming Optimal Execution
        printSectionDivider("[STAGE 2] DYNAMIC PROGRAMMING OPTIMAL ALLOCATION (Standard 0/1 DP)");
        SolutionReport dpPlan = solveDynamicProgramming(inventory, truckCapacity, false);
        System.out.println("Optimization Status   : OPTIMAL GLOBAL SOLUTION ATTAINED");
        System.out.printf("Total Utility Achieved: %d humanitarian points\n", dpPlan.totalUtility);
        System.out.printf("Gross Payload Loaded  : %d / %d kg (%.1f%% payload efficiency)\n", 
                dpPlan.totalWeight, dpPlan.capacity, dpPlan.getCapacityUtilization());
        System.out.printf("Execution Compute Time: %d ns (~%.3f ms)\n", 
                dpPlan.executionTimeNs, dpPlan.executionTimeNs / 1_000_000.0);
        
        System.out.println("\nLoaded Relief Supplies Manifest:");
        for (ReliefItem it : dpPlan.packedItems) {
            System.out.println("  [+] " + it);
        }

        // Verification with Space-Optimized DP
        int spaceOptUtility = solveSpaceOptimizedDP(inventory, truckCapacity);
        System.out.printf("\nSpace-Optimized 1D DP Verification: %d points (Exact Match: %b)\n",
                spaceOptUtility, (spaceOptUtility == dpPlan.totalUtility));

        // 3. Greedy Heuristic Comparison
        printSectionDivider("[STAGE 3] GREEDY ALGORITHM BENCHMARK (Sorting by Utility/Weight Ratio)");
        SolutionReport greedyPlan = solveGreedy(inventory, truckCapacity);
        int utilityLoss = dpPlan.totalUtility - greedyPlan.totalUtility;
        double lossPercent = (double) utilityLoss / dpPlan.totalUtility * 100.0;
        
        System.out.printf("Greedy Utility Achieved: %d points\n", greedyPlan.totalUtility);
        System.out.printf("Greedy Payload Utilized: %d / %d kg (%d kg payload unutilized!)\n", 
                greedyPlan.totalWeight, greedyPlan.capacity, (truckCapacity - greedyPlan.totalWeight));
        System.out.printf("Suboptimality Deficit  : -%d points (-%.2f%% loss compared to DP)\n", utilityLoss, lossPercent);
        System.out.println("Items Chosen by Greedy:");
        for (ReliefItem it : greedyPlan.packedItems) {
            System.out.println("  [-] " + it);
        }
        System.out.println("Analysis: Greedy failed because 0/1 knapsack cannot accept partial items, leaving capacity gaps.");

        // 4. Brute Force Benchmark
        printSectionDivider("[STAGE 4] BRUTE FORCE EXHAUSTIVE RECURSION BENCHMARK (O(2^N))");
        SolutionReport bfPlan = solveBruteForce(inventory, truckCapacity);
        System.out.printf("Brute Force Utility    : %d points (Matches DP: %b)\n", bfPlan.totalUtility, (bfPlan.totalUtility == dpPlan.totalUtility));
        System.out.printf("Total Recursive Calls  : %d calls (Theoretical 2^10 = 1,024 evaluations)\n", bfPlan.recursiveCallsCount);
        System.out.printf("Execution Compute Time : %d ns (~%.3f ms)\n", bfPlan.executionTimeNs, bfPlan.executionTimeNs / 1_000_000.0);

        // 5. Performance Comparison Matrix Table
        printSectionDivider("[STAGE 5] ALGORITHMIC COMPLEXITY & PERFORMANCE COMPARISON");
        System.out.printf("%-18s %-14s %-12s %-12s %-14s %-12s\n", 
                "Algorithm", "Time Comp.", "Space Comp.", "Utility", "Payload (kg)", "Optimality");
        System.out.println("--------------------------------------------------------------------------------");
        System.out.printf("%-18s %-14s %-12s %-12d %-14s %-12s\n",
                "Brute Force", "O(2^N)", "O(N)", bfPlan.totalUtility, bfPlan.totalWeight + "/" + truckCapacity, "Optimal");
        System.out.printf("%-18s %-14s %-12s %-12d %-14s %-12s\n",
                "Greedy Heuristic", "O(N log N)", "O(1)", greedyPlan.totalUtility, greedyPlan.totalWeight + "/" + truckCapacity, "Suboptimal");
        System.out.printf("%-18s %-14s %-12s %-12d %-14s %-12s\n",
                "Dynamic Prog 2D", "Theta(N*W)", "Theta(N*W)", dpPlan.totalUtility, dpPlan.totalWeight + "/" + truckCapacity, "Optimal");
        System.out.printf("%-18s %-14s %-12s %-12d %-14s %-12s\n",
                "Dynamic Prog 1D", "Theta(N*W)", "Theta(W)", spaceOptUtility, dpPlan.totalWeight + "/" + truckCapacity, "Optimal");

        // 6. Real-World Priority & Perishable Optimization
        printSectionDivider("[STAGE 6] REAL-WORLD OPTIMIZATION: PERISHABLE MEDICAL SUPPLIES");
        SolutionReport priorityPlan = solveDynamicProgramming(inventory, truckCapacity, true);
        System.out.printf("Weighted Priority Util: %d points\n", priorityPlan.totalUtility);
        System.out.printf("Payload Allocated     : %d / %d kg\n", priorityPlan.totalWeight, priorityPlan.capacity);
        System.out.println("Prioritized Manifest for Emergency Flight/Truck:");
        for (ReliefItem it : priorityPlan.packedItems) {
            System.out.printf("  [*] #%-2d %-34s | Base: %2d -> Boosted: %3d | Perish: %s\n",
                    it.getId(), it.getName(), it.getUtility(), it.getEffectiveUtility(), it.isPerishable() ? "YES [SECURED]" : "No");
        }

        // 7. Multi-Truck Fleet Dispatch (Multiple Knapsack)
        printSectionDivider("[STAGE 7] MULTI-TRUCK RELIEF FLEET ALLOCATION (MKP DISPATCH)");
        int[] reliefFleet = new int[]{65, 55, 40}; // 3-truck convoy
        Map<String, SolutionReport> convoy = solveMultiTruckFleet(inventory, reliefFleet);
        int totalConvoyUtility = 0;
        int totalConvoyWeight = 0;

        for (Map.Entry<String, SolutionReport> truck : convoy.entrySet()) {
            SolutionReport trReport = truck.getValue();
            System.out.printf("\n>>> %s | Loaded: %d/%d kg | Utility: %d points\n", 
                    truck.getKey(), trReport.totalWeight, trReport.capacity, trReport.totalUtility);
            for (ReliefItem it : trReport.packedItems) {
                System.out.printf("    - #%-2d %-34s (%2d kg, Util: %2d)\n", it.getId(), it.getName(), it.getWeight(), it.getUtility());
            }
            totalConvoyUtility += trReport.totalUtility;
            totalConvoyWeight += trReport.totalWeight;
        }

        System.out.println("\n--------------------------------------------------------------------------------");
        System.out.printf("CONVOY SUMMARY: Delivered %d total utility points across %d kg payload using 3 trucks.\n",
                totalConvoyUtility, totalConvoyWeight);
        System.out.println("+==============================================================================+\n");
    }
}
