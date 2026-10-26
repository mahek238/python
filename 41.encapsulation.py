class Student:
 def __init__(self, name, age):
    self.__name = name # private
    self.__age = age # private
 def show(self):
    print(f"Name: {self.__name}, Age: {self.__age}")
 def set_age(self, age):
    if age > 0:
        self.__age = age
s = Student("Yash", 21)
s.show()
s.set_age(22)
s.show()