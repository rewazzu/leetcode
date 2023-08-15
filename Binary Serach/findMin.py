class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        best = float('inf')

        while nums[start] > nums[end]:
            middle = start + (end - start) // 2
            middle_val = nums[middle]
            best = min(best, middle_val)
            if nums[start] <= middle_val:
                start = middle + 1
            else:
                end = middle - 1

        return min(best, nums[start])



"""Commentary: This is binary search with a twist.
The rotated list is essentially two different sorted lists. The minimum value will appear at the start of a sorted
portion.
We store a best found value, and then throw away either the left or right side. We compare the middle value to the
start value to determine which side to throw away.
Since this is binary search it is O(log(n))
"""