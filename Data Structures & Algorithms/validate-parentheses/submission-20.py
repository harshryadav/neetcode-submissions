class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False

        valid_parenthesis = {
            ')':'(',
            '}':'{',
            ']':'['
        }

        st = []
        st.append(s[0])

        for i in range(1,len(s)):
            if (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                if st and st[-1] == valid_parenthesis.get(s[i]):
                    st.pop()
                else:
                    return False
            else:
                st.append(s[i])

        return len(st) == 0
'''
hash map that maps open bracket to a close bracket

{
    ")" : "("
    "}" : "{"
    "]" : "["
}

Psuedocode
--------------------------------------

create a hashmap of valid parenthesis

create a stack
push the first element of s into the stack

loop through string s
    if we see a closed bracket
        
        if stack not empty and our last element we added is a corresponding closing bracket
            we pop the value off from the stack
        
        else 
            we return false
    
    else add to the stack

return lenth of stack == 0 


Time Complexity: O(n) because at most we go through the length of s

Space Complexity: O(n) our stack can at most go to the length of s

'''