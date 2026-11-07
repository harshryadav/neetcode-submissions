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
                      

[38] <- not added
[30]

temp = 1


append(temp)

[40] <- not added
[35]
[36]
[30]
[38]

temp = 4

append(temp)

[36] <- not added
[30]

temp = 1

append(temp)

[40] <- not added
[35]
[36]

temp = 2

append(temp)

[40] <- not added
[35]


temp = 1

append(temp)

[28]
[40]

edge case where if we are at the end of the array then we reset temp

append(temp)


[28]

edge case where if we are at the end of the array then we reset temp

append(temp)






[30,38,30,36,35,40,28]


temp = 0

checking = 0

result = []



[30,38,30,36,35,40,28]
 i
[30]

temp = 1

checking = 30

result = []




[30,38,30,36,35,40,28]
    i

temp = 1 
if checking < ith value
    pop
    result = [1]
    temp = 0
    push ith value to stack
    checking = 38



[30,38,30,36,35,40,28]
       i

temp = 0
checking = 38


[30]
[38]



[30,38,30,36,35,40,28]
          i

temp = 1
checking = 38

[36]
[30]
[38]



[30,38,30,36,35,40,28]
             i

temp = 2
checking 38

[35]
[36]
[30]
[38]


[30,38,30,36,35,40,28]
                i

checking = 38
temp = 3
if checking < ith value:
    keep popping until the value of temp

    result [1 4]

    

'''