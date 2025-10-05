# class Car():
#     def __init__(self, brand):
#         self.brand = brand
#         self.acc = True
#         self.clutch = True
#         self.brake = True
#         print(f"{self.brand} Car object created...")

#     def start(self):
#         self.acc = True
#         self.clutch = True
#         self.brake = False
#         print("Car started...")

#     def stop(self):
#         self.acc = False
#         self.clutch = True
#         self.brake = True
#         print("Car stoped...")

# c1 = Car("Tata-Harrier")
# c1.start()
# c1.stop()


class Account:
    def __init__(self, Balance, Account_no, password):
        self.Balance=Balance
        self.Account_no=Account_no
        self.__password= password
        #__password is a private parameter which can only be accessed in the current class,
        #if you want to access a private parameter you must create a seperate another function in the same class
        # and call the new function created in the class 

    def get_Balance(self):
        print(self.Balance)
    
    def debit(self,amount):
        if amount>self.Balance:
            print("Insufficient Balance")
        else:
            self.Balance -= amount
            print("Rs.", amount,"was debited.")
            print("The Total Balance is = ",self.get_Balance())

    def credit(self,amount):
        self.Balance += amount
        print("RS.",amount,"was Credited.")
        print("The Total Balance is = ",self.get_Balance())


    def complexDetails(self):
        print(self.__password)     


   
# a1= Account(2000, 753951, "paisal lev")
# a1.complexDetails()
# a1.get_Balance()
# a1.debit(5000)
# a1.debit()
# a1=Account(1000,12345)
# a1.debit(1000)
# a1.credit(10000)
# a1.debit(7500)
# a1.credit(40000)
# a1.debit(100)