# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1

        if list1.val <= list2.val:
            current = list1
            next1 = list1.next
            next2 = list2
        else:
            current = list2
            next1 = list1
            next2 = list2.next
        head = current
        while next1 or next2:
            if next1 is None:
                current.next = next2
                next2 = None
            elif next2 is None:
                current.next = next1
                next1 = None
            elif next1.val <= next2.val:
                current.next = next1
                current = next1
                next1 = next1.next
            else:
                current.next = next2
                current = next2
                next2 = next2.next
        return head


'''Commentary: 
This is a O(n + m) problem where n and m are the lengths of the lists. We iterate through each list and only do 
  constant time operations in each iteration so it is linear.'''

