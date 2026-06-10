class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}

        for num in nums:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1

        # res = []
        # for key1, val1 in freq.items():
        #     curr_max_value_key = key1

        #     for key2, val2 in freq.items():

        #         max(val1, val2)
        #         if val2 > val1:
        #             curr_max_value_key = key2
        #             freq[key2] = 0
            
        #     freq[key1] = 0

        #     if len(res) == k:
        #         return res
        #     res.append(curr_max_value_key)
                    
        res = []
        i = 0
        while i < k:
            max_key = max(freq, key=freq.get)
            res.append(max_key)
            freq[max_key] = 0
            i += 1

        
        return res
