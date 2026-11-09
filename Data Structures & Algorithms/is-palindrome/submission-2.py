class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1

        while left < right:
            if not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -= 1
            else:
                if s[left].lower() != s[right].lower():
                    return False
                left += 1
                right -= 1
        return True



'''
The idea behind this is simple. We loop through the string s, keeping track of a left and right pointer. We have to update the pointers when we see a matching non-alphanumeric character. If we see no match then we no that it can't be a palindrome. We loop throguh until right and left meet. 


left = 0
right = lenth of string s

while left < right
    if charcater at s[left] and s[right] is alphanumeric and c[left] == c[right]
        continue
    else they do not match

if we have gone through the loop successfully then it is a palindrome so we return true


Time Complexity: O(n) as we are looking throguh the length of string s n/2 times compraing left and right character in the string

Space Compleoxty: O(1), we do not create any addtional data structures




'''