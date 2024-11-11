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
}