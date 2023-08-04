class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        smaller = 0
        bigger = len(numbers) - 1

        while bigger > smaller:
            value = numbers[bigger] + numbers[smaller]
            if target < value:
                bigger -=1
            elif target > value:
                smaller +=1
            elif target == value:
                return [smaller + 1, bigger+1]


'''
Commentary: At most we do O(n) passes through the array.
At first I accidentally flipped the > and < signs. I need to be more careful about that.

'''