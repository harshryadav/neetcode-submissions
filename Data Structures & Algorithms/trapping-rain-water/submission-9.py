class Solution:
    def trap(self, height: List[int]) -> int:
        # max_from_left = [0] * len(height)
        # max_from_right = [0] * len(height)

        # for i in range(1, len(height)):
        #     max_from_left[i] = max(max_from_left[i-1], height[i-1])

        # for i in range(len(height)-2, -1, -1):
        #     max_from_right[i] = max(max_from_right[i+1], height[i+1])

        # total_water = 0
        # for i in range(len(height)):
        #     water = min(max_from_left[i], max_from_right[i]) - height[i]
        #     if water > 0:
        #         total_water += water
        
        # return total_water

        if not height:
            return 0
        
        left = 0
        right = len(height)-1
        leftMax = height[left]
        rightMax = height[right]
        water_count = 0
        while left < right:
            if leftMax < rightMax:
                left += 1
                water_count += max(leftMax, height[left]) - height[left]
                leftMax = max(leftMax, height[left])
            else:
                right -= 1
                water_count += max(rightMax, height[right]) - height[right]
                rightMax = max(rightMax, height[right])
        
        return water_count



'''

max_from_left = [0,0,2,2,3,3,3,3,3,3] <- one loop to get this
max_from_right = [3,3,3,3,3,3,3,2,1,0] <- another loop to get this


total_water = 0
loop through the height list
    min(max_from_left[i], max_from_right[i]) - height[i]

TC: O(n) + O(n) + O(n) = O(3n) ~= O(n)
SC: O(n) + O(n) = O(2n) ~= O(n)




height=[4,2,0,3,2,5]

left = [0,4,4,4,4,4]
right = [5,5,5,5,5,0]

0 - 4 = -4

4 - 2 = 2 <--- add to total

4 - 0 = 4 <--- add to total

4 - 3 = 1 <-- add

4 - 2 = 2 <-- add

0 - 5 = -5




if height is 0 then we return 0

left = 0
right = length of height

leftMax = 0
rightMax = 0

water_count = 0
while left < right
    if leftMax < rightMax:
        water_count += max(leftMax, height[left]) - height[left]
        leftMax = max(leftMax, height[left])
        increment left
    else:
        water_count += max(leftMax, height[right]) - height[right]
        rightMax = max(rightMax, height[right])
        decrement right        



height=[4,2,3]


left = 0
right = 2
leftMax = 0
rightMax = 0





'''