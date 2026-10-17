import java.util.*;
import javax.swing.*;
import java.awt.*;

public class SmartTraffic {

    // Edge represents a road
    static class Edge {
        int to;
        int weight;

        Edge(int to, int weight) {
            this.to = to;
            this.weight = weight;
        }
    }

    static ArrayList<Edge>[] graph;
    static int[] parent;

    // Add road
    static void addRoad(int u, int v, int weight) {
        graph[u].add(new Edge(v, weight));
    }

    // Dijkstra's Algorithm
    static int[] dijkstra(int source) {

        int n = graph.length;
        int[] distance = new int[n];
        parent = new int[n];

        Arrays.fill(distance, Integer.MAX_VALUE);
        Arrays.fill(parent, -1);

        PriorityQueue<int[]> pq =
                new PriorityQueue<>(
                        Comparator.comparingInt(a -> a[1])
                );

        distance[source] = 0;
        pq.add(new int[]{source, 0});

        while (!pq.isEmpty()) {

            int[] current = pq.poll();

            int u = current[0];
            int dist = current[1];

            if (dist > distance[u])
                continue;

            for (Edge edge : graph[u]) {

                int v = edge.to;
                int newDist = dist + edge.weight;

                if (newDist < distance[v]) {

                    distance[v] = newDist;
                    parent[v] = u;

                    pq.add(new int[]{v, newDist});
                }
            }
        }

        return distance;
    }

    // Print shortest path
    static void printPath(int source, int destination) {

        ArrayList<Integer> path = new ArrayList<>();

        int current = destination;

        while (current != -1) {
            path.add(current);
            current = parent[current];
        }

        Collections.reverse(path);

        System.out.print("Path: ");

        for (int i = 0; i < path.size(); i++) {

            System.out.print(path.get(i));

            if (i < path.size() - 1)
                System.out.print(" -> ");
        }
    }

    // Update road weight
    static void updateRoad(int u, int v, int newWeight) {

        for (Edge edge : graph[u]) {

            if (edge.to == v) {
                edge.weight = newWeight;
                return;
            }
        }
    }

    // Simple visualization
    static void showGraph(
            int[] path,
            int source,
            int hospital
    ) {

        JFrame frame = new JFrame(
                "Smart Traffic Management"
        );

        frame.setSize(900, 600);
        frame.setDefaultCloseOperation(
                JFrame.DISPOSE_ON_CLOSE
        );

        JPanel panel = new JPanel() {

            protected void paintComponent(Graphics g) {

                super.paintComponent(g);

                // Junction positions
                int[][] pos = {
                        {100, 250},
                        {250, 120},
                        {250, 380},
                        {450, 250},
                        {650, 120},
                        {650, 380}
                };

                // Draw roads
                g.setColor(Color.GRAY);

                for (int u = 0; u < graph.length; u++) {

                    for (Edge e : graph[u]) {

                        int x1 = pos[u][0];
                        int y1 = pos[u][1];

                        int x2 = pos[e.to][0];
                        int y2 = pos[e.to][1];

                        g.drawLine(x1, y1, x2, y2);
                    }
                }

                // Draw optimal path
                g.setColor(Color.RED);

                for (int i = 0; i < path.length - 1; i++) {

                    int u = path[i];
                    int v = path[i + 1];

                    g.drawLine(
                            pos[u][0],
                            pos[u][1],
                            pos[v][0],
                            pos[v][1]
                    );
                }

                // Draw junctions
                for (int i = 0; i < pos.length; i++) {

                    if (i == source)
                        g.setColor(Color.BLUE);

                    else if (i == hospital)
                        g.setColor(Color.GREEN);

                    else
                        g.setColor(Color.BLACK);

                    g.fillOval(
                            pos[i][0] - 15,
                            pos[i][1] - 15,
                            30,
                            30
                    );

                    g.setColor(Color.BLACK);

                    g.drawString(
                            "J" + i,
                            pos[i][0] - 5,
                            pos[i][1] - 20
                    );
                }

                g.setColor(Color.BLACK);

                g.drawString(
                        "Blue = Ambulance",
                        50,
                        50
                );

                g.drawString(
                        "Green = Hospital",
                        200,
                        50
                );

                g.drawString(
                        "Red = Shortest Path",
                        350,
                        50
                );
            }
        };

        frame.add(panel);
        frame.setVisible(true);
    }

    public static void main(String[] args) {

        int n = 6;

        graph = new ArrayList[n];

        for (int i = 0; i < n; i++)
            graph[i] = new ArrayList<>();

        /*
             Sample Road Dataset

             J0 = Ambulance
             J5 = Hospital

             Roads:
             0 -> 1 = 4
             0 -> 2 = 2
             1 -> 3 = 5
             2 -> 3 = 1
             3 -> 4 = 3
             4 -> 5 = 2
             2 -> 5 = 10
        */

        addRoad(0, 1, 4);
        addRoad(0, 2, 2);
        addRoad(1, 3, 5);
        addRoad(2, 3, 1);
        addRoad(3, 4, 3);
        addRoad(4, 5, 2);
        addRoad(2, 5, 10);

        int source = 0;
        int hospital = 5;

        // First calculation
        System.out.println("----- Initial Traffic -----");

        int[] distance = dijkstra(source);

        System.out.println(
                "Shortest distance to hospital: "
                        + distance[hospital]
                        + " minutes"
        );

        printPath(source, hospital);

        // Save path for visualization
        ArrayList<Integer> list = new ArrayList<>();

        int current = hospital;

        while (current != -1) {
            list.add(current);
            current = parent[current];
        }

        Collections.reverse(list);

        int[] path = new int[list.size()];

        for (int i = 0; i < list.size(); i++)
            path[i] = list.get(i);

        // Show initial route
        showGraph(
                path,
                source,
                hospital
        );

        // Dynamic traffic update
        System.out.println(
                "\n\n----- Traffic Update -----"
        );

        System.out.println(
                "Road 2 -> 3 is congested."
        );

        System.out.println(
                "Travel time changed from 1 to 8 minutes."
        );

        updateRoad(2, 3, 8);

        // Run Dijkstra again
        distance = dijkstra(source);

        System.out.println(
                "\n----- Updated Traffic -----"
        );

        System.out.println(
                "New shortest distance: "
                        + distance[hospital]
                        + " minutes"
        );

        printPath(source, hospital);

        // Create updated path
        list.clear();

        current = hospital;

        while (current != -1) {
            list.add(current);
            current = parent[current];
        }

        Collections.reverse(list);

        path = new int[list.size()];

        for (int i = 0; i < list.size(); i++)
            path[i] = list.get(i);

        // Show updated route
        showGraph(
                path,
                source,
                hospital
        );
    }
}
