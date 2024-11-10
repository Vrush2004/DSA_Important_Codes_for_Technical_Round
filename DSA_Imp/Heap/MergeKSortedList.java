// Given an list of K lists where each list is sorted. Merge all the lists in one and return the one sorted list.
// Sample input 
// list = {{10, 22, 28, 35, 40},
//         {6, 11, 15, 18},
//         {3, 9, 21, 36},
//         {1, 2, 3, 4, 5}}
// Sample Output
// {1,2,3,3,4,5,9,10,11,15,18,21,22,28,35,36,40}
// Time complexity = O(nlogk)
// space complexity = O(K)

package DSA_Imp.Heap;

import java.util.*;

class Pair implements Comparable<Pair> {
    int val;
    int li;  // list index
    int di;  // element index in the list

    Pair(int val, int li, int di) {
        this.val = val;
        this.li = li;
        this.di = di;
    }

    // Correct comparison logic
    public int compareTo(Pair o) {
        return this.val - o.val;  // Compare values to maintain min-heap property
    }
}

public class MergeKSortedList {
    public static void main(String[] args) {
        // Example usage
        ArrayList<ArrayList<Integer>> lists = new ArrayList<>();

        // Adding the sample input lists
        lists.add(new ArrayList<>(Arrays.asList(10, 22, 28, 35, 40)));
        lists.add(new ArrayList<>(Arrays.asList(6, 11, 15, 18)));
        lists.add(new ArrayList<>(Arrays.asList(3, 9, 21, 36)));
        lists.add(new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5)));

        ArrayList<Integer> mergedList = mergeSortedLists(lists);

        // Printing the merged list
        System.out.println(mergedList);
    }

    public static ArrayList<Integer> mergeSortedLists(ArrayList<ArrayList<Integer>> lists) {
        // Priority Queue to store the smallest element and its index information
        PriorityQueue<Pair> pq = new PriorityQueue<>();

        // Initialize the priority queue with the first element from each list
        for (int i = 0; i < lists.size(); i++) {
            if (!lists.get(i).isEmpty()) {
                pq.add(new Pair(lists.get(i).get(0), i, 0));
            }
        }

        ArrayList<Integer> ans = new ArrayList<>();

        // Process the heap until it is empty
        while (!pq.isEmpty()) {
            Pair rp = pq.remove();  // Get the smallest element
            ans.add(rp.val);

            // If there's more element in the list of this index, add the next element to the heap
            if (rp.di + 1 < lists.get(rp.li).size()) {
                pq.add(new Pair(lists.get(rp.li).get(rp.di + 1), rp.li, rp.di + 1));
            }
        }

        return ans;
    }
}
