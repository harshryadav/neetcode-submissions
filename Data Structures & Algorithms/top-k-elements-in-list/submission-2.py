class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # get the frequencies of each unique element
        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
                    
        res = []
        i = 0
        # get the top k frequent elements
        while i < k:
            # returns the key of the highest element in the dictionary
            max_key = max(freq, key=freq.get)
            res.append(max_key)
            # set the highest element's value to 0
            freq[max_key] = 0
            i += 1

        return res
