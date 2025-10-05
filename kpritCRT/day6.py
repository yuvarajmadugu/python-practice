                        #recursion

# #tricky function:
# def  show(n):
#     if (n == 0):
#         return
#     print(n)

#     show(n-1)
#     print(f"output from inside of function {n}")

# show(5)
# print("putput from outside of function")


#write a recursive function to calculate the sum of first n natural numbers:
# def calNaturalnums(n):

#     if(n==0):
#         return
#     sum += n
    
#     calNaturalnums(n-1)
#     print(sum)


# def calNaturalnums(n):
#     def sum():
#         sum = 0
#         if(n==0):
#             return
#         sum+=n
#         calNaturalnums(n-1)
    
# calNaturalnums(5)
#cal natural nums fail not working




                #files handling i/o:
#create a new file "practice.txt". add the following data in it:
fileName=open("practice.txt","w")
fileName.write("hi\neveryone")
fileName.close()

#to read .txt file in terminal:
a = open("practice.txt")
data = a.read()
print(data)
fileName.close

#replace data in the file:
b= open("practice.txt")
data = b.read()
replaced = data.replace("everyone","yuvi")
print(replaced)
fileName.close()

c= open("practice.txt","w")
c.write(replaced)







