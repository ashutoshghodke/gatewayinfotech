
# # Print numbers from 1 to 5 5+1=6
# for i in range(1, 11):
#     print(i)
 
# for i in range (start,end)

# fruits = ["apple", "banana", "mango"] #list dtype
# for fruit in fruits:
#     print("I like", fruit)


# i = 1
# while i  <= 5:
#     print(i) #=1,2,3,4,5
#     i += 1  # Important! To avoid infinite loop


# password = ""
# while password != "python":
#     password = input("Enter the password: ")
# print("Correct password! Access granted.")


# Example: Stop the loop when we find the number 7
# print("Demonstrating break:")
# for num in range(1, 11):
#     if num == 7:
# #         print("Found 7! Stopping the loop.")
# #         break  # Exits the loop immediately
# #     print(num)
# # print("Loop finished.\n")

# l=[1,2,3,4,5,6,7,8,9,10]
# for i in l:
#     print(i)


# for i in [1,2,3,4,5,6,7,8,9,10]:
#     print(i)


# for i in range(1, 11):
#     print(i)

# list(map(print, [1,2,3,4,5,6,7,8,9,10]))


# Example: Skip the number 5, continue with the rest
# print("Demonstrating continue:")
# for num in range(1, 8):
#     if num == 2:
#         print("Skipping number 2.")
#         continue  # Skips the rest of the code in this iteration
#     print(num)
# print("Loop finished.\n")


# sequence=[1,2,3,4,5]
# for item in sequence:
#     if item ==4:
        
#         break
#     print(item)
    

# sequence=[1,2,3,4,5]
# for item in sequence:
#     if item ==3:
#         print(item)
#         break


# sequence=[1,2,3,4,5]
# for item in sequence:
#     if item ==3:
        
#         break
# print(item)


# Example: Placeholder - do nothing when number is 3
# print("Demonstrating pass:")
# for num in range(1, 6):
#     if num == 3:
#         pass  # Placeholder: code will be added later
#     print(num)
# print("Loop finished.\n")

from dev.config import Password,USERNAME,Secret_number

secret_number=Secret_number
print("welcome to the no.guessing game!")
print("guess the no. between 1 to 50 ")
print("you have only 5 attempt ,enter 0 to quit this game !")

for attempt in range (1,6):
    guess=int(input(f"attempt {attempt}: enter your guess:"))

    if guess==0:
        print("game stopped by pradeep")
        break

    if guess <0 :
        print("not a valid guess as the no is negative no.")
        continue
    
    if guess ==secret_number :
        print ("congrates ,you guessed it right ,pradeep")
        break
 
    elif guess >secret_number:
        print("too high ! try again")

    else:
        print("too low ,try again !")

    if attempt ==3 :
        print("the secret no is even no.")
        pass 

else:
    print("sorry ! your guess is wrong !")



