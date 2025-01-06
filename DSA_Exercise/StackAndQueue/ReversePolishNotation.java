// Evaluate the value of arithmetic expression given in reverse polish notation.
// Sample input 
// expression = ["2", "3", "*", "4", "+"]
// Sample output = 10
// time complexity = 0(n)
// space complexity = 0(d) 

package DSA_Exercise.StackAndQueue;
import java.util.*;

public class ReversePolishNotation {
    public static void main(String[] args){
        String[] exp = {"2" ,"-11", "18", "3", "/", "+", "*", "20", "+"};
        System.out.println(calculateRPN(exp));
    }

    public static int calculateRPN(String[] exp){
        Stack<Integer> st = new Stack<>();
        for(int i =0; i<exp.length; i++){
            String str = exp[i];
            if(str.equals("+") || str.equals("-") || str.equals("*") || str.equals("/")){
                int pop1 = st.pop();
                int pop2 = st.pop();
                st.push(solve(pop2, pop1, str));
            }
            else{
                st.push(Integer.parseInt(str));
            }
        }
        return st.pop();
    }

    public static int solve(int pop2, int pop1, String oprtr){
        if(oprtr.equals("+")){
            return pop2 + pop1;
        }
        else if(oprtr.equals("-")){
            return pop2 - pop1;
        }
        else if(oprtr.equals("*")){
            return pop2 * pop1;
        }
        else {
            return pop2 / pop1;
        }
    }
}