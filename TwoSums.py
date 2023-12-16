'''
1. Two Sum
Easy
Topics
Companies
Hint
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]

Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
 indices = {0: 2, 1: 7}
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Dictionary to store the indices of elements
        indices = {}

        # Find the largest number in nums that is less than or equal to the target
        for i in range(len(nums)):
            num = nums[i]

            # If the current number is greater than the target, break the loop
            if num > target:
                break
            # Calculate the complement needed to reach the target
            complement = target - num

            # Check if the complement is in the dictionary
            if complement in indices:
                # If found, return the indices of the two numbers
                return [indices[complement], i]
            else:
                # Otherwise, add the current number and its index to the dictionary
                indices[num] = i

        # If no solution is found, return an empty list or handle it as needed
        return []


nums = [2, 7, 11, 15]
target = 9
solution = Solution()
result = solution.twoSum(nums, target)
print(result)

nums = [3, 2, 4]
target = 6
result = solution.twoSum(nums, target)
print(result)

nums = [3, 3]
target = 6
result = solution.twoSum(nums, target)
print(result)
