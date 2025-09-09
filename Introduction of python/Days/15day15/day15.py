# /


# # try:
# #     x = 10 / 0
# # except ZeroDivisionError:
# #     print("Cannot divide by zero")

# try:
#     num = int("abc")
#     print(10 / num)
# except ZeroDivisionError:
#     print("❌ Division by zero!")
# except ValueError:
#     print("❌ Not a number!")
# a=10
# num = int("abc")

# print(num/a)

try:
    num = int("5")
except ValueError:
    print("Invalid number")
else:
    print("✅ No error, number is:", num)
finally:
    print("Program finished")