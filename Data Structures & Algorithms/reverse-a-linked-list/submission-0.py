# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        temp = head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev


'''

prev = null
curr = head
temp = head
while curr.next:
    temp = curr.next
    curr.next = prev
    prev = curr

return curr

0 --> 1 --> 2 --> 3


'''
        