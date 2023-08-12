class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        fleets = 0
        cars = []
        for i in range(len(position)):
            pair = [position[i], speed[i]]
            cars.append(pair)
        cars.sort(key=lambda x: x[0])

        for i in range(len(cars) - 1, -1, -1):
            finish_time = (target - cars[i][0]) / cars[i][1]

            if len(stack) > 0 and stack[-1] >= finish_time:
                continue
            else:
                fleets += 1
                stack.append(finish_time)
        return fleets

"""
Commentary: 
This runs in O(nlogn) because we need to sort the list. We then do constant time operations iterating
through the input, which is only linear.

The trick to this question is to realize that we only add a fleet if a car takes longer than the car in front of it.
We can figure this out by sorting the input by position, and then check the time left to the destination.
"""