#wap to print from 1 to 100
# for i in range(1,101):
#     print(i)
#in same line
# for i in range(1,101):
#     print(i,end=" ")


#wap to print from 100 to 1
# for i in range(100,0,-1):
#     print(i,end=" ")


#wap to print the multiplication table
# num=int(input("Enter a number: "))
# for i in range(1,11):
#     print(num*i)


#break and continue 
# for i in range(5):
#     if(i==3):
#         break
#     print(i)
# print("next part")
# for i in range(5):
#     if(i==3):
#         continue
#     print(i)


#wap to find sum of first n natural numbers:(using while)
# num = int(input("Enter a num: "))
# i=1
# sum=0
# while(i<=num):
#     sum+=i
#     i+=1
# print(sum)


#wap to find sum of first n natural numbers:(using for loop)
# n=int(input("Enter a n: "))
# s = 0
# for i in range(1,n+1):
#     s+=i
# print(s)


#wap find the factorial of first n num using for loop
# n=int(input("Enter a n: "))
# fact=1
# for i in range(n,0,-1):
#     fact*=i
# print(fact)


#wap find the factorial of first n num using while loop
# n=5
# i=n
# fact=1
# while(i>0):
#     fact*=i
#     i-=1
# print(fact)

#lists
#wap to ask the uer to enter the three names of their 3 fav movies and store them in list

# mylist=[]

# m1=input("enter movie 1: ")
# mylist.append(m1)
# m1=input("enter movie 2: ")
# mylist.append(m2)
# m1=input("enter movie 3: ")
# mylist.append(m3)
# print(mylist)

# for i in range(1,4):
#     userip = input(f"Enter fav movie {i}: ")
#     mylist.append(userip)
# print(mylist)


#wap to create a list and print numbers in list
list = [5,6,4,8,9]
output = "["
output2 = "]"
print(output, end=" ")
for i in list:
    print(f"{i}",end=" ")
print(output2)