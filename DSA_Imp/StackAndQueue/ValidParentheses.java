// Given a string of opening and closing brackets([,{,(,),},]) which represents an expression. Check if the expression is valid.
// Valid expression is one where opening and closing brackets match up well.
// sample input 
// expression - {()}[]
// sample output
// true
// time complexity = 0(n)
// space complexity = 0(n)

package DSA_Imp.StackAndQueue;
import java.util.*;

public class ValidParentheses {
    public static void main(String[] args){
        String str = "[{()}()";
        System.out.println(isValid(str));
    }

    public static boolean isValid(String str){
        Stack<Character> st = new Stack<>();
        for(int i = 0; i< str.length(); i++){
            char ch = str.charAt(i);
            if(ch == '(' || ch == '{' || ch == '['){
                st.push(ch);
            }else{
                if(st.size() == 0){
                    return false;
                }
                if(ch == ')' && st.peek() == '('){
                    st.pop();
                }
                else if(ch == '}' && st.peek() == '{'){
                    st.pop();
                }
                else if(ch == ']' && st.peek() == '['){
                    st.pop();
                }
                else{
                    return false;
                }
            }
        }
        if(st.size() == 0){
            return true;
        }else{
            return false;
        }
    }
}