class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        left = 0
        right = 0
        seen = set()
        best = 1
        seen.add(s[0])

        while right < len(s) - 1:
            if s[right + 1] not in seen:
                right += 1
                seen.add(s[right])
            else:
                if right == left:
                    seen.remove(s[left])
                    left += 1
                    right += 1
                    seen.add(s[right])
                elif right > left:
                    seen.remove(s[left])
                    left += 1
            current = right - left + 1
            best = max(best, current)

        return best



""" Commentary: This occurs in O(n) time since we are making a single pass through the input
Challenges: 
I got the syntax wrong initially for the set functions
With the edge case where right==left I initially added to the set before removing. If you add to the set first, the adding
doesnt happen if the element is already in the set. Which is a problem when that same element gets removed in the next line.

"""