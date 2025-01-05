"""

69. Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer
should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.


Constraints:

0 <= x <= 231 - 1

"""


def my_sqrt(x):
    if x < 2:
        return x

    left, right = 0, x
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result


# Test cases
print(my_sqrt(4))  # Output: 2
print(my_sqrt(8))  # Output: 2
print(my_sqrt(10))  # Output: 3
print(my_sqrt(0))  # Output: 0
print(my_sqrt(1))  # Output: 1

