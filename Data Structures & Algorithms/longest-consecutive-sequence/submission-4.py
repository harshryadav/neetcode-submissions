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


create a set of nums

max_count = 0
loop through the nums array
    if the num - 1 is not in the unique_nums set
        set temporary counter to 1
        while num + 1 in unique_nums
            increment counter by 1
            increment num value by 1
        
        get max(max_count, counter)
    

return max_count





Time Complexity = O(N) because we loop through the array at most 2N times 

Space Complexity = O(N) because we use a has set to store elements from nums


'''