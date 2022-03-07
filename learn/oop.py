# class Animal:
#     def __init__(self, legs):
#         self.legs = legs
#
#     def myLegs(self):
#         print("I have " + str(self.legs) + " legs")
#
#
# # class Cat:
# #     def __init__(self, color, legs):
# #         self.color = color
# #         self.legs = legs
# #
# #
# # felix = Cat("ginger", 4)
# # rover = Cat("dog-color", 4)
# # stumpy = Cat("brown", 3)
#
# class Dog(Animal):
#     def __init__(self, name):
#         super().__init__(4) ##如果父類別有建構子，子類別的建構子通常都要呼叫父類別的建構子以完成初始化。(可以不呼叫，但是使用父類別的屬性就會AttributeError。)(沒有此屬性)
#         self.name = name
#
#     def bark(self):
#         print("My Name is " + self.name + ", I have " + str(self.legs) + " legs")
#
#
# fido = Dog("Little White")
# fido.bark()  #=> My Name is Little White, I have 4 legs
# print(fido.legs) #=> 4 ## 繼承自父類別的屬性
# fido.myLegs() #=> I have 4 legs  ## 繼承自父類別的方法(直接呼叫


class Animal:
    def __init__(self, ):
        print("Animal Init")


class Tiger(Animal):
    def __init__(self):
        print("Tiger begin init")
        super().__init__()
        print("Tiger end init")


class Lion(Animal):
    def __init__(self):
        print("Lion begin init")
        super().__init__()
        print("Lion end init")


class LionTiger(Lion, Tiger):

    def __init__(self):
        print("LionTiger begin init")
        super().__init__()
        print("LionTiger end init")


LionTiger()
