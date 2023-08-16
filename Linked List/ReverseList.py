# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head
        while current is not None:
            future = current.next
            current.next = previous
            previous = current
            current = future
        return previous


'''Commentary: Runs in O(n), as we touch each element once and only do constant time operations

Fundamental Linked List Problem, just need to store the future node so we can access it after we change the current
pointer.
'''