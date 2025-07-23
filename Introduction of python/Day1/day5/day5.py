


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

# from dev.config import Password,USERNAME,secret_number

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
import random

secret_number = random.randint(1, 50)
print("Welcome to the Number Guessing Game!")
print("Guess the number between 1 and 50.")
print("You have 5 attempts. Enter 0 to quit anytime.")

for attempt in range(1, 6):  # 5 chances
    guess = int(input(f"Attempt {attempt}: Enter your guess: "))

    if guess == 0:
        print("Game stopped by player.")
        break  # Exit the game immediately
    
    if guess < 0:
        print("Negative numbers are not allowed! Attempt skipped.")
        continue  # Skip this attempt

    if guess == secret_number:
        print(f"Congratulations! You guessed the number in {attempt}th attempts.")
        break  # Player wins, exit loop
    
    elif guess > secret_number:
        print("Too high! Try again.")
    
    else:
        print("Too low! Try again.")

    if attempt == 3:
        pass  # Placeholder: Add a hint feature here later

else:
    # This runs only if the for loop completes without a break
    print(f"Sorry, you're out of attempts. The number was {secret_number}.")
