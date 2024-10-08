"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

"""


def longest_common_prefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]
    for string in strs[1:]:
        while string[:len(prefix)] != prefix:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


prefix_words = ["flower", "flow", "flight"]
# prefix_words = ["dog", "racecar", "car"]
# prefix_words = "prefix"
# prefix_words = 1997
result = longest_common_prefix(prefix_words)
print(result)
