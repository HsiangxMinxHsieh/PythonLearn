"""
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

"""


def printCombine(strData, integer):
    print(strData + str(integer))


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i in range(len(nums)):
            printCombine("i:=>", i)
            printCombine("nums[i]:=>", nums[i])
            printCombine("target-nums[i]:=>", target - nums[i])
            printCombine("numMap.get(target-nums[i]):=>", numMap.get(target - nums[i]))
            printCombine("numMap:=>", numMap)

            if (target - nums[i]) in numMap:
                return [numMap.get(target - nums[i]), i]
            else:
                numMap[nums[i]] = i


print("結果是=>" + str(Solution().twoSum([2, 3, 7, 8, 9], 10)))
