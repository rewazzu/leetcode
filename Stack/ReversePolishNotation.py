class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        if len(tokens) == 1:
            return int(tokens[-1])
        for token in tokens:
            if token in ["+", "-", "*", "/"]:
                second = int(stack.pop())
                first = int(stack.pop())
                if token == "+":
                    result = first + second
                if token == "-":
                    result = first - second
                if token == "*":
                    result = first * second
                if token == "/":
                    result = int(first/second)
                stack.append(result)
            else:
                stack.append(token)

        return stack[-1]


"""Commentary:
This runs in O(n) because for each token we just do a max of two operations. 

The only tricky part of this one is rounding towards zero which can be done by int()
also the edge case when there is only one input requires its own way to deal with it"""