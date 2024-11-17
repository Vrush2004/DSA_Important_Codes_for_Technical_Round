// Given a 1D integer array A containing N integers, the array A is circular.
// A circular array is one where the next element of the last element is the first element.
// You need to find next immediate larger number for every element in the array A.
// NOTE:For any element within the circular array, the next immediate larger number could be found circularly past the end and before it.
// If there is no number greater, return -1.

#include <vector>
#include <stack>
#include <iostream>

using namespace std;

vector<int> Solution::solve(vector<int> &A) {
    int N = A.size();
    vector<int> result(N, -1);  // Initialize the result array with -1
    stack<int> s;
    
    // Iterate over the array twice to handle the circular nature
    for (int i = 0; i < 2 * N; ++i) {
        // Circular index using modulo
        int currentIndex = i % N;
        
        // Process elements in the stack while the current element is greater
        // than the element at the index stored in the stack
        while (!s.empty() && A[currentIndex] > A[s.top()]) {
            int index = s.top();
            s.pop();
            result[index] = A[currentIndex];  // Update the next greater element
        }
        
        // Push the current index to the stack only during the first pass
        if (i < N) {
            s.push(currentIndex);
        }
    }

    return result;
}