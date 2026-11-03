class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq_nums = set(nums)
        
        max_count = 0

        for num in nums:
            if num-1 not in uniq_nums:
                counter = 1
                while num+1 in uniq_nums:
                    counter += 1
                    num += 1
                
                max_count = max(max_count, counter)
        
        return max_count







'''
The start of a sequence means that there is no number that is less than -1 of it


unique_nums = set(nums)

max_count = -inf
loop through the nums array
    if the num - 1 is not in the unique_nums set
        counter = 1
        while num + 1 in unique_set
            counter += 1
        
        max_count = max(max_count, counter)
    

return max_count

    







'''