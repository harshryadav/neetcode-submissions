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
        i = 1
        while i < len(s):
            if (s[i] == ')' or s[i] == '}' or s[i] == ']'):
                if st and st[-1] == valid_parenthesis.get(s[i]):
                    st.pop()
                    i += 1
                else:
                    return False
            else:
                st.append(s[i])
                i += 1

        # for i in range(1,len(s)):
        #     if (s[i] == ')' or s[i] == '}' or s[i] == ']'):
        #         if st and st[-1] == valid_parenthesis.get(s[i]):
        #             st.pop()
        #         else:
        #             return False
        #     else:
        #         st.append(s[i])

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

while the stack is not empty and less then length of s  
    
    if we see a closed bracket
        check in our stack if the last element we added is a corresponding closing bracket
        if it is then we pop the value off from the stack
        else we return false
    
    else add to the stack

return true


Time Complexity: O(n) because at most we go through the length of s

Space Complexity: O(n) our stack can at most go to the length of s




"(){}}{"

st = ['(']
i = 1


Iteration 1: is stack not empty? yes and is 1 < 6? yes

is ')' a closed parenthesis? yes
is it a valid parenthesis? yes

remove from stack
st = []
i = 2

Iteration 2: is stack not empty? no and is 2 < 6? yes



'''