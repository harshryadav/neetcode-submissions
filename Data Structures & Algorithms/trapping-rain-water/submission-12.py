class Solution:
    def trap(self, height: List[int]) -> int:
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
                leftMax = max(leftMax, height[left])
                water_count += leftMax - height[left]
            else:
                right -= 1
                rightMax = max(rightMax, height[right])
                water_count += rightMax - height[right]
        
        return water_count

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


'''

max_from_left = [] <- one loop to get this
max_from_right = [] <- another loop to get this

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
right = len(height)-1

leftMax = height[left]
rightMax = height[len(height)-1]

water_count = 0
while left < right
    if leftMax < rightMax:
        increment left
        leftMax = max(leftMax, height[left])
        water_count += leftMax - height[left]
    else:
        decrement right
        rightMax = max(rightMax, height[right])
        water_count += rightMax - height[right]


TC: O(n)
SC: O(1)

'''