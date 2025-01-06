#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

int* solve(int* A, int n1, int* len1) {
    // Create a max-heap and a min-heap.
    priority_queue<int> maxHeap;  // Max heap for the smaller half of the elements
    priority_queue<int, vector<int>, greater<int>> minHeap;  // Min heap for the larger half of the elements
    
    vector<int> result;
    
    for (int i = 0; i < n1; i++) {
        int num = A[i];
        
        // Insert the number into the correct heap
        if (maxHeap.empty() || num <= maxHeap.top()) {
            maxHeap.push(num);
        } else {
            minHeap.push(num);
        }
        
        // Balance the heaps if necessary
        if (maxHeap.size() > minHeap.size() + 1) {
            minHeap.push(maxHeap.top());
            maxHeap.pop();
        } else if (minHeap.size() > maxHeap.size()) {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
        
        // The median is the top of the max-heap
        result.push_back(maxHeap.top());
    }
    
    // Allocate memory for the result array
    *len1 = result.size();
    int* resultArr = new int[*len1];
    for (int i = 0; i < *len1; i++) {
        resultArr[i] = result[i];
    }
    
    return resultArr;
}

int main() {
    int A[] = {1, 2, 5, 4, 3};
    int n1 = 5;
    int len1;
    int* result = solve(A, n1, &len1);
    
    for (int i = 0; i < len1; i++) {
        cout << result[i] << " ";
    }
    cout << endl;
    
    delete[] result;
    return 0;
}