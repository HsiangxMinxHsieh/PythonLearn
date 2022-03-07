# nums = [1,2,3]
# print(nums+nums)
# print(nums*3)
#
# print("ax"*3)
# # print('bx'*4)
#
# words = ["hello"]
# words.append(65)
# print(words)
# # nums.append("hello")
# print(words)
#
# print(nums.append("hello"))
# print(nums)
#
# nums = [9, 8, 7, 6, 5]
# # nums.append(4)
# nums.insert(2, 11)
# print(nums)
#
# i = 5
# while True:
#     print(i)
#     i = i - 1
#     if i <= 2:
#         break

# nums = [1,2,3]
# for num in nums:
#     print(str(num)+"\n")
#
# nums = list(range(2, 5))
# print((range(7, 5)))

# print(list(range(1,10,2)))

# for i in range(0,9,3):
#     print(i)

# for i in range(10):
#     if not i % 2 == 0:
#         print(i+1)
#
#
# def my_func():
#     nums = list[1, 2, 3]
#     for i in nums:
#         print(i)
#     return
#
#
# for i in range(0, 6, 3):
#     print(i)
#
# """
# my_func()
# """

# def add(x, y):
#     return x + y
#
#
# def square(x, y):
#     return x ** y
#
#
# print(add(square(2, 3), square(3, 7)))

# def square(x):
#     return x * x
#
#
# def print_data(func, x):
#     print(func(x))
#
#
# print_data(square, 42)

# """
# 這是第一行多行註解，可以無限行。
# 這是第二行多行註解，可以無限行。
# 這是第三行多行註解，可以無限行。
# """


# import math
#
# num = 10
# print(math.sqrt(num))

# import random
# #
# for i in range(10):
#     print(random.randint(0, 1))
#
# # print(random.random())

# from math import sqrt as a
# print(a(16))

# def print_nums(x):
#     for i in range(x):
#         print(i)
#         return

# print_nums(10)
# import traceback
#
# try:
#     b = 7
#     a = (9 / 0)
#
# except ZeroDivisionError:
#     print(traceback.format_exc())
#
#
# raise ValueError

# try:
#     a = 3 / 0
# except:
#     print("Error!")
#     raise

# assert print(1) == print(2)
# def my_func(x):
#     assert x > 0, "Is Error!"
#     print(x)
# my_func(-3)

# file = open("test.txt", "r",encoding="utf-8")
# print(file.read(10))
# print(file.read(5))
# print(len(file.readlines()))
# print(file.read(3))
# file.close()

# file = open("test2.txt", "w") #如果test不存在會建立一個新的
# print(file.write("this has been written to a file"))
# file.close()
#
# file = open("test2.txt","r")
# print(file.read())
# # file.close()
#
# file = open("test.txt", "ab")  # 如果test不存在會建立一個新的
# # "w"模式下，無論如何，檔案皆會被覆蓋。
# print(file.write(b'qq0123456789abcdef\n'))  # 寫入方法會回傳成功時，寫入的字元數
# file.close()
#
# # with open("test2.txt","r") as file:
# #     print(file.read())

# #
# file = open("test3.txt", "r")
#
# #your code goes here
# # print(file.readlines())
# n = int(input("請輸入欲查詢之天數："))
# for i in range(n):
#     file.readline()
#
# print(file.readline())
#
# file.close()

# print(None)

# maps = {22.0: 15, "Mary": "2"}
#
# # print(maps)
#
# print(maps.get("2"))
# print(maps.get("John", "Do Not Have"))
# print(maps[33])
#
# print(22.0 in maps)
#
# words = ()
# data = ()
# print(words == data)

# sqs = (0, 1, 4, 9, 16, 25, 36, 49, 64)
# print(sqs[3:7:3])
# print(sqs[-1::]) #=> (0, 16, 64)
# print(sqs[-1:5]) #=> (0, 16, 64)

# sqs = (0, 1, 4, 9, 16, 25, 36, 49, 64)
# print(sqs[7:3:-1])
# print(len(sqs[8:5:-3]))
# # print(sqs[1:-2])
#
# nums = [i * 2 for i in range(10**100) if i % 3 == 0]  # => 將0~9的內容乘以2，形成列表。
# print(nums)  # =>

# nums = [i * 2 for i in range(10) if i % 3 == 0]  # => 將0~9的內容乘以2，並過濾掉除以3於數為0的數字形成列表。
# print(nums)  # =>

# print("#, ".join(["123", "abc", "789"]))

# print("This is a Book.".upper())

# print(min(11, 123, 456))
# print(min([11, 123, 456]))
#
# nums = [1, 2, 3]
# # print(min(nums))
# # print(max(nums))
# # print(sum(nums))
# #
# # print(all([i > 2 for i in nums]))
# # print(any([i > 2 for i in nums]))
#
#
# for i, v in enumerate(nums):
#     print(i)
# #     print(v)
# file = open("q2.txt")
# txt = file.read()
# # your code goes here
# list = txt.split(" ")
# maxLen = -1
# for i, v in enumerate(list):
#     if maxLen > len(v):
#         maxLen = len(v)
#         index = i
#
# print(list[index])
#
# file.close()
# # for v in enumerate(list)
# #     print(v)

# def test(func, arg):
#     return func(func(arg))
#
# def mult(x):
#     return x * x
#
# print(test(mult, 2))

# # 使用def命名：
def square(x):
    return x * x


#
# print(square(3))
# # 使用lambda：
# print((lambda x: x * x)(4))
#
# # 將lambda給定名稱以重複使用：
# square2 = lambda x: x * x
# print(square2(5))

# nums = [1, 2, 3]
# nums2 = [3, 2, 1, 4]
# # print(list(map(square, nums)))
# # print(list(map(lambda x:x*2, nums))) #=> [2, 4, 6]
#
# # print(list(filter(lambda x: x % 2 != 0, nums)))
#
#
# def add_two(x, y):
#     return x + y
#
# print(list(map(add_two, nums, nums2)))

# def infinite_sevens():
#     while True:
#         yield 7
#
#
# for i in infinite_sevens():
#     print(i)

# def get_even(n):
#     for num in range(1, n):
#         if num % 2 == 0:
#             yield num
#
#
# print(list(get_even(10)))  # => [2, 4, 6, 8]

#
# def countDown(n):
#     while n > 0:
#         yield n
#         n -= 1
#
#
# for i in list(countDown(10)):
#     print(i)
#
# print(list(countDown(5)))

# def decor(func):
#     def wrap():
#         print("=======")
#         func()
#         print("=======")
#
#     return wrap
#
#
# # @decor  # 加上@decor代表呼叫它時會以decor方法包裝。
# def print_text():
#     print("Hello world!")

# print_text()

# def fib(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return fib(x-1) + fib(x-2)
#
# print(fib(4))

# nums = {1, 1, 2, 3, 4, 5, 3, 1, 1}
# print(nums)
# nums.add(-7)
# nums.remove(3)
# # print(4 in nums)
#
# from itertools import product, permutations
# from itertools import cycle
# from itertools import repeat
#
# letters = ("A", "B")
# print(list(product(letters,range(2))))
# print(list(permutations(letters)))
#
# # for i in cycle(4):
# #     print(i)
#     if (i >= 11):
#         break
# num = 5
# print(list(count(5)))

# def fibonacci(n):
#     # complete the recursive function
#     if n <= 1:
#         return 1
#     print(fibonacci(n - 1) + fibonacci(n))
#
#
# fibonacci(num)
#
# def fib(x):
#     if x <= 1:
#         return 1
#     else:
#         return fib(x - 1) + fib(x - 2)
#
#
# n = 7
# for i in range(n-1):
#     if i < 1:
#         print(i)
#     print(fib(i))
# print("0")  # 1
# print("1")  # 2
# print(fib(1))  # 3
# print(fib(2))  # 4
# print(fib(3))  # 5
# print(fib(4))  # 6
# print(fib(5))  # 7
# print(fib(6))  # 8
# print(fib(7))  # 9
# print(fib(8))  # 10

# nums = [1, 2, 3]
# len(nums)
# dict = {"2", 1}
# print(dict)
# dict.__contains__(3)
# print(3 in dict)
# print(dict)

class Solution(object):

    def printCombine(strData, integer):
        print(strData.add(str(int)))

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i in range(len(nums)):
            self.printCombine("i:=>", i)
            print(nums[i])
            print(target - nums[i])
            print(numMap.get(target - nums[i]))
            print(numMap)
            if (target - nums[i]) in numMap:
                return [numMap.get(target - nums[i]), i]
            else:
                numMap[nums[i]] = i


