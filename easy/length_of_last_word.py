"""

Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.

Constraints:

1 <= s.length <= 104
s consists of only English letters and spaces ' '.
There will be at least one word in s.

"""


def length_of_last_word(sentence):
    # words = sentence.split()
    # return len(words[-1])

    # s = sentence.rstrip()
    # count = 0
    # for char in reversed(str):
    #     if char == ' ':
    #         break
    #     count += 1
    # return count

    count = 0
    is_word = False
    for char in reversed(sentence):
        if char != ' ':
            count += 1
            is_word = True
        elif is_word:
            break
    return count


# s = " Hello World "
s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
result = length_of_last_word(s)
print(result)
