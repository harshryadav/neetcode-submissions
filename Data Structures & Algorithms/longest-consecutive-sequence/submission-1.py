class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        uniq_nums = set(nums)
        
        max_count = float('-inf')

        for num in nums:
            if num-1 not in uniq_nums:
                counter = 1
                while num+1 in uniq_nums:
                    counter += 1
                    num += 1
                
                max_count = max(max_count, counter)
        
        return max_count







'''
set(nums) = 0,3,2,5,4,6,1


min_num = inf

loop through nums and add each element to the set
    0,3,2,5,4,6,1

loop through nums
    check if that element+1 is in the set
        if so, we add to a hash set mapping that num to the number 1 greater in it
        else, add an empty set

loop through that hash set starting from the smallest number
    check if that number has a set size greater than 0
        if so then we increment a counter and go to the number in that set, we continue this keep track of the longest counter


return the logest count we have seen





0 -> 1
3 -> 4
2 -> 3
5 -> 6
4 -> 5
6 -> inf
1 -> 2



[3,5,6,7,8,9]

3 -> []
5 -> [6]
6 -> [7]
8 -> [9]



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