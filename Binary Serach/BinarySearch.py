class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1
        found = None

        while end >= start:
            current = (end - start) // 2 + start
            found = nums[current]
            if found > target:
                end = current - 1
            elif found < target:
                start = current + 1
            elif found == target:
                return current

        return -1



"""
Commentary: Runs in O(logn) as the input gets halfed each time.
Classic binary search. 
"""