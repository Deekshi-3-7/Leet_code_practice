"""Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII,
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].
"""


def roman_to_int(roman_characters):
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    # total = 0
    # for i in range(len(roman_characters) - 1):
    #     if roman_values[roman_characters[i]] < roman_values[roman_characters[i + 1]]:
    #         total -= roman_values[roman_characters[i]]
    #     else:
    #         total += roman_values[roman_characters[i]]
    # return total + roman_values[roman_characters[-1]]

    # roman_characters = roman_characters.replace('IV', 'IIII')
    # roman_characters = roman_characters.replace('IX', 'VIIII')
    # roman_characters = roman_characters.replace('XL', 'XXXX')
    # roman_characters = roman_characters.replace('XC', 'LXXXX')
    # roman_characters = roman_characters.replace('CD', 'CCCC')
    # roman_characters = roman_characters.replace('CM', 'DCCCC')
    #
    # for char in roman_characters:
    #     total += roman_values[char]
    # return total

    total = 0
    prev_value = 0
    for char in reversed(roman_characters):

        curr_value = roman_values[char]
        if curr_value < prev_value:
            total -= curr_value
        else:
            total += curr_value
        prev_value = curr_value
    return total


result = roman_to_int('MCMXCIV')
print(result)
