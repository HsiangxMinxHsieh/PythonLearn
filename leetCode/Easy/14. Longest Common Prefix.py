"""
14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

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
strs[i] consists of only lower-case English letters.


"""


def compareTwoStringAndFindSame(str1, str2):
    result = ""
    # 1. 解析這兩個字串，比較相同的部分加在result，若不相同則break。
    if str1 == "" or str2 == "":
        return ""

    for i in range(min(len(str1), len(str2))):
        if str2[i] != str1[i]:
            break
        else:
            result += str1[i]

    # 2. 依照剩下的字串比照當前的result是否相同(for迴圈)

    return result


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 0. 非法檢查：
        # (1).如果只有一個字串，則回傳第一個字串
        # (2).前兩個字串若有空字串，則直接回傳空字串。
        if len(strs) <= 1:
            return strs[0]

        if strs[0] == "" or strs[1] == "":
            return ""

        result = compareTwoStringAndFindSame(strs[0], strs[1])
        for i in (range(0, len(strs))):
            result = compareTwoStringAndFindSame(result, strs[i])

        return result


print("結果是=>" + Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix(["a111", "1456", "178", "111"]))
