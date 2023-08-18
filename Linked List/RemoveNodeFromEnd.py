class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        previous = None
        current = head
        future = head.next
        terminal = head

        for i in range(n):
            terminal = terminal.next

        while terminal:
            previous = current
            current = current.next
            future = future.next
            terminal = terminal.next

        if previous:
            previous.next = future
        else:
            return head.next
        return head


"""Commentary: This is O(n) linear time complexity as we 
 are simply iterating through the list doing constant time operations
 The tricky part here is realizing we can use a pointer that is n ahead of current
  to indicate we are at the node to remove"""