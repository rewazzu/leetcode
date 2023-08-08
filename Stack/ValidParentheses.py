class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for element in s:
            if element in ["(","[","{"]:
                stack.append(element)
            elif len(stack) == 0:
                return False
            elif element == ")":
                if stack.pop() != "(":
                    return False
            elif element == "]":
                if stack.pop() != "[":
                    return False
            elif element == "}":
                if stack.pop() != "{":
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


"""Commentary: This is O(n) solutions since we pass through the array once and do constant operations per iteration

Have to remember the edge cases where you might try to pop an empty stack, or you might be left with some elements in
the stack when you finish. """