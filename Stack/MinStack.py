class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minimum)==0 or val <= self.minimum[-1]:
            self.minimum.append(val)
        return None

    def pop(self) -> None:
        popped = self.stack.pop()
        if popped == self.minimum[-1]:
            self.minimum.pop()
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]



"""Commentary: All operations are in constant time O(1)
 
 This problem only took me a few minutes to solve.
 The trick to this question is realizing that you can store the minimum in a stack itself. If a new min is added,
 you just add to the minstack. If it is removed, then you remove from the minstack as well.
 
 """