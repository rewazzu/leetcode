class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tail = head
        previous_list = []

        while tail.next:
            previous_list.append(tail)
            tail = tail.next

        while len(previous_list) and tail != head:
            head_next = head.next
            head.next = tail
            head = head_next
            if tail == head:
                break
            tail.next = head
            tail = previous_list.pop()

        head.next = None

'''Commentary:
This solution runs in O(n) time and uses O(n) of space
The tricky part of this solution is backing up the end pointer as it is a singly list list.
'''