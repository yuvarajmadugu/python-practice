                #OOPS

# class Student:
#     # name = "uv"
#     def __init__(self, name, age): #__init__ is special method used to initialize objects when a class is instantiated. It’s often called the constructor.
#         self.name = name
#         self.age = age
#         print("Student Object created!")

#     def hello(self):
#         print("Hello from def function")

# #while printing the below 4 lines, uncomment name in Student class and remove name, age parameters in the constructor or __init__ method
# # s1 = Student()        #s1 is object of Student class
# # print(s1)             #object address
# # print(s1.name)        #prints name from Student class
# # s1.hello()            #calls hello method from Student class

# #giving object data
# s1 = Student("uv", 20)  #instance of class is object 
# print(s1.name)
# print(s1.age)
# s1.hello()

# s2 = Student("ss", 22)
# print(s2.name)
# print(s2.age)
# s2.hello()


# #wap that creates a student class that takes names & marks of 3 subjects as arguments in constructor. Then create a method to print the average
# class Stud:
#     def __init__(self, name, m1, m2, m3):
#         self.name = name
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#         print("Student object created and attributes as name, m1, m2, m3 are taken.")
#         print(f"Name: {name}, M1: {m1}, M2: {m2}, M3: {m3}")

#     def avg(self):
#             average = (self.m1 + self.m2 +self.m3)/3
#             print(f"Average of all marks is {average}")
   
# s1 = Stud("UV", 90, 89, 79)
# s1.avg()


# create a  Circle class where in parameter radius is given and area() and perimeter() is calculated. { (Area = Pie*r*r) and (Perimeter = 2*Pie*r) }
class Circle:
    def __init__ (self, radius):
        self.radius = radius
    
    def area(self):
        pie = 3.14
        area = pie*self.radius*self.radius
        print(f"Area of circle: {area}")

    def perimeter(self):
        pie = 3.14
        perimeter = 2*pie*self.radius
        print(f"Perimeter of circle: {perimeter}")

    def get_results(self):
        print(f"Area: {self.area()}")
        print(f"Circumference: {self.perimeter()}")

c1 = Circle(20)
c1.area()
c1.perimeter()