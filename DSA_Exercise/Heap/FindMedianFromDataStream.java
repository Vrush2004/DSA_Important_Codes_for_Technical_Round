// Time complexity = O(nlogn)
// Space complexity = O(n)

package DSA_Exercise.Heap;

import java.util.*;

class MedianFinder {
    PriorityQueue<Integer> pq1; // Max-heap for the lower half
    PriorityQueue<Integer> pq2; // Min-heap for the upper half

    public MedianFinder() {
        pq1 = new PriorityQueue<>(Collections.reverseOrder());
        pq2 = new PriorityQueue<>();
    }

    void add(int val) {
        if (pq1.isEmpty() && pq2.isEmpty()) {
            pq1.add(val);
        } else {
            if (val < pq1.peek()) {
                pq1.add(val);
            } else {
                pq2.add(val);
            }
        }

        int diff = Math.abs(pq1.size() - pq2.size());
        if (diff > 1) {
            if (pq1.size() > pq2.size()) {
                pq2.add(pq1.remove());
            } else {
                pq1.add(pq2.remove());
            }
        }
    }

    int findMedian() {
        // If the heaps are unbalanced, return the root of the larger heap
        if (pq1.size() >= pq2.size()) {
            return pq1.peek();
        } else {
            return pq2.peek();
        }
    }

    int remove() {
        // Remove from the heap that has more elements
        if (pq1.size() >= pq2.size()) {
            return pq1.remove();
        } else {
            return pq2.remove();
        }
    }
}

public class FindMedianFromDataStream {
    public static void main(String[] args) {
        MedianFinder medianFinder = new MedianFinder();
        
        // Add elements to the data stream
        medianFinder.add(10);
        System.out.println("Median after adding 10: " + medianFinder.findMedian());
        
        medianFinder.add(15);
        System.out.println("Median after adding 15: " + medianFinder.findMedian());

        medianFinder.add(5);
        System.out.println("Median after adding 5: " + medianFinder.findMedian());

        medianFinder.add(8);
        System.out.println("Median after adding 8: " + medianFinder.findMedian());

        // Remove the median element and check the new median
        System.out.println("Removing median: " + medianFinder.remove());
        System.out.println("New median after removal: " + medianFinder.findMedian());

        // Add more elements and check the median
        medianFinder.add(20);
        System.out.println("Median after adding 20: " + medianFinder.findMedian());

        medianFinder.add(30);
        System.out.println("Median after adding 30: " + medianFinder.findMedian());
    }
}
