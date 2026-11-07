class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                pop_index = stack.pop()
                res[pop_index] = i - pop_index
    
            stack.append(i)
        
        return res







'''
temperatures = [30,38,30,36,35,40,28]
                      
res = [0, 0, 0, 0, 0, 0, 0]

stack = []


[30,38,30,36,35,40,28]
i = 0

stack = [0]


[30,38,30,36,35,40,28]
i = 1


stack = [1]



[30,38,30,36,35,40,28]
i = 2

stack = [1,2]



'''