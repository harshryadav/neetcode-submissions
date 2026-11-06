class MinStack:

    def __init__(self):
        self.min_stack = []
        self.min_seen = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)

        if len(self.min_seen) == 0:
            self.min_seen.append(val)

        elif self.min_seen[-1] > val:
            self.min_seen.append(val)
        
        else:
            self.min_seen.append(self.min_seen[-1])


    def pop(self) -> None:
        self.min_stack.pop()
        self.min_seen.pop()

    def top(self) -> int:
        return self.min_stack[-1]
        
    def getMin(self) -> int:
        return self.min_seen[-1]




        


'''
init - create a list

    min_stack = []
    min_seen = []

push - append the interger val to min_stack

    min_stack.append()

pop - remove top element of min_stack

    min_stack.pop() 

    any time we pop an elment from min_stack, we have to also pop from min_seen stack



top - the last element is at the end of the the list (or in other words the top of the stack)

    return min_stack[-1]

getMin - we need to keep track of the min after each push somehow so that after we pop, we will update the next min

we do that with a separate list keeping track of the current min we have seen and adding to the list after each push operation

    
min_stack = []

min = +inf


push 8
push 3
push 9
push 7



[7]
[9]
[3]
[8]

min_stack = [8, 3, 9, 7]


[3]
[3]
[3]
[8]

min = [8, 3, 3, 3]

getMin = 3

pop - 7 is gone

min_stack =
[9]
[3]
[8]

min = 
[3]
[3]
[8]

getMin = 3

pop - removes 9

min_stack =
[3]
[8]

min = 
[3]
[8]


getMin = 3

pop - removes 3

min_stack=
[8]

min=
[8]


any time we pop ana elment from min stack, we have to also pop from min



Time Complexity: O(1) because each operation (push, pop, top, getMin) is at most constant time 

Space Complexity: O(n) we use two stacks O(n) + O(n) = O(2n) which we can simplify by ignoring leading coefficients we get O(n)

'''