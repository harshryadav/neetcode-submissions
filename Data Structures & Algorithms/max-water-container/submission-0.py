class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights)-1
        max_area = 0

        while left != right:
            height = min(heights[left], heights[right])
            width = right - left
            area = width * height

            if area > max_area:
                max_area = area
            
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_area

'''
height = [1,7,2,5,4,7,3,6]



left = 0
right = len(heights) - 1
max_area = 0
while left != right
    height = min(height(left),height(right))
    width = right - left

    area = width * height

    if area > max_area
        update max_area

    if height[left] <  height[right]
        increment left
    else
        decement right

return max_area


height = [1,7,2,5,4,7,3,6]

left = 0
right = 7
max_area = 0

while 0 != 7
    height = min(1,6) = 1
    width = 7 - 0 = 7

    area = 7 * 1 = 7

    if area > max_area
        max_area = 7
    
    1 < 6? yes
        then we incrmenet left pointer, left = 1


while 1 != 7
    height = 6
    width = 6

    area = 36

    is 36 > 7? yes
        max_area = 36
    
    is 7 < 6? no

    is 7 > 6? yes
        right = 6



height = [2,2,2]


left = 0
right 2

max_area = 0

0 != 2

    height = 2
    width = 2
    area = 4

    max_area = 4




'''