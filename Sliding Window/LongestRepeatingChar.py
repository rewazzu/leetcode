class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0

        best = 1
        seen = [0] * 26
        left = 0

        for right in range(len(s)):
            seen[ord(s[right]) - ord('A')] += 1
            length = right - left + 1
            while length - max(seen) > k:
                seen[ord(s[left]) - ord('A')] -= 1
                left += 1
                length = right - left + 1
            best = max(best, length)

        return best


"""Commentary: This solution is in order 26n or O(n). The 26 is because for each element we need to find the max count,
which takes 26 lookups

This problem the trick is to realize there is only 26 possible inputs which allows us to speed up the runtime using a
fixed size array. The rest is a simple sliding window problem.


"""