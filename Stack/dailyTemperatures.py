class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while len(stack) > 0 and stack[-1][0] < temperatures[i]:
                _, old_index = stack.pop()
                output[old_index] = i - old_index
            stack.append([temperatures[i], i])

        return output



'''Commentary: This runs in O(n) time as we pass through the input once and only do constant-time operations
The trick to this question is to realize we can use a stack and store the indicies of past days.'''