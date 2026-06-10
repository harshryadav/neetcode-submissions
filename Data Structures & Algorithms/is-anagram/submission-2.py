class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = [0] * 26

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            index = ord(s[i]) - ord('a')
            freq[index] += 1

            index = ord(t[i]) - ord('a')
            freq[index] -= 1


        # for c in s:
        #     index = ord(c) - ord('a')
        #     freq[index] += 1

        # for c in t:
        #     index = ord(c) - ord('a')
        #     freq[index] -= 1

        for i in range(len(freq)):
            if freq[i] != 0:
                return False
        
        return True

