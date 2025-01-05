"""

67. Add Binary

Given two binary strings a and b, return their sum as a binary string.


Example 1:
Input: a = "11", b = "1"
Output: "100"

Example 2:
Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""


def add_binary(a, b):
    a = a[::-1]
    b = b[::-1]

    result = []
    carry = 0

    for i in range(max(len(a), len(b))):
        bit_a = int(a[i]) if i < len(a) else 0
        bit_b = int(b[i]) if i < len(b) else 0

        total = bit_a + bit_b + carry
        result.append(str(total % 2))
        carry = total // 2

    if carry:
        result.append(str(carry))

    return ''.join(result[::-1])


a = "11"
b = "1"

bin_result = add_binary(a, b)
print(bin_result)
