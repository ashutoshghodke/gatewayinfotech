
# empty_tuple = ()
# print(empty_tuple)
# empty_tuple2 = tuple()
# print(empty_tuple2)
# print(type(empty_tuple2))


# lst=[1,2,3,4,5]
# tup=tuple[1,2,3,4,5]
# print(type(tup))
# print(type(lst))

# tup=(1,2,3,4)
# l1=list(tup)
# print(type(l1))



# fruits = ("apple", "banana", "cherry")

# print(fruits[-1])  # Output: apple

# print(fruits[2])  # Output: cherry

# print(fruits[-1]) # Output: cherry (counting from the end)



# votes = ("yes", "no", "yes", "yes")

# yes_votes = votes.count("yes")
# print(yes_votes)
# no_votes = votes.count("no")
# print(no_votes)

# pets = ["dog", "cat", "fish", "cat",10,22,"fish"]
# cat_index = pets.index("fish")
# print(cat_index)

# colors = ("red", "green", "blue", "green")
# green_index = colors.index("green")
# print(green_index) # Output: 1


# coordinates = (10, 20)

# x, y = coordinates

# print(x) # Output: 10

# print(y) # Output: 20

# clas= ("sanket","pradeep","rohini")
# a,b,c=clas
# print(a)
# print(b)
# print(c)


# personal_info = ("John", 30)

# location = ("New York", "USA")

# full_profile = personal_info + location
# print(full_profile)


# short_tuple = (12)
# short_tuple = [12]
# long_tuple = short_tuple * 3
# print(long_tuple)


# weekdays = ["Monday", "Tuesday", "Wednesday"]
# weekdays = ("Monday", "Tuesday", "Wednesday")
# print("Monday" in weekdays) # Output: True

# print("Sunday" in weekdays) # Output: False



# # Nested Tuples:
# nested = ((1, 2), (3, 4))
# print(nested[1][0])  # 2


# ✈️ Flight Seat Bookings - List, Tuple, and Set Example (Beginner Friendly)

# Step 1: Data (List of Tuples - each tuple = fixed row seating)
bookings = [
    ("Amit", "Ravi", "Priya"),   # Row 1
    ("Sita", "Rahul", "Neha"),   # Row 2
    ("Amit", "Ravi", "Priya"),   # Row 3 (duplicate of Row 1)
    ("Vijay", "Meena", "Arun")   # Row 4
]

# Step 2: Show all bookings (LIST allows duplicates)
print("📋 All Seat Bookings (List Format):")
row_number = 1
for row in bookings:
    print("Row", row_number, ":", row)
    row_number += 1

print("-" * 40)

# Step 3: Convert List → Set to find UNIQUE bookings
unique_bookings = set(bookings)

print("✅ Unique Seat Arrangements (Set Format):")
for row in unique_bookings:
    print(row)

print("-" * 40)

# Step 4: Count unique arrangements
print("Total Unique Arrangements:", len(unique_bookings))

print("-" * 40)

# Step 5: Search for a passenger in the bookings
search_name = input("🔍 Enter a passenger name to search: ").strip()

found_rows = []
row_number = 1
for row in bookings:
    if search_name in row:
        found_rows.append(row_number)
    row_number += 1

if found_rows:
    print(f"🎯 {search_name} is seated in Row(s):", found_rows)
else:
    print(f"❌ {search_name} is not found in any booking.")
