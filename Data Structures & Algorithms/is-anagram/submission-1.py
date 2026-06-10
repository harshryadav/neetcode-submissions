class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26

        if len(s) != len(t):
            return False

        for c in s:
            index = ord(c) - ord('a')
            freq[index] += 1

        for c in t:
            index = ord(c) - ord('a')
            freq[index] -= 1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        
        return True


        # freq_s = {}
        # freq_t = {}

        # for c in s:
        #     if c not in freq_s:
        #         freq_s[c] = 0
        #     freq_s[c] += 1
        
        # for c in t:
        #     if c not in freq_t:
        #         freq_t[c] = 0
        #     freq_t[c] += 1

        # for key in freq_s:
        #     if key not in freq_t:
        #         return False
        #     if freq_s[key] != freq_t[key]:
        #         return False
        # return True




# s = racecars   t = carrace
# r --> 2
# a --> 2
# c --> 2
# e --> 1
# s --> 1

# r --> 0
# a --> 0
# c --> 0
# e --> 0

