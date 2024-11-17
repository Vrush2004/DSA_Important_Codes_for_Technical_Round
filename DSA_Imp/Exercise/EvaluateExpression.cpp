// An arithmetic expression is given by a string array A of size N.   Evaluate the value of an arithmetic expression in Reverse Polish Notation.
// Valid operators are +, -, *, /.  Each string may be an integer or an operator.
// Note: Reverse Polish Notation is equivalent to Postfix Expression, where operators are written after their operands.

#include <vector>
#include <string>
#include <stack>
#include <cstdlib>

using namespace std;

int Solution::evalRPN(vector<string> &A) {
    stack<int> s;
    
    // Iterate through each token in the input expression
    for (const string &token : A) {
        // If token is an operator, perform the operation
        if (token == "+" || token == "-" || token == "*" || token == "/") {
            int b = s.top(); s.pop();  // Pop the second operand
            int a = s.top(); s.pop();  // Pop the first operand
            
            int result = 0;
            
            if (token == "+") {
                result = a + b;
            } else if (token == "-") {
                result = a - b;
            } else if (token == "*") {
                result = a * b;
            } else if (token == "/") {
                result = a / b;  // Perform integer division
            }
            
            s.push(result);  // Push the result back onto the stack
        } else {
            // Otherwise, it's a number, push it onto the stack
            s.push(stoi(token));  // Convert the string to an integer
        }
    }
    
    // The stack will have the final result
    return s.top();
}