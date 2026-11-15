class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

'''

we check the middle value and it's num's left and right value to see which direction to check



left = 0
right = len(nums) - 1

while left < right
    mid = (left + right) / 2

    if nums[mid-1] > nums[right]
        left = mid + 1
    else
        right = mid

return nums[left]


TC: O(logn)
SC: O(1)

'''
        