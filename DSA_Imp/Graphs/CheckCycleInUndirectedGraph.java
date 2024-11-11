// dfs time complexity = O(v+e)
// dfs space complexity = O(v + ht of tree)
// bfs time complexity = O(v+e)
// bfs space complexity = O(v)

package DSA_Imp.Graphs;

import java.util.*;

class Pair{
    int vtx;
    int parent;

    public Pair(int vtx, int parent){
        this.vtx = vtx;
        this.parent = parent;
    }
}

public class CheckCycleInUndirectedGraph {
    public static void main(String[] args) {
        int n = 7; // Number of vertices

        @SuppressWarnings("unchecked")
        ArrayList<Integer>[] graph = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        // Add edges for an undirected graph
        addEdge(graph, 0, 1);
        addEdge(graph, 0, 2);
        addEdge(graph, 0, 3);
        addEdge(graph, 1, 2);
        addEdge(graph, 2, 3);
        addEdge(graph, 3, 4);
        addEdge(graph, 2, 4);
        addEdge(graph, 5, 6);

        // Cycle detection in undirected graph
        boolean[] visited = new boolean[graph.length];
        boolean hasCycle = false;

        for (int i = 0; i < visited.length; i++) {
            if (!visited[i]) {
                // For all the components
                if (isCyclic(graph, i, visited, -1)) {
                    hasCycle = true;
                    break;
                }
            }
        }
        System.out.println("Cycle detected: " + hasCycle);
    }

    // Helper method to add an undirected edge
    public static void addEdge(ArrayList<Integer>[] graph, int u, int v) {
        graph[u].add(v);
        graph[v].add(u);
    }

    // DFS method
    public static void dfs(ArrayList<Integer>[] graph, int src, boolean[] visited) {
        visited[src] = true;
        System.out.print(src + " ");
        for (int neighbor : graph[src]) {
            if (!visited[neighbor]) {
                dfs(graph, neighbor, visited);
            }
        }
    }

    // BFS method
    public static void bfs(ArrayList<Integer>[] graph, int src, boolean[] visited) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(src);
        visited[src] = true;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            System.out.print(node + " ");
            for (int neighbor : graph[node]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    queue.add(neighbor);
                }
            }
        }
    }

    // Cycle detection using DFS for an undirected graph
    public static boolean isCyclic(ArrayList<Integer>[] graph, int src, boolean[] visited, int parent) {
        visited[src] = true;
        for (int neighbor : graph[src]) {
            if (!visited[neighbor]) {
                if (isCyclic(graph, neighbor, visited, src)) {
                    return true;
                }
            } else if (neighbor != parent) {
                return true;
            }
        }
        return false;
    }

    public static boolean isCyclicBfs(ArrayList<Integer>[] graph, int src, boolean[] visited) {
        Queue<Pair> q = new ArrayDeque<>();
        q.add(new Pair(src, -1));
        visited[src] = true;

        while (q.size() > 0) {
            Pair rp = q.remove();
            for(int nbr : graph[rp.vtx]){
                if(nbr == rp.parent){
                    if(visited[nbr] == true){
                        // we are visiting an already visited vertex
                        return true;
                    }
                    visited[nbr] = true;
                    q.add(new Pair(nbr, rp.vtx));
                }
            }
        }
        return false;
    }
}