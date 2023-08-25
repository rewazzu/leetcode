class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = False
        dummy_head = ListNode()
        l3 = dummy_head
        carry = 0

        while l1 and l2:
            val = l1.val + l2.val + carry
            carry = 0
            if val >= 10:
                val -= 10
                carry = 1
            l3.next = ListNode(val)
            l3 = l3.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            val = l1.val + carry
            carry = 0
            if val >= 10:
                val -= 10
                carry = 1
            l3.next = ListNode(val)
            l1 = l1.next
            l3 = l3.next

        while l2:
            val = l2.val + carry
            carry = 0
            if val >= 10:
                val -= 10
                carry = 1
            l3.next = ListNode(val)
            l2 = l2.next
            l3 = l3.next

        if carry:
            l3.next = ListNode(1)

        return dummy_head.next


'''Commentary:
This code runs in O(n+m) where n and m are lengths of the list.
This is because we iterate through both lists and do constant time operations each time.
The memory complexity is O(n+m) as we create a new list. 

This problem is straight forward, mostly need to keep track of the carry overs

'''