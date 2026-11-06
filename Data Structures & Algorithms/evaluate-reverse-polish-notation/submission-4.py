class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in ('*', '-', '/', '+'):
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    stack.append(operand1 + operand2)
                if token == "-":
                    stack.append(operand1 - operand2)
                if token == "*":
                    stack.append(operand1 * operand2)
                if token == "/":
                    stack.append(int(operand1 / operand2))
            else:
                stack.append(int(token))

        return stack[-1]



'''

we know that thre can only be 4 operators 

and our operands can only be between -200 and 200




stack = 
[2]
[1]

use a "+" next

so we pop and put that element in a list

stack = [1]
operand = [2]

we keep popping until stack is empty

stack []
operand = [2, 1]


we perform whatever operator we get with the last element and the first

1 + 2 = 3


then we push into a stack


stack = [3, 3]
operand = []

"*"

stack = []
operand = [3, 3]


stack = [9]
operand = []


stack = [9, 4]
operand = [4, 9]

stack = [5]


stack = []
result = 0

loop through the tokens list:
    if number push into stack

    else we stop and compute 
        pop the last two elements
        operand2 = pop() 
        operand1 = pop()

        result = operand1 operator operand2

        push result into stack


return result



we iterate through the tokens
    push only numbers into the stack

    when we come across an operator we will perform that operator on the last two elements of the stack

    then we will append the result of that operation to the stack


return the first element of the stack


'''