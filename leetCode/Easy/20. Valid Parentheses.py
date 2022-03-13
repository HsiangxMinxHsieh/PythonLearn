"""
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftList = ["(", "[", "{"]
        rightList = [")", "]", "}"]

        storeList = []
        if s[0] in rightList or len(s) % 2 != 0:
            return False

        # 將每一個左括號，儲存在List
        for i in range(len(s)):
            # print("i是=>" + str(i) + " store是=>" + str(storeList))
            if s[i] in leftList:
                storeList += s[i]

                # 如果有右括號的話，比對List中，上一個value是不是對應的，如果是的話，把上一個對應的拿掉。
            else:  # 在right括號中，要比對它的上一個內容是不是對應的符號
                if len(storeList) == 0 or rightList.index(s[i]) == leftList.index(storeList[len(storeList) - 1]):
                    # 喉~一樣了，移除它！
                    if len(storeList) != 0:
                        storeList.pop(len(storeList) - 1)
                    else:  # 代表前面沒有對應的左括號，卻有這個右括號。
                        return False

                    continue
                else:
                    return False

        if len(storeList) != 0:
            return False
        else:
            return True


print("結果是=>" + str(Solution().isValid("[]))")))


"""
Result：
Runtime: 30 ms, faster than 42.70% of Python online submissions for Valid Parentheses.
Memory Usage: 13.7 MB, less than 33.79% of Python online submissions for Valid Parentheses.
"""
