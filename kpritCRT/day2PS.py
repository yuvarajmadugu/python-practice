#wap to check if a number entered by user is even or odd
# num = int(input("Enter a number to check if it is even or odd: "))
# if num % 2 == 0:
#     print(f"{num} is even.")
# else:
#     print(f"{num} is odd.")


#wap username format checker:
#Task: If it contains a space, print "Invalid username." or if its < 4 characters, print "Username too short." Else, print "Valid username."
# username = input("Enter a username: ")
# if " " in username:
#     print("Invalid username.")
# elif len(username) < 4:
#     print("Username too short.")
# else:
#     print("Valid username.")
    

#wap to find the greatest of 3 numbers entered by the user
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
# if a >= b and a >= c:
#     greatest = a
# elif b >= a and b >= c:
#     greatest = b
# else:
#     greatest = c
# print(f"The greatest number is: {greatest}")



#wap to check if a number is a multiple of 7 or not.
# num = int(input("Enter a number: "))
# if num % 7 == 0:
#     print(f"{num} is a multiple of 7.")
# else:
#     print(f"{num} is not a multiple of 7.")



#wap to build a form validation:
# Ask user for input
full_name = input("Enter your full name: ").strip()
email = input("Enter your email address: ").strip()
password = input("Enter your password: ")

# Validation flags
is_valid = True

# Validate Full Name
if not full_name or " " not in full_name:
    print("Invalid full name")
    is_valid = False

# Validate Email Address
elif "@" not in email or not email.endswith(".com"):
    print("Invalid email address")
    is_valid = False

# Validate Password
elif len(password) < 6 or " " in password:
    print("Weak or invalid password")
    is_valid = False

# Final success message
if is_valid:
    print("Form submitted successfully")



#wap to validate an email with "@"" and ".com" at the end
# email=(input("Enter an email: "))
# if "@" in email and email.endswith(".com"):
#     print("valid email")
# else:
#     print("invalid")
# #to check endswith(".com") without this function:
# val = email[-4:]
# print(val)


