class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left = 0
        right = len(height) - 1

        while left < right:
            value = min(height[left], height[right]) * (right - left)
            if value > best:
                best = value
            if height[left] >= height[right]:
                right -= 1
            elif height[left] < height[right]:
                left += 1

        return best


'''
Commentary: This is a O(n) solution since we just iterate through the array once.

The trick to this question is to recognize that we can just update the shorter of the two walls.
After understanding that aspect, the rest of the solution is straightforward.

'''