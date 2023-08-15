class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (end-start)//2 + start
            start_val = nums[start]
            end_val = nums[end]
            middle_val = nums[middle]

            if middle_val == target:
                return middle
            elif middle_val >= start_val:
                if target <= middle_val and target >= start_val:
                    end = middle - 1
                else:
                    start = middle + 1
            else:
                if target >= middle_val and target <= end_val:
                    start = middle + 1
                else:
                    end = middle - 1
        return -1

"""
Commentary:
This is binary search with a twist. 
When doing binary search one half will be sorted, one side will contain the pivot 
We check if the target is in the range of the sorted, if it is we keep that side, if it is not we throw that side away
Since this is binary search it runs in O(n)
"""