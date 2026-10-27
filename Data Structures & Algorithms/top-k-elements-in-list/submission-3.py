class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for i in nums:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1
            
        top_k = sorted(freq, key=freq.get, reverse=True)[:k]

        return top_k

# return k most frequent elements
# output can be in any order


'''
nums = [1,2,2,3,3,3], k = 2

1 --> 1
2 --> 2
3 --> 3

[2,3]



initialize a hashmap

loop through the nums array and get frequencies of each distinct element

loop through the hashmap
    add 



nums = [1,2,2,3,3,3], k = 2

{2:2, 3:3, 1:1}




create a prioriy queue

loop through nums array adding each elements frequency and elenet as a tuple

return the top k frequecies



'''


