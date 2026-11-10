class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            val = numbers[left] + numbers[right]

            if val == target:
                return [left+1, right+1]
            elif val < target:
                left += 1
            else:
                right -= 1


'''
The idea is we loop through the array keep track of a left and right pointer. We comoute the sum of the left and right values and check
    if that sum is the same as the target, then we return left and right's indices
    if the sum is greater than the targert, then we increment left pointer
    else, increment the right pointer

The idea is that doing it this way, the pointers look to be self "correcting" themselves towards the correct values that sum up to the target. This works because the array is sorted so we know that increasing and decreasing our pointers shifts the sum up or down closer to the target.

Time Complexity: O(n)
Space Complexity: O(1)
'''
        