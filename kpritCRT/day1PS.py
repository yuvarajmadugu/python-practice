# x = input("Enter a number: ") #throws error you must add int(input("Enter a num: "))
# y = 5
# print(x + y)


# a = "5"
# b = 3
# c = a * b
# print(c) #results 555


# result = 3 * (4 + 2) - 5
# print(result) #13 


# result = 3 + 6 * (5 + 4) ** 2 / 3
# print(result) #165.0


#wap that prompts the user for their name, age, and city, then prints a message in the format:
# name = str(input("Enter your name: "))
# age = int(input("Enter your age: "))
# city = input("Enter the city you live in: ")
# print(f"Hello {name}, you are {age} years old and live in {city}.")


#wap that asks the user for their first and last name and then prints the full name in the format:
# firstname = (input("Enter your firstname: "))
# lastname = (input("Enter your lastname: "))
# print(f"First Name: {firstname}, Last Name: {lastname}")


#wap to input a side & print its area. (Area = Side x Side)
# Side = int(input("Enter the side value: "))
# Area = Side*Side
# print(f"Area of mentioned side is: {Area}")


#wap to input 2 floating point numbers & print their Average.
# num1 = float(input("Enter a num: "))
# num2 = float(input("Enter a num: "))
# avg = (num1+num2)/2
# print(avg)


#wap to Input two integers from the user and print true if a>b else false
# a = int(input("Enter the first number (a): "))
# b = int(input("Enter the second number (b): "))
# print(a >= b)


# #wap to input users first name and print his name and its length
# name= str(input("Enter user name: "))
# print(f"User name: {name}")
# length=len(name)
# print(length)


# #wap that checks whether the first and last characters of a string are the same. Print true or false
# name= str(input("Enter user name: ").lower())
#     #checking if the string is empty or not
# if len(name)>0 and name[0] == name[-1]:
#      print(True)
# else:
#      print(False)


#wap to input users firstname and print its length. Check the occurrence of the alphabet "a" 
# name=(input("Enter a name: "))
# count_a= name.count("a")
# print(count_a)
    
     
#wap to input from the user and check if it's a palindrome(same from back and front)
# name=input("Enter a name: ")
# print(name)
# reversed = name[::-1]
# print(reversed)
# if name == reversed:
#     print(True)
# else:
#     print(False)

# palindrome
# name=input("enter name: ")
# print(name[0::])  #from the beginning to the end
# print(name[::-1]) #from the end to the beginning
# print(name[0:5])  #from the beginning to the 5th character
# print(name[0:5:2]) #from the beginning to the 5th character with a step of 2
# print(name[0:len(name)]==name[::-1]) #from the beginning to the end and from the end to the beginning are equal

# word=input('word:')
# example=word[0:len(word)]
# reverse=word[-1:-len(word)-1:-1]