class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        previous_i = None
        for i in range(len(nums) - 2):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            if previous_i == nums[i]:
                continue
            previous_i = nums[i]
            while left < right:
                current = nums[left] + nums[right]
                if right >= len(nums):
                    break
                if left <= i:
                    break
                if current > target:
                    right -= 1
                elif current < target:
                    left += 1
                elif current == target:
                    results.append([nums[i], nums[left], nums[right]])
                    previous_right = nums[right]
                    while nums[right] == previous_right and left < right:
                        right -= 1

        return results

'''Commentary: First we sort which takes nlogn then for each i we perform up to n actions, which is n^2
 Overall complexity is n^2
 
 The trick to this problem is to realize it boils down two sorted 2sum. Once you realize that you just have to deal
 with the duplicate problem. '''