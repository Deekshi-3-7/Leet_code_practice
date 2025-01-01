"""

Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
or -1 if needle is not part of haystack.



Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.


Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

"""


def getFirstOccurrence(haystack, needle):
    len_h = len(haystack)
    print("len_h", len_h)
    len_n = len(needle)
    print("len_n", len_n)
    print("diff", len_h-len_n)

    for i in range(len_h - len_n+1):
        if haystack[i:i+len_n] == needle:
            return i
    return -1


haystack = "hello"
needle = "ll"

# result = haystack.find(needle)
# print(result)

first_occurrence = getFirstOccurrence(haystack, needle)
print(first_occurrence)
