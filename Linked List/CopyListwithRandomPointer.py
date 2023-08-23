class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        original_head = head
        original = head
        copy_head = Node(original.val)
        copy = copy_head

        while original:
            original.side = copy
            copy.side = original
            if original.next:
                copy.next = Node(original.next.val)
            else:
                copy.next = None
            original = original.next
            copy = copy.next

        copy = copy_head
        while copy:
            if copy.side.random:
                copy.random = copy.side.random.side
            else:
                copy.side = None
            copy = copy.next

        return copy_head



'''Commentary: 
This algorithm runs with two passes, each pass only doing constant time operations.
Therefore the time complexity is O(n)

The trick here is figuring out how to access future nodes when assigning "random" we do this by separating
the task into two passes. For the first pass we create all the nodes and create a "side" property that allows
us to traverse between the original and the copy. Then on the second pass we fill in random by using the side 
property.'''