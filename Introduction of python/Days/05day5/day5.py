


"""
# print("WELCOME TO THE ELECTION BOARD OF MAHARASHTRA ")

# age=age = int(input("Enter your age: "))

# if age <18 :
#     print("USER NOT VALID TO VOTE ")

# elif age >50 :
#     print("USER NOT VALID TO VOTE ")

# else:
#     print("USER IS VALID TO VOTE ")


# marks=int(input("Enter your Marks: "))

# if marks>=90:
#     print("grade A")

# elif marks>=75 :
#     print("grade B")

# elif marks>=50:
#     print("grade C")

# else:
#     print("fail")

 from dev.config import Password,USERNAME,secret_number

# print("welcome to the magic show ")

# guess=int(input("guess a number between 1 to 10:"))

# if guess == secret_number:
#     print("you guessed it right")
# else:
#     print("you guessed it wrong")

# password=int(input("enter your password"))
# username=input("enter your username")
# if password ==Password and username==USERNAME:
#     print("access granted")
# else:
#     print("access denied")
"""
from dev.config import treasure

# Treasure dictionary (secret box)
treasure = {
    "Red Room": "treasure 💎",
    "Blue Room": "treasure🪙",
    "Green Room": "treasure ⚔️",
    "Black Room": "treasure 😢"
}

print("Welcome to the Treasure Hunt Game!")

# Ask student to choose a room
choice = input("Which room do you want to enter? (Red Room/Blue Room/Green Room/Black Room): ")

# Find treasure
if choice in treasure:
    print("You found:", treasure[choice])
else:
    print("This room does not exist!")
