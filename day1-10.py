                          #ESCAPE SEQUENCE:
'''
# hey yuvi
'''
from pickle import TRUE


print("i am a good boy\nas usally i am sexy too") #i want xyz
#i wrote this just for junior understanding purpose 
'''
i would have xyz
i dont like things such as xyz
why dont you mind your business   
'''
# print(i am yuvi as you know )
print("i am \"the best\"")
print("hey", 6, 7, sep="~", end="ochesan raa bulloda")
print("\ni love someone")
                              #DATATYPES:
a=1
print (a)
yuvi=21
b=yuvi
print(b)
c="yuvi"
d=TRUE
e=complex(8,2)
f=9.45


'''
for print b, 21 is printed as output if no doublequotes thats
the reason we use "" to print that inside double quote
matter,in string data type or character datatype (char)
'''

"""
print(c)
print(a+c)
#will not execute due to two different different data types
output: unsupported oprand type(s) fro +: 'int' and 'str'
if true or false is declared its bool data type
"""
 
print(type(a)) #integer int
print(type(c)) #string str
print(type(d)) #bytes / boolean bool
print(type(e)) #complex
print(type(f)) #float
                        #OPERATORS 
"""+, -, *, /, **, // .
    exercise for creating a calculator"""
g=50
h=3
print("the resultant value of", g, "+", h, "is", g + h)
print("the resultant value of", g, "-", h, "is", g - h)
print("the resultant value of", g, "*", h, "is", g * h)
print("the resultant value of", g, "/", h, "is", g / h)
print("the resultant value of", g, "/", h, "is", g / h)
                      #TYPECASTING
ab="1"
ba=2
#print(ab+ba)
#output is error if ""12, to avoid this case conversion is done
print(int(ab)+int(ba))
cd=1.9
dc=8
X=cd+dc
print("X:", cd, "+", dc, "is", cd+dc)
print(type(X))
                       #USER INPUT
mn=input("enter the first value:")
nm=input("enter the second value:")
#print(mn+nm)
#result of 2&3 is 23 
print(int(mn)+int(nm))