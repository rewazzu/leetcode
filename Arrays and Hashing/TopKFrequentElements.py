class Solution:
    def topKFrequent(self, nums, k: int):
        frequency = {}
        for num in nums:
            frequency[num] = frequency.setdefault(num, 0) + 1

        frequency_list = list(frequency.items())
        frequency_list.sort(key=lambda x: x[1], reverse=True)
        print(frequency_list)
        result = [x[0] for x in frequency_list]
        result = result[:k]
        return result


def test_case(nums,result, k):
    solution = Solution()
    valid = solution.topKFrequent(nums,k) == result
    return valid


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    result = [1,2]
    k = 2
    valid = test_case(nums,result,k)

'''Commentary
First pass adding frequencies to dictionary is O(n)
Sorting dictionary items is O(nlogn)
Extracting elements is O(n)
Overall run time is O(nlogn)

The overall structure of the result came naturally. 
Had some difficulty remembering the syntax for the list sort method'''
