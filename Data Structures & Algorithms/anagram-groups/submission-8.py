class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        res = []

        # compute anagram given two strings
        def isAnagram(string1: str, string2: str) -> bool:
            freq = [0] * 26
            
            if len(string1) != len(string2):
                return False

            for i in range(len(string1)):
                freq[ord(string1[i]) - ord('a')] += 1
                freq[ord(string2[i]) - ord('a')] -= 1
            
            for i in range(len(freq)):
                if freq[i] != 0:
                    return False
            
            return True

        # loop through each word in the list
        for i in range(len(strs)):
            temp = []
            temp.append(strs[i])
            # loop through each word in list
            for j in range(len(strs)):
                # check if word is not itself and an anagram
                if i != j and isAnagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    strs[j] = 'removed' # overwrite the word so that we do not add it again

            # check if this word has already been added
            if temp[0] == 'removed':
                continue
            else:
                res.append(temp)
        return res

