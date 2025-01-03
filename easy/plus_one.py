"""

Plus one

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the
integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer
does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.



Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].

Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].

Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].


Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.

"""


def plus_one(digits):
    # sum_string = ""
    # sum_list = []
    # for digit in digits:
    #     sum_string += str(digit)
    # sum = int(sum_string) + 1
    # for char in str(sum):
    #     sum_list.append(int(char))
    # return sum_list

    # num = int(''.join(map(str, digits))) + 1
    # return list(map(int, str(num)))

    """for digits between 0 and 10"""
    if any(d > 9 for d in digits):
        raise ValueError("Input array must only contain single-digit integers.")

    n = len(digits)
    carry = 1
    for i in range(n - 1, -1, -1):
        digits[i] += carry
        if digits[i] < 10:
            return digits
        digits[i] = 0
    return [1] + digits


# digits = [1, 2, 3]
# digits = [4, 3, 2, 1]
digits = [1, 9]

result = plus_one(digits)
print(result)
