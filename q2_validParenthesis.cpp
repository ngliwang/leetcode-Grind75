#include <stack>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    bool isValid(string s) {
        stack<char> st;  //taking stack for keep tracking the order of the brackets..

        // auto = string::iterator
        for(auto i:s)  //iterate over each and every elements
        {

            // simultaneous push and check
            
            // if opening bracket, straightaway push
            if(i=='(' or i=='{' or i=='[') st.push(i);  //if current element of the string will be opening bracket then we will just simply push it into the stack
            
            
            // for closing brackets, check if those in stack matches those in string
            // first CLOSING should match the first OPENING
            else 
            {
                if(st.empty() or (st.top()=='(' and i!=')') or (st.top()=='{' and i!='}') or (st.top()=='[' and i!=']')) return false;
                st.pop();  //if control reaches to that line, it means we have got the right pair of brackets, so just pop it.
            }
        }
        return st.empty();  //at last, it may possible that we left something into the stack unpair so return checking stack is empty or not..
    }
};

int main()
{
    // q2 valid parenthesis
    Solution s2;
    string s = "([)]";
    bool result = s2.isValid(s);
    cout << "result"<< result << endl;
    return 0;
}