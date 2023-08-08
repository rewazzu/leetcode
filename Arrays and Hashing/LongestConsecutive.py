class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        num_set = set(nums)
        best = 1
        for num in nums:
            current = 1
            left_num = num - 1
            next_num = num + 1
            if left_num not in num_set:
                while next_num in num_set:
                    next_num += 1
                    current += 1
            best = max(current, best)

        return best


"""Commentary: This is O(n) because we visit each number at most 2 times.

The trick to this problem is to realize that the start of sequences do not have left neighbors.
This allows us to only search for next values if the number is the start of a sequence, reducing the time complexity
from O(n^2) to O(n)"""