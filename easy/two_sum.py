"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


def two_sum(numbers, target_element):
    seen = {}
    for i, num in enumerate(numbers):
        print(seen)
        second_element = target_element - num
        if second_element in seen:
            return [seen[second_element], i]
        seen[num] = i


# nums = [2, 7, 11, 15]
# target = 9

# nums = [3, 2, 4]
# target = 6

nums = [3, 3]
target = 6

result = two_sum(nums, target)
print(result)
