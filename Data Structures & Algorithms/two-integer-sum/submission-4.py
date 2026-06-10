class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        nums_map = {}

        for i in range(len(nums)):
            temp = target - nums[i]

            if temp in nums_map.keys():
                return [nums_map[temp], i]

            nums_map[nums[i]] = i


        # nums_map {
        #     3: 1
        #     4: 2
        #     5: 3
        #     6: 4
        # }


        # for i in range(len(nums)):
        #     j = i + 1
        #     for j in range(len(nums)):
        #         if i != j and nums[i] + nums[j] == target:
        #             return [i, j]
        
        # return []




