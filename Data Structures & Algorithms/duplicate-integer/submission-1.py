class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dupe = {}

        for num in nums:
            if num not in dupe:
                dupe[num] = 0
            dupe[num] += 1
            if dupe[num] > 1:
                return True

        return False


# Time Complexity - O(n) b/c we have to go through each number in the list nums
# Space Complexity - O(n) b/c we are looping through and storing the counts of each number in nums

