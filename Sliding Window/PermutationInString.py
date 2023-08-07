class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        target = {}
        for element in s1:
            target[element] = target.get(element, 0) + 1

        potential = {}
        for element in s2[0:len(s1)]:
            potential[element] = potential.get(element, 0) + 1
        print(potential, target)
        if potential == target:
            return True

        for index in range(1, len(s2) - len(s1) + 1):
            potential[s2[index - 1]] -= 1
            if potential[s2[index - 1]] == 0:
                potential.pop(s2[index - 1])
            potential[s2[index + len(s1) - 1]] = potential.get(s2[index + len(s1) - 1], 0) + 1
            if potential == target:
                return True

        return False

'''Commentary:
This solution runs in 26n time or O(n) time. This is because we create a potential window for each index in s2.
For each window we have to check if the dictionaries are equal which takes up to 26 checks.

The trick to this question is to realize that we can pop and push elements from the "potential" dictionary as we slide
the window across the input. This reduces the complexity from O(nm) to O(n)

'''