class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        left_arr = []
        curr_product = 1
        for i in range(len(nums)):
            left_arr.append(curr_product)
            curr_product *= nums[i]
        
        
        right_arr = []
        curr_product = 1
        for i in range(len(nums)-1, -1, -1):
            right_arr.append(curr_product)
            curr_product *= nums[i]
        right_arr.reverse()
        

        output = []
        for i in range(len(left_arr)):
            output.append(left_arr[i]*right_arr[i])
        
        return output
'''
Example 1:
nums = [1,2,4,6]

output = [48,24,12,8]

Example 2:
nums = [-1,0,1,2,3]

output = [0,-6,0,0,0]

Psuedo code (brute force)
--------------------------
output = []
loop through the nums array (i)
    sum = 1
    loop through the nums array (j)
        if i == j we ignore
        else we will multiply the current value at j with sum

    output[i] = sum

return output




[1,2,4,6]

left_pass
sum = 1
loop through nums
    ignoring the current number find the product of everything left of it and add it to left_arr

[1,1,2,8]


[1,2,4,6]
right_arr
sum = 1
loop through nums backwards
    ignoring the current number add the product of everything right of it and add it to right_arr


[48,24,6,1]


[1,1,2,8]
[48,24,6,1]

48, 24, 12, 8



nums = [-1,0,1,2,3]

[1,-1,0,0,0]

[0,6,6,3,1]

[0,-6,0,0,0]

'''