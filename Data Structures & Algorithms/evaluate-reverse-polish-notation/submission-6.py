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

        return stack[0]



'''


we iterate through the tokens

    when we come across an operator we will perform that operator on the last two elements of the stack, then we will append the result of that operation to the stack
    
    push only numbers into the stack

return the first element of the stack



Time Complexity: O(n)
Space COmplexity: O(n)

'''