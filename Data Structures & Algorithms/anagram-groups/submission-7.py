class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]

        res = []
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

        # alreadyAdded = set()
        # for i in range(len(strs)):
        #     temp = []
        #     for j in range(len(strs)):
        #         if i != j and isAnagram(strs[i], strs[j]):
        #             temp.append(strs[j])
        #             alreadyAdded.add(strs[j])
            
        #     if strs[i] not in alreadyAdded:
        #         temp.append(strs[i])
        #         alreadyAdded.add(strs[i])
        #         res.append(temp)
        # return res


        # for word we want to check if it is an anagram with other words in the list
        # if they are then we create a list and add those as a group
        # can we block those already grouped values?

        for i in range(len(strs)):
            temp = []
            temp.append(strs[i])
            for j in range(len(strs)):
                if i != j and isAnagram(strs[i], strs[j]):
                    temp.append(strs[j])
                    strs[j] = 'removed'

            if temp[0] == 'removed':
                continue
            else:
                res.append(temp)
        return res
        
# input --> ["", "", ""]
# output --> [["", "", ""]]
