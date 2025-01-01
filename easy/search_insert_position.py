"""

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not,
return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104

"""


def search_insert(nums, target):
    # if target in nums:
    #     return nums.index(target)
    # else:
    #     for i in range(len(nums)):
    #         if target < nums[0]:
    #             return 0
    #         elif target > nums[-1]:
    #             return len(nums)
    #         elif nums[i] < target < nums[i + 1]:
    #             return i + 1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left


nums = [1, 3, 5, 6]
target = 7

print(search_insert(nums, target))
