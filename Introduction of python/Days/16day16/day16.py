
# # # # # class Car:
# # # # #     def __init__(self, brand, color):
# # # # #         self.brand = brand
# # # # #         self.color = color

# # # # # car1 = Car("Toyota", "Red")
# # # # # car2 = Car("BMW", "Black")

# # # # # print(car1.brand)  
# # # # # print(car2.color)



# # # # # class Student:
# # # # #     def __init__(self, name, roll_no):
# # # # #         self.name = name
# # # # #         self.roll_no = roll_no

# # # # # s1 = Student("Rahul", 101)
# # # # # print(s1.name)

# # # # # ----airflow ----species=mammall-------

# # # # # class Dog:
# # # # #     species = "species"  # Class variable (shared)

# # # # #     def __init__(self, name):
# # # # #         self.name = name  # Instance variable (unique)

# # # # # d1 = Dog("Bruno")
# # # # # d2 = Dog("Tommy")

# # # # # print(d2.species)  # Mammal
# # # # # print(d2.name)     # Tommy


# # # # class Math:
# # # #     pi = 3.14  # Class variable

# # # #     def __init__(self, radius):
# # # #         self.radius = radius

# # # #     def area(self):  # Instance method
# # # #         return Math.pi * self.radius * self.radius

# # # #     @classmethod
# # # #     def change_pi(cls, new_pi):  # Class method
# # # #         cls.pi = new_pi

# # # #     @staticmethod
# # # #     def greet():  # Static method
# # # #         print("Hello from Math class!")

# # # # m = Math(5)
# # # # print(m.area())
# # # # Math.greet()



# # # class Animal:
# # #     def speak(self):
# # #         print("Animal speaks")

# # # class Dog(Animal):  # Dog inherits Animal
# # #     def bark(self):
# # #         print("Woof!")

# # # # d = Dog()
# # # # d.speak()
# # # # d.bark()


# # # class Cat:
# # #     def sound(self):
# # #         print("Meow")

# # # class Dog:
# # #     def sound(self):
# # #         print("Woof")

# # # for animal in [Cat(), Dog()]:
# # #     animal.sound()


# # class Account:
# #     def __init__(self, balance):
# #         self.__balance = balance  # private 1000

# #     def deposit(self, amount):
# #         self.__balance += amount #1500

# #     def get_balance(self):
# #         return self.__balance

# # acc = Account(1000)
# # acc.deposit(500)
# # print(acc.get_balance())


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r

#     def area(self):
#         return 3.14 * self.r * self.r

# c = Circle(5)
# print(c.area())


#distructor 

class Car:
    def __init__(self, brand):
        self.brand = brand
        print(f"{self.brand} car created!")

    def __del__(self):
        # Destructor
        print(f"{self.brand} car destroyed!")

c1 = Car("Tesla")
del c1   # Explicitly calling destructor


# a=3  --- ref add =asdfghjk --- empty --- garbage collection =unrefereced object 
# b=3  ---ref add =zxcvbnm,
