class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]

        slow = 0

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow


'''Commentary: 
This solution uses Floyd's algorithm. 
We treat the array as a linked list. There is a cycle in the linked list, we use floyd's to detect the cycle.
Runs in O(n) time.'''