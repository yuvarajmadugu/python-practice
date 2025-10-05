        #functions

# #wap to print a list and length of list using function:
# mylist = [1,2,3,4,5,6,7,8,9]
# def lenlist():
#     print(len(mylist))
# lenlist()


# # #WAP to print the elements of a list in a single line and seperate line.
# #sameline
# mylist = [1,2,3,4,5,6,7,8,9]
# def sameline():
#     print(mylist)
# sameline()
# #seprate line
# for i in mylist:
#     print(i)


# #wap to convert usd to inr:
# def usdtoinr(usd):
#     inr = usd*83
#     print(inr)
# usdtoinr(90)


#wap to print n!/(n-r)! i.e permutation:
def fact(num,r):
    sum=1

    for i in range(num,0,-1):
        sum*=i
    print(sum)

    x= num-r #3
    for i in range(x,0,-1):
        x*=i
    y=x/(num-r)
    print(y)

    print(sum/y)
    
fact(5,3)