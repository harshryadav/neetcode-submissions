class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {} # define a dictionary
        for i in range(len(nums)): # loop through the nums list
            temp = target - nums[i] # subtract target from current nums value
            if temp in nums_map.keys(): # does that subtracted value already exist in the hashmap?
                return [nums_map[temp], i] # if so, return the index of the subtracted value and current value

            nums_map[nums[i]] = i # map value to their index position

# Time complexity - O(n) b/c at worst case we loop through all values in the list of nums
# Space complexity - O(n) b/c we create a hashmap that at worst case can be of size n being list of nums

        # # Brute force solution
        # for i in range(len(nums)):
        #     j = i + 1
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []






