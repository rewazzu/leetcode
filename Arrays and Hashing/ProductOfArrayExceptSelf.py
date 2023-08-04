class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [[] for x in range(len(nums))]
        postfix = [[] for x in range(len(nums))]
        result = [[] for x in range(len(nums))]

        for index, num in enumerate(nums):
            if index == 0:
                value = 1
            else:
                value = prefix[index - 1] * nums[index - 1]
            prefix[index] = value

        for index in range(len(nums) - 1, -1, -1):
            if index == len(nums) - 1:
                value = 1
            else:
                value = postfix[index + 1] * nums[index + 1]
            postfix[index] = value

        for index in range(len(nums)):
            value = prefix[index] * postfix[index]
            result[index] = value

        return result


"""Commentary
We do three passes across the input so it becomes an O(n) solution
Memory can be reduced by saving directly into the result array instead of prefix,postfix arrays
"""