# my_set = {1, 2, 3, 4,4,2,1}
# print(my_set)

#typecasting 
# From a list using set()
# numbers = set([1, 2, 3, 3, 4])
# print(numbers)  # Output: {1, 2, 3, 4}


# # Empty set
# empty_set = set()
# print(type(empty_set))

#flow of excution for for Loop
# colors = {"red", "green", "blue"}
# for i in colors:
#     if i == "green":
#         print("colur is matching")
        
#     else:
#         print("invalid colour ")

   


animals = {"dog", "cat"}

# # Add single
# animals.add("lion")
# print(animals)

# Add multiple
# animals.update(["tiger", "elephant"])
# print(animals)

# # Remove
# animals.remove("cat")
# print(animals)

# Discard
# animals.discard("cow")  # No error if 'cow' not present
# print(animals)
# # Pop
# item = animals.pop()
# print("Removed:", item)

# # Clear
# animals.clear()
# print(animals)  # Output: set()Think of a set like a "collection of friends in a WhatsApp group" — no friend can be added twice.


A = {1, 2, 3}
B = {3, 4, 5}

print(A | B)   # Union → {1, 2, 3, 4, 5}
print(A & B)   # Intersection → {3}
print(A - B)   # Difference → {1, 2}
print(A ^ B)   # Symmetric Difference → {1, 2, 4, 5}