class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        best = 0
        lowest = prices[0]
        diff = []

        while right < len(prices):
            current = prices[right] - prices[left]
            if current > best:
                best = current
            if prices[right] < lowest:
                lowest = prices[right]
                left = right
            right += 1
        return best

    """ Commentary
    We iterate up to 2n or O(n)
    The trick to this question is to realize that left only updates if we find a new lowest price.
    """