class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        if nums[left] == target:
            return left
        
        while left <= right:
            mid = (left+right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] <= nums[right]: # check if right side is sorted
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else: # check if left side is sorted
                if nums[mid] >= target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

'''

nums=[1,3] target=3


nums = [3,4,5,6,1,2], target = 1

check if target <= right, if so we shift left pointer

else we shift thr right pointer

target = 1
[3,4,5,6,1,2]
 l   m     r

left = 3
right = 5
[3,4,5,6,1,2]
       l   r

target = 0
nums=[4,5,6,7,0,1,2]

left = 0
right = 6

0 < 6
    mid = (0 + 6) / 2 = 3

    is 7 == 0? no

    if 0 <= 2? yes
        left = 4

nums=[4,5,6,7,0,1,2]

4 < 6
    mid = (4 + 6) / 2 = 5

    is 1 == 0? no

    is 0 <= 2? yes


'''
        