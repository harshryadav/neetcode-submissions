class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = {}

        for val in nums:
            if val not in res:
                res[val] =  1         
            else: 
                res[val] = res[val] + 1

            if res[val] > 1:
                return True
        
        return False
        