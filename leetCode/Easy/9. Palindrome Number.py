def getTheDigit(x):
    if x // 10 == 0:
        return 0
    else:
        return getTheDigit(x // 10) + 1


def get10Pow(x):
    if x <= 1:
        return 10
    else:
        return get10Pow(x - 1) * 10


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
