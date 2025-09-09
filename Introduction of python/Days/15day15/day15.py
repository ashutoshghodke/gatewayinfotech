
# # # numbers = [10, 20, 30]
# # # it = iter(numbers)  # make iterator

# # # print(next(it))  # 10
# # # print(next(it))  # 20
# # # print(next(it))  # 20
# # # # print(next(it))  # 20



# # def count_up_to(n):
# #     x = 1
# #     while x <= n:
# #         yield x   # give one value
# #         x += 1

# # gen = count_up_to(8)

# # print(next(gen))  # 1
# # print(next(gen))  # 2
# # print(next(gen))  # 3
# # print(next(gen))  # 3
# # print(next(gen))  # 3
# # print(next(gen))  # 3
# # print(next(gen))  # 3
# # print(next(gen))  # 3
# # print(next(gen))  # 3 --- index out of bond 


# # def greet_decorator(say_name,say_name1):
# #     def wrapper():
# #         print("👋 Hello!")
# #         say_name()
# #         print("🎉 Bye!")
# #         say_name1()
# #     return wrapper

# # @greet_decorator

# # def say_name():
# #     print("My name is MONSTER.")

# # say_name()

# # def say_name1():
# #     print("My name is devil.")

# # say_name1()



# def greet_decorator(func):
#     def wrapper():
#         print("👋 Hello!")
#         func()
#         print("🎉 Bye!")
#     return wrapper

# @greet_decorator
# def say_name():
#     print("My name is MONSTER.")

# @greet_decorator
# def say_name1():
#     A=10
#     B=20
#     print("THE ADDITION OF 2 NO=",A+B)

# # Call the decorated functions
# say_name()
# say_name1()



# a=10
# b=0
# print(a/b)
# print("hi there ! ashutoshh this side ")

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("❌ You can’t divide by zero!")
# print("hi there ! ashutoshh this side ")

# 1 --------30- (error)------40(error)---------- 500

# try:
#     num = int("abc")
#     print(10 / num)
#     # x = 10 / 0
# except ValueError:
#     print("❌ Not a number!")
# except ZeroDivisionError:
#     print("❌ Division by zero!")


# try:
#     # num = int("5") #5
#     num = int("asdfghjk") #5
# except ValueError:
#     print("Invalid number")
# else:
#     print("✅ No error, number is:", num)
# finally:
#     print("Program finished")

