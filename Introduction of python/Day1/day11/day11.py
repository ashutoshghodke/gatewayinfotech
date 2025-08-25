import array

# Create an array of integers from a list
# my_array = array.array('i', [10, 20, 30, 40])

# # Print the array and its type
# print(my_array)
# print(type(my_array))


# fruits = array.array("u", ['a', 'b' ])  
# fruits.append('c')  
# print(fruits)  # 


import array

# fruits = array.array("u", ['a', 'b'])
# fruits.append('c')
# print(fruits.tolist())
# fruits = array.array("i", [1,2,3])  
# fruits.append(4)  
# print(fruits)  # array('u', ['a', 'b', 'c'])

# insert(i, x) → Insert at position i
# numbers = array.array('i', [10, 20, 30])  
# numbers.insert(1, 15)  
# print(numbers)  # array('i', [10, 15, 20, 30])

# pop([i]) → Removes element at index (last by default)
# numbers = array.array('i', [10, 20, 30])  
# numbers.pop(1)     # removes 30  
# print(numbers)    # array('i', [10, 20])

# remove(x) → Removes first occurrence of element
# numbers = array.array('i', [10, 20, 30, 20])  
# numbers.remove(20)  
# print(numbers)  # array('i', [10, 30, 20])/


# index(x) → Returns index of element
# numbers = array.array('i', [10, 20, 30])  
# print(numbers.index(20))  # 1


# # reverse() → Reverses array
# numbers = array.array('i', [10, 20, 30])  
# numbers.reverse()  
# print(numbers)  # array('i', [30, 20, 10])

# count(x) → Counts occurrences
# numbers = array.array('i', [10, 20, 20, 30])  
# print(numbers.count(20))  # 2

# # extend(iterable) → Add multiple elements
# numbers = array.array('i', [10, 20])  
# numbers.extend([30, 40, 50])  
# print(numbers)  # array('i', [10, 20, 30, 40, 50])

# Looping Through Array
# numbers = array.array('i', [5, 10, 15, 20])  

# for num in numbers:  
#     print(num)  


# fruits = array.array("u", ['a', 'b'])
# fruits.append('c')
# print(fruits.tolist())
fruits = array.array("i", [1,2,3])  
fruits.append(4) 
print(fruits) 
print(fruits.tolist())
