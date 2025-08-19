# students = {
#     "Amit": 85,
#     "Sneha": 92,
#     "Ravi": 78,
#     'sanket':59,
#     'pradeep':59
# }


# students["sanket"]=59
# del students[59]
# print(students)
# print(students.values())
# print(students.values)
# print(students.keys())
# data governance ----> data security 


# suspects = {
#     "Ravi": {"place": "Market", "item": "Banana"},
#     "Sneha": {"place": "School", "item": "Book"},
#     "Amit": {"place": "Bank", "item": "Gold Coin"},
#     "Priya": {"place": "Park", "item": "Ball"},
#     "Karan": {"place": "Cinema", "item": "Ticket"}
# }


# print ("welcome in the team of detective Rohini ")

# for name,details in suspects.items():
#     if details ['place']=="Bank" and details['item']=="Gold Coin" :
# #         print("the thief is :" , name, "!!!")



# suspects = [
#     ["Ravi", "Market", "Banana"],
#     ["Sneha", "School", "Book"],
#     ["Amit", "Bank", "Gold Coin"],
#     ["Priya", "Park", "Ball"],
#     ["Karan", "Cinema", "Ticket"]
# ]

# print("Welcome to the team of detective Rohini!")

# for suspect in suspects:
#     name, place, item = suspect
# #     if place == "Bank" and item == "Gold Coin":
# #         print("The thief is:", name, "!!!")
# #         break



# names = ["Ravi", "Sneha", "Amit", "Priya", "Karan"]
# places = ["Market", "School", "Bank", "Park", "Cinema"]
# items = ["Banana", "Book", "Gold Coin", "Ball", "Ticket"]

# print("Welcome to the team of detective Rohini!")

# for name, place, item in zip(names, places, items):
#     # if place == "Bank" and item == "Gold Coin":
#     #     print("The thief is:", name, "!!!")
#     #     break
#     print(names, places, items)

names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

zipped_list = zip(names, ages)

# To see the result, you need to convert the zip object to a list
print(list(zipped_list))
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]