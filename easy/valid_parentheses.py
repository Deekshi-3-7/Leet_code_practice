"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


def is_valid(s: str) -> bool:
    brackets_mapping = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    stack = []

    for char in s:
        if char in brackets_mapping:
            top_element = stack.pop() if stack else "#"

            if top_element != brackets_mapping[char]:
                return False

        else:
            stack.append(char)

    return not stack


# parenthesis = "([])"
# parenthesis = "()"
# parenthesis = "()[]{}"
# parenthesis = "]("
parenthesis = "(]"
result = is_valid(parenthesis)
print(result)
