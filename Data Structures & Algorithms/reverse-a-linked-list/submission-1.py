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
while curr:
    store curr's next value in temp
    point curr to prev
    set prev to curr
    set curr to temp

return prev


TC: O(N)
SC: O(1)


'''
        