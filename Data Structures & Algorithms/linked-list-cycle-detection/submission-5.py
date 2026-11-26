# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        fast = head.next
        slow = head
        while fast and fast.next:
            if fast == slow:
                return True

            fast = fast.next.next
            slow = slow.next
        
        return False

'''
TC: O(n)
If there is no cycle, fast reaches the end of the list in O(n/2) steps. If there is a cycle, fast closes the gap on slow by 1 node per iteration, guaranteeing they meet within at most one full pass of the list.

SC: O(1)
Only two pointer variables (fast and slow) are stored regardless of the input list size.
'''