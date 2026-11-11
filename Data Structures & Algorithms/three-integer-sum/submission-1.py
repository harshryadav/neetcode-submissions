class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums = sorted(nums)
        for i in range(len(nums)):
            # print(nums)
            left = i + 1
            right = len(nums) - 1
            while left < right:
                pair = nums[left] + nums[right]
                # print(pair)
                if pair == -(nums[i]):
                    triplet = sorted([nums[i], nums[left], nums[right]])
                    if triplet not in res:
                        res.append(triplet)
                if pair > -(nums[i]):
                    right -= 1
                else:
                    left += 1

        return res        


        # Brute force
        # res = []
        # for i in range(len(nums)):
        #    for j in range(i + 1, len(nums)):
        #       for k in range(j + 1, len(nums)):
        #         if nums[j] + nums[k] == -(nums[i]):
        #             triplet = sorted([nums[i], nums[j], nums[k]])
        #             if triplet not in res:
        #                 res.append(triplet)
        


'''

O(n) + O(n) + O(n) = O(n^3)

brute force would be --

we repaeat search two other elements for the ith element to see if all 3 add up to 0


nums = [-1,0,1,2,-1,-4]

nums = [-4,-1,-1,0,1,2]



sort(nums) --> nlogn

res = []
loop through sorted nums array
    left = i + 1
    right = length of nums

    while left <= right
        is nums[left] + nums[right] == -(nums[i])

        if yes: 
            sort the triple
            if not triplet in res
                append triplet to res

        if nums[left] + nums[right] > -(nums[i])
            shift right pointer left
        else
            shift left pointer right
    



nums = [-4,-1,-1,0,1,2]



'''