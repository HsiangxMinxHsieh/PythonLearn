class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        dict49 = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        # 先判斷有沒有4和9的羅馬文字，並拿掉
        for k, v in dict49.items():
            if s.__contains__(k):
                s = s.replace(k, "")
                result += v

        # 剩下計算單一的有幾個
        dict15 = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        for k, v in dict15.items():
            if s.__contains__(k):
                # 這裡要計算共有幾個k
                for c in s:
                    if c == k:
                        result += v

        print("當前s是=>" + str(s))

        return result


print(Solution().romanToInt("MMMIX"))
