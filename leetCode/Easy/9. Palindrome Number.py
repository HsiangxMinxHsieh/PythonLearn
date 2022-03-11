"""
9. Palindrome Number

Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1

"""


def getTheDigit(x):
    if x // 10 == 0:
        return 0
    else:
        return getTheDigit(x // 10) + 1


def get10Pow(x):
    if x <= 1:
        return 10
    else:
        return get10Pow(x - 1)\
               * 10


def reverseTheNum(x):
    if x < 10:
        return x
    else:
        return x % 10 * get10Pow(getTheDigit(x)) + reverseTheNum(x // 10)


class Solution(object):

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            return x == reverseTheNum(x)


print(Solution().isPalindrome(223322))
