class Solution:

    def encode(self, strs: List[str]) -> str:
        '''
        The idea here is that we encode the word with
        it's word length and some delimiter in the
        front of the word so that we can process it
        when we have to decode. 
        '''
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res


    def decode(self, s: str) -> List[str]:
        '''
        The idea is we want to think of the word as:
        <word_length><delimiter><word>
        4#hello5#world

        We loop thorugh reading the length of the word
        after the delimiter and then adding that to the result.
        Afterwards, we increment the pointer i to the next word
        length and then repeat the process until we read all words. 
        '''
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