class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            product = 1
            j = 0
            while j < len(nums):
                if i != j:
                    product *= nums[j]
                j += 1      
            res.append(product)
        
        return res
        
# The above solution O(n^2) so not the best. Need to optimize it to O(n)