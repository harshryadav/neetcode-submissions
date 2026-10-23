class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        res = {}

        for i in range(len(s)):
            if s[i] not in res:
                res[s[i]] = 1
            else:
                res[s[i]] += 1

        for i in range(len(t)):    
            if t[i] not in res:
                res[t[i]] = 1
            else:
                res[t[i]] -= 1

        for key, value in res.items():
            if value != 0:
                return False 
        
        return True