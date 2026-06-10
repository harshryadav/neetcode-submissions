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
