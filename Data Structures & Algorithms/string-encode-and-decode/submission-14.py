class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        # res = []
        # temp = ""
        # for i in range(len(s)):
        #     if s[i] == '#':
        #         res.append(temp)
        #         temp = ""
        #     else:
        #         temp += s[i]
        
        # res.append(temp)


        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            
            word_length = int(s[i:j])
            curr_word = s[j + 1 : j + 1 + word_length]
            res.append(curr_word)
            i = j + 1 + word_length

        return res