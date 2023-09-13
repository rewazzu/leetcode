class Solution:
    def calc_hours(self, piles, speed):
        if speed <= 0:
            return float('inf')
        hours = 0
        for pile in piles:
            hours += -(-pile // speed)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        end = max(piles)
        best = None
        while start <= end:
            middle = start + (end - start) // 2
            hours = self.calc_hours(piles, middle)
            if hours > h:
                start = middle + 1
            elif hours <= h:
                best = middle
                end = middle - 1

        return best

"""
Commentary: We are essentially doing binary search across the range 0 to max(Piles). Each time we do binary search
we do n operations. So the time complexity is O(log(maxPiles)*n)

This problem is an interesting twist on binary search. We need to realize that our possible values are between 1 and 
max(Piles). Then given a speed we need to realize how to calculate hours. Then we realize that it is possible to do binary
search where hours is your target to find and speed is your index. The last twist is that we need to find the minimum
value so instead of stopping when we find the target, we store the best value so far and then continue until the
list is exhausted.


"""