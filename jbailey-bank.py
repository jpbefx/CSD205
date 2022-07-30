####    James Bailey CSD205_Module12: Final. Due Sat. May 14th, 2022.   ####
####                                    Works Cited:

####        https://github.com/Chrisgarlick/Python_Projects/blob/main/My_Projects/Banking_system.py
####        https://careerkarma.com/blog/python-inheritance/
####        https://stackoverflow.com/questions/55970682/in-python-how-do-i-update-the-balance-when-i-withdraw-money-then-deposit-money

##  Requirements:
#       BankAccount values: 
#           accountnumber
#           balance_CheckingAccount
#           balance_SavingsAccount
#               Functions:
#                   withdraws()
#                   deposits()
#                   getBalance()
#       CheckingAccount values:
#           fees
#           minimumbalance
#               Functions:
#                   deductFees()
#                   checkMinimBalance()
#       SavingsAccount values:
#           interestrate
#               Functions:
#                   addInterest()



##############  **LOST COUNT** attempt   ##############
#  Create User class, set name



class User:
    """save the user's name to memory to call later"""
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
#  Create a BankAccount class, import user, set name, acc#, and balance
class BankAccount(User):
    """save BankAccount information with Methods and Parent/Child classes"""
    total_deposits = 0
    total_withdraws = 0
    accountNumber = "2001009003"

    def __init__(self, name, age, balance):
        super().__init__(name, age)
        self.balance = balance

    def getBalance(self):
        """Return the current balance."""
        return f"{self.name}, you have a balance of: ${self.balance}"

#   Create deposit Method, set deposit amount, add the amount to the balance and return the new balance.   
    def deposit(self):
        """Set and add the current deposit."""
        try:
            amountDeposit = float(input("How much would you like to deposit?"))      
            print("Thank you for depositing")
            self.balance += amountDeposit
            self.total_deposits += 1
            return f"Your balance is now: ${round(self.balance)}."
        except ValueError:
            print("Please input a numerical value.")

#   Create withdraw Method, set withdraw amount, subtract the amount from the balance and return the new balance.
    def withdraw(self):
        """Set and subtract the current withdraw."""
        try:
            amountWithdraw = float(input("How much would you like to withdraw?"))
            print("Thank you for your withdraw.")
            if amountWithdraw > self.balance:
                print(f"We're sorry, {name} you do not have sufficient funds.\nYour balance is ${self.balance}.")
            else:
            
                print("Thank you for your business")
                self.balance -= amountWithdraw
                self.total_withdraws += 1
                return f"Your balance is now: ${round(self.balance)}."
        except ValueError:
            print("Please input a numerical value.")


#   Create CheckingAccount, import BankAccount, set name, acc#, balance, fees, and minBalance
class CheckingAccount(BankAccount):
    """Initialize CheckingAccount information"""
    def __init__(self, name, accountNumber, balance):
        """Initialize the CheckingAccount."""
        super().__init__(name, accountNumber, balance)
        accountNumber = accountNumber + "01"

#   define deductFees Method, set fees
    def deductFees(self):
        """Deduct the fees from the balance."""
        fees = float(5)
        if fees > self.balance:
            return f"Were sorry, your fees this month of ${fees} has cost you more than you have in your account.\nPlease deposit more money to your account."
        else:
            return f"Your balance is now: ${round(self.balance)}."


#   Define checkMinimunBalance Method, set balance. 
#   Check to see if balance is less than 50
#   If True let the user know, if false continue
    def checkMinimumBalance(self):
        """Make sure the balance is at least $50.00."""
        if self.balance < float(50):
            return f"Your balance of ${self.balance} is less than $50.00.\nPlease deposit at least ${float(50) - self.balance}."
        else:
            return f"Your balance is now: ${round(self.balance)}."

#   Create SavingsAccount, import BankAccount, set name, acc#, balance, fees, minBalance, and interestRate
class SavingsAccount(BankAccount):
    def __init__(self, name, accountNumber, interestRate, balance):
        """Initialize the SavingsAccount."""
        super().__init__(name, accountNumber, balance)
        self.interestRate = interestRate

#   Define addInterest Method, set interestRate
#   Divide balance by 100 multipy by 2
#   return interestTotal
    def addInterest(self):
        """Add the interest rate to the balance."""
        interestRate = int(2) / 100
        self.balance += interestRate
 
 
#   difine a set of numbers 1-6 as a menu for the user, catch improper inputs
def options():
    """Provide the user with options."""
    print("Thank you for creating your JBailey Bank account!")
    print("Here are a list of options, please choose a number for the option you want: ")
    while True:
        option_choice = int(input("1) See Balance\n2) Make A Withdraw\n3) Make A Deposit\n4) See Total Withdraws\n5) See Total Deposits\n6) Quit\n"))
        if option_choice == 1:
            print(user_one_bank.getBalance())
        elif option_choice == 2:
            print(user_one_bank.withdraw())
        elif option_choice == 3:
            print(user_one_bank.deposit())
        elif option_choice == 4:
            print(f"There have been {user_one_bank.total_withdraws} withdraws")
        elif option_choice == 5:
            print(f"There have been {user_one_bank.total_deposits} deposits")
        elif option_choice == 6:
            print("Thank you for using JBailey bank. Please come again soon.")
            return False
        else:
            print("Please enter a number 1-6, only.")

def bank_creation():
    """Create the balance througout everything."""
    balance = float(200)
    return balance

#   a loop of driver code to execute, then exit to the options function.
while True:
    print("Welcome to James Bailey's Bank")
    name = input("Please enter your name: ")
    age = int(input("Enter your current age."))
    current_user = User(name, age)
    print("Thank you for registering. Please create your bank account.")
    current_user_balance = bank_creation()
    user_one_bank = BankAccount(current_user.name, current_user.age, current_user_balance)
    flag = options()
    if flag == False:
        break




#############   Yet Another Attempt     ####################

#class BankAccount():
#    total_deposits = 0
#    total_withdraws = 0
#
#    def __init__(self, name, accountNumber, balance):
#        self.accountNumber = accountNumber
#        self.balance = balance
#        self.name = name
#    
#    def withdraw(self):
#        amountWithdraw = float(input("Please input the amount you would like to deposit."))
#        amountWithdraw += self.balance
#        self.total_withdraws += 1
#
#    def deposit(self):
#        amountDeposit = float(input("Please input the amount you would like to deposit."))
#        amountDeposit -= self.balance
#        self.total_deposits += 1
#
#
#    def getBalance(self):
#        return self.balance
#
#
#class CheckingAccount(BankAccount):
#    def __init__(self, name, accountNumber, balance, fees, minimumBalance):
#        super.__init__(name, accountNumber, balance)
#        self.minimumBalance = minimumBalance
#        self.fees = fees
#
#    def deductFees(self):
#        fees = float(5)
#        fees -= self.balance
#        print(self.balance)
#
#    def checkMinimumBalance(self):
#        if self.balance < float(50):
#            print(f"You are below your minimum balance of $50.00.\nPlease deposit at least ${float(50) - self.balance}")
#
#
#class SavingsAccount(BankAccount):
#    def __init__(self, name, accountNumber, balance, interestRate):
#        super.__init__(name, accountNumber, balance)
#        self.intrestRate = interestRate
#        interestRate = int(2) / 100
#
#    def addInterest(self):
#        self.intrestRate += self.balance
#        print(self.balance)
#
#
#
#
#
#def options():
#    print("Thank you for creating your Bank account!")
#    print("Here are a list of options, please choose a number for the option you want: ")
#    while True:
#        option_choice = int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraws\n5) See Total Deposits\n6) Quit\n"))
#        if option_choice == 1:
#            print(current_user.getBalance)
#        elif option_choice == 2:
#            print(current_user.withdraw)
#        elif option_choice == 3:
#            print(current_user.deposit)
#        elif option_choice == 4:
#            print(f"There have been {current_user.total_withdraws} withdraws")
#        elif option_choice == 5:
#            print(f"There have been {current_user.total_deposits} deposits")
#        elif option_choice == 6:
#            print("Thank you for using your bank. Please come again soon.")
#            return False
#            
#        else:
#            print("Please choose a correct number from 1-7")
#
#
#while True:
#    current_user = BankAccount(name, accountNumber, balance)
#    name = input("Please enter your name.")
#    accountNumber = "2001009003"
#    balance = float(200)
#    flag = options()
#    if flag == False:
#        break


###########     Another Attempt     ##################


#class User:
#    def __init__(self, name):
#        self.name = name
#
#    def show_details(self):
#        return f"Thank you, {self.name.title()}"
#
#class BankAccount(User):
#    total_deposits = 0
#    total_withdraws = 0
#
#    def __init__(self, name,balance):
#        super().__init__(name)
#        self.balance = balance
#
#    def bank_creation(self):
#        self.balance = balance
#        return balance
#
#    def show_info(self):
#        return f"{self.name} has a remaining balance of: £{self.balance}"
#
#    def deposit(self):
#        dp = float(input("Please enter how much you would like to input: "))
#        print("Thank you for depositing...")
#        self.balance += dp
#        self.total_deposits += 1
#        return f"Your balance is now: £{round(self.balance, 2)}"
#
#    def withdraw(self):
#        wd = float(input("Please enter how much you would like to withdraw: "))
#        print("Thank you for withdrawing...")
#        self.balance -= wd
#        self.total_withdraws += 1
#        return f"Your balance is now: £{round(self.balance, 2)}"
#
#def options():
#    print("Thank you for creating your Bank account!")
#    print("Here are a list of options, please choose a number for the option you want: ")
#    while True:
#        option_choice = int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraws\n5) See Total Deposits\n6) Quit\n"))
#        if option_choice == 1:
#            print(BankAccount.show_info())
#        elif option_choice == 2:
#            print(BankAccount.withdraw())
#        elif option_choice == 3:
#            print(BankAccount.deposit())
#        elif option_choice == 4:
#            print(f"There have been {BankAccount.total_withdraws} withdraws")
#        elif option_choice == 5:
#            print(f"There have been {BankAccount.total_deposits} deposits")
#        elif option_choice == 6:
#            print("Thank you for using your bank. Please come again soon.")
#            return False
#            break
#        else:
#            print("Please choose a correct number from 1-6")
#
#
#    
#
#balance = float(200)
##user = User()
#name = input("Please enter your name: ")
#print("Welcome to the BC Bank")
#user_balance = BankAccount.bank_creation
#user_bank = BankAccount(name, user_balance)
#options()
#



######################################################

# class BankAccount():
# 
    # def __init__(self, acct_no, balance):
        # if balance < 0:
            # raise ValueError('Balance cannot be negative')
        # self._account_number = acct_no
        # self._balance = balance
# 
    # def withdraw(self, amount):
        # if amount < 0:
            # raise ValueError("Withdrawn amount is negative.")
        # if amount > self._balance:
            # raise ValueError('Dont have sufficient balance')
        # self._balance -= amount
# 
    # def deposit(self, amount):
        # if amount < 0:
            # raise ValueError("Deposit amount is negative.")
        # self._balance += amount
# 
    # def getBalance(self):
        # return self._balance
# 
# 
# class CheckingAccount(BankAccount):
# 
    # def __init__(self, acct_no, balance, fees, minimumBalance):
        # super().__init__(acct_no, balance)
        # self._fees = fees
        # self._minimumBalance = minimumBalance
        # if self.checkMinimumBalance():
            # self.deductFees()
# 
    # def deductFees(self):
        # print('${} deducted for not maintaining sufficient balance'.format(self._fees))
        # self._balance -= self._fees
# 
    # def checkMinimumBalance(self):
        # return self.getBalance() < self._minimumBalance
# 
# 
# def withdraw(self, amount):
    # super().withdraw(amount)
# 
    # if self.checkMinimumBalance():
        # self.deductFees()
# 
# 
# def __str__(self):
    # return 'Account Number: {}, Current Balance: ${:.2f}'.format(self._account_number, self.getBalance())
# 
# 
# class SavingsAccount(BankAccount):
    # def __init__(self, acct_no, balance, interest_rate):
        # super().__init__(acct_no, balance)
        # self._interest_rate = interest_rate
# 
    # def addInterest(self):
        # interest = self.getBalance() * self._interest_rate / 100
        # self.deposit(interest)
# 
# 
# def main():
    # id = input('Enter checking account id: ')
    # balance = float(input('Enter checking account initial balance: '))
    # min_balance = float(input('Enter minimum balance to be maintained: '))
    # fees = float(input('Enter fees to be deducted for not maintaining minimum balance: '))
    # try:
        # checkAccount = CheckingAccount(id, balance, fees, min_balance)
        # print(checkAccount)
    # except Exception as e:
        # print(str(e))
# 
# 
# main()

#######################################################

# class BankAccount(object):
    # def __init__(self, initial_balance=0):
        # self.balance = initial_balance
    # def deposit(self, amount):
        # self.balance += amount
    # def withdraw(self, amount):
        # self.balance -= amount       
    # def get_balance(self, initial_balance, rate):
        # return self.get_balance() * self._rate
# 
# class BankAccountWithInterest(BankAccount):
#   def __init__(self, initial_balance=0, rate=0.1):
    #  BankAccount.__init__(self, initial_balance)
    #  self._rate = rate           
#   def interest(self):
    #  return self.balance * self._rate
# 
# 
# balance = (float(100))
# my_account = BankAccount(balance)
# my_interest = BankAccountWithInterest(balance)
# print(my_account.balance)
# print(my_interest.balance + my_interest.interest())



# 
# 






##############  Second Attempt  ##############

# class User:
    # """Create a new username for the account."""
    # def __init__(self, name):
        # self.name = name
# 
    # def show_details(self):
        # Return the result of the user's input for their name.
        # return f"{self.name}, thank you for your business!"
    # 
# 
# class BankAccount(User):
    # """Create a new bank account with the user's name"""
    # def __init__(self, name, accountNumber, startingBalance):
        # super().__init__(name)
        # assign startingBalance 
        # assign the accountNumber
        # self.accountNumber = accountNumber
        # self.startingBalance = startingBalance
        # self.account = startingBalance
    # 
    # def deposit(self, amount):
        # """Apply a deposit method to call later."""
        # Ask the user how much they want to deposit and add it to the balance.
        # self.amount = amount
        # self.account += amount
        # 
        # 
    # 
    # def withdraw(self, amount):
        # """Apply a withdraw method to call later."""
        # if self.withdraw > amount:
            # print(f"We're sorry, {self.name} you do not have sufficient funds.\nYour balance is ${self.amount}.")
        # else: 
            # new_balance = amount - withdraw
            # print("Amount left in your account: AED" + str(new_balance))
            # return (new_balance)        
        #  
        # 
# 
# 
    # def getBalance(self):
        # """return the remaining balance of the Bank Account"""
        # self.getBalance = self.amount
        # return f"{self.name}, your current balance is, ${self.amount}."
# 
# 
# class CheckingAccount(BankAccount):
    # """Create a new Checking Account in the new Bank Account."""
    # def __init__(self, name, fees, minimumbalance):
        # super().__init__(name, balance)
        # self.balance_CheckingAccoung = balance_CheckingAccount
        # self.balance_SavingsAccount = balance_SavingsAccount
        # self.fees = fees
        # self.minimumbalance = minimumbalance
        # accountnumber = accountnumber + "01"
# 
# 
    # def deductFees(self, fees):
        # """subtract 2% from the account"""
        # self.fees = fees
        # self.balance_CheckingAccount = self.balance_CheckingAccount - fees
# 
    # def checkMinimumBalance(self):
        # """Check the balance to make sure it is at least at $50.00, if not notify the user."""
        # self.checkMinimumBalance = 
        # if minimumbalance < float(50):
            # pass
        # else:
            # return f"{self.name}, we're sorry, but you don not have the minimum balance of ${self.minimumbalance}.\nPlease deposit at least ${self.minimumbalance - self.balance} to your Savings Account."
# 
# 
# class SavingsAccountf(BankAccount):
    # """Create a new Savings Account in the new Bank Account."""
# 
    # def __init__(self, name, ):
        # super().__init__(name, balance_CheckingAccount, balance_SavingsAccount, interestrate)
        # self.balance_CheckingAccoung = balance_CheckingAccount
        # self.balance_SavingsAccount = balance_SavingsAccount
        # accountnumber = accountnumber + "02"
        # self.interestrate = interestrate
        # interestrate = interestrate + interestrate * 0.2
        # interestrate = "{:.2%}".format(interestrate)
        # return interestrate
# 
# 
# def options():
    # print("Thank you for creating your Bank account!")
    # print("Here are a list of options, please choose a number for the option you want: ")
    # while True:
        # option_choice = int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) Quit\n"))
        # if option_choice == 1:
            # print(user_one_bank.show_info())
            # 
        # elif option_choice == 2:
            # print(user_one_bank.withdraw())
            # 
        # elif option_choice == 3:
            # print(user_one_bank.deposit())
            # 
        # elif option_choice == 4:
            # print(f"There have been {user_one_bank.total_withdraws} withdraws")
# 
            # break
        # else:
            # print("Please choose a correct number from 1-4")
# 
# 
# 
# 
# 
# accountNumber = "2001009003"
# 
# startingBalance = 200
# 
# 
# 
# 
# 
# 
# 
# 

# name = input("Please enter your name.")
# deposit_CheckingAccount = float(input(f"{name}, please enter the amount you would like to depost to your Checking Account."))
# deposit_SavingsAccount = float(input(f"{name}, please enter the amount you would like to depost to your Savings Account."))
# balance_CheckingAccount = float(200)
# balance_SavingsAccount = float(50)
# minimumbalance = float(50)
# fees = float(2)
# minbalance = float(50)
# interestrate = float(2)
# withdraw = float(input("Please enter how much you would like to withdraw: "))


# return f"Thank you for your business.\nYour new balance for account #{self.accountnumber} is, {self.balance}"
# 
        # withdraw_CheckingAccount + > self.balance_CheckingAccount:
            # return f"We're sorry, {self.name}.\nYour account # {self.accountnumber} is insufficient.\nYour current balance is, ${self.balance}.\nPlease try again."
        # else:    
            # self.balance_CheckingAccount = balance_CheckingAccount - withdraw_CheckingAccount
            # return f"Thank you for your business, {self.name}.\nYour new balance is, ${self.balance}"
        # if withdraw_SavingsAccount > self.balance_SavingsAccount:






##############  First Attempt  ##############

# 
# class User:
    # """Create a new username for the account."""
    # def __init__(self, name):
        # self.name = name
# 
    # def show_details(self):
    #    Return the result of the user's input for their name.
        # return f"{self.name}, thank you for your business!"
    # 
# 
# class BankAccount(User):
    # """Create a new bank account with the user's name"""
    # def __init__(self, name, accountnumber, balance_CheckingAccount, balance_SavingsAccount):
        # super().__init__(name)
    #    assign the balance for both Checking and Savings - Accounts
        # self.balance_CheckingAccount = balance_CheckingAccount
        # self.balance_SavingsAccount = balance_SavingsAccount
    #    assign the account number and the balance to the account
        # self.accountnumber = accountnumber
    # 
    # def deposit(self, deposit_CheckingAccount, deposit_SavingsAccount):
        # """assign deposit values for both checking and savings accounts."""
    #    Ask the user how much they want to deposit and add it to the balance.
        # self.deposit_CheckingAccount = deposit_CheckingAccount + self.balance_CheckingAccount
        # self.deposit_SavingsAccount = deposit_SavingsAccount + self.balance_SavingsAccount
        # 
        # 
        # 
    # 
    # def withdraw(self, withdraw_CheckingAccount, withdraw_SavingsAccount):
        # """Ask the user from which account, and how much they would like to withdraw, and subtract it from the balance."""
    #    convert the string into a floating point number,
        # self.withdraw_CheckingAccount = float(withdraw_CheckingAccount)
        # self.withdraw_SavingsAccount = float(withdraw_SavingsAccount)        
    #    check to see if the withdraw amount for each account is not more than the available balance, of each account.
# 
# 
    # def getBalance(self):
        # """return the remaining balance of the Bank Account"""
        # self.getBalance = self.balance
        # return f"{self.name}, your current balance is, ${self.balance}."
# 
# 
# class CheckingAccount(BankAccount):
    # """Create a new Checking Account in the new Bank Account."""
    # def __init__(self, name, balance_CheckingAccount, balance_SavingsAccount, fees, minimumbalance):
        # super().__init__(name, balance)
        # self.balance_CheckingAccoung = balance_CheckingAccount
        # self.balance_SavingsAccount = balance_SavingsAccount
        # self.fees = fees
        # self.minimumbalance = minimumbalance
        # accountnumber = accountnumber + "01"
# 
# 
    # def deductFees(self, fees):
        # """subtract 2% from the account"""
        # self.fees = fees
        # self.balance_CheckingAccount = self.balance_CheckingAccount - fees
# 
    # def checkMinimumBalance(self, minimumBalance):
        # """Check the balance to make sure it is at least at $50.00, if not notify the user."""
        # 
        # if minimumBalance < float(50):
            # pass
        # else:
            # return f"{self.name}, we're sorry, but you don not have the minimum balance of ${self.minimumbalance}.\nPlease deposit at least ${self.minimumbalance - self.balance} to your Savings Account."
# 
# 
# class SavingsAccountf(BankAccount):
    # """Create a new Savings Account in the new Bank Account."""
# 
    # def __init__(self, name, ):
        # super().__init__(name, balance_CheckingAccount, balance_SavingsAccount, interestrate)
        # self.balance_CheckingAccoung = balance_CheckingAccount
        # self.balance_SavingsAccount = balance_SavingsAccount
        # accountnumber = accountnumber + "02"
        # self.interestrate = interestrate
        # interestrate = interestrate + interestrate * 0.2
        # interestrate = "{:.2%}".format(interestrate)
        # return interestrate
# 
# 
# def options():
    # print("Thank you for creating your Bank account!")
    # print("Here are a list of options, please choose a number for the option you want: ")
    # while True:
        # option_choice = int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) Quit\n"))
        # if option_choice == 1:
            # print(user_one_bank.show_info())
            # 
        # elif option_choice == 2:
            # print(user_one_bank.withdraw())
            # 
        # elif option_choice == 3:
            # print(user_one_bank.deposit())
            # 
        # elif option_choice == 4:
            # print(f"There have been {user_one_bank.total_withdraws} withdraws")
# 
            # break
        # else:
            # print("Please choose a correct number from 1-4")
# 
#name = input("Please enter your name.")
# deposit_CheckingAccount = float(input(f"{name}, please enter the amount you would like to depost to your Checking Account."))
# deposit_SavingsAccount = float(input(f"{name}, please enter the amount you would like to depost to your Savings Account."))
# accountnumber = "2001009003"
# balance_CheckingAccount = float(200)
# balance_SavingsAccount = float(50)
# minimumbalance = float(50)
# fees = float(2)
# minbalance = float(50)
# interestrate = float(2)
# withdraw = float(input("Please enter how much you would like to withdraw: "))
# 
# print("Welcome James Bailey's Bank")
# name = input("Please enter your name: ")
# current_user = User(name)
# 
# 
# 
#return f"Thank you for your business.\nYour new balance for account #{self.accountnumber} is, {self.balance}"

#        withdraw_CheckingAccount + > self.balance_CheckingAccount:
#            return f"We're sorry, {self.name}.\nYour account # {self.accountnumber} is insufficient.\nYour current balance is, ${self.balance}.\nPlease try again."
#        else:    
#            self.balance_CheckingAccount = balance_CheckingAccount - withdraw_CheckingAccount
##            return f"Thank you for your business, {self.name}.\nYour new balance is, ${self.balance}"
#        if withdraw_SavingsAccount > self.balance_SavingsAccount:
# 
# 


#### Example Code 1  https://github.com/Chrisgarlick/Python_Projects/blob/main/My_Projects/Banking_system.py ####

#class User:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#    def show_details(self):
#        return f"Thank you, {self.age} year old, {self.name.title()}"
#
#class Bank(User):
#    total_deposits = 0
#    total_withdraws = 0
#
#    def __init__(self, name, age, balance):
#        super().__init__(name, age)
#        self.balance = balance
#
#    def show_info(self):
#        return f"{self.name} has a remaining balance of: £{self.balance}"
#
#    def deposit(self):
#        dp = float(input("Please enter how much you would like to input: "))
#        print("Thank you for depositing...")
#        self.balance += dp
#        self.total_deposits += 1
#        return f"Your balance is now: £{round(self.balance, 2)}"
#
#    def withdraw(self):
#        wd = float(input("Please enter how much you would like to withdraw: "))
#        print("Thank you for withdrawing...")
#        self.balance -= wd
#        self.total_withdraws += 1
#        return f"Your balance is now: £{round(self.balance, 2)}"
#
#def options(user_two):
#    print("Thank you for creating your Bank account!")
#    print("Here are a list of options, please choose a number for the option you want: ")
#    while True:
#        option_choice = int(input("1) See Balance\n2) Withdraw\n3) Deposit\n4) See Total Withdraws\n5) See Total Deposits\n6) Quit\n"))
#        if option_choice == 1:
#            print(user_one_bank.show_info())
#            if option_choice == 1 and user_two != None:
#                print(user_two_bank.show_info())
#        elif option_choice == 2:
#            print(user_one_bank.withdraw())
#            if option_choice == 2 and user_two != None:
#                print(user_two_bank.withdraw())
#        elif option_choice == 3:
#            print(user_one_bank.deposit())
#            if option_choice == 3 and user_two != None:
#                print(user_two_bank.deposit())
#        elif option_choice == 4:
#            print(f"There have been {user_one_bank.total_withdraws} withdraws")
#            if option_choice == 4 and user_two != None:
#                print(f"There have been {user_two_bank.total_withdraws} withdraws")
#        elif option_choice == 5:
#            print(f"There have been {user_one_bank.total_deposits} deposits")
#            if option_choice == 5 and user_two != None:
#                print(f"There have been {user_two_bank.total_deposits} deposits")
#        elif option_choice == 6:
#            print("Thank you for using your bank. Please come again soon.")
#            return False
#            break
#        else:
#            print("Please choose a correct number from 1-7")
#
#def bank_creation():
#    balance = float(input("how much money do you have: "))
#    return balance
#    
#
#while True:
#    print("Welcome to the BC Bank")
#    name = input("Please enter your name: ")
#    age = int(input("Please enter your age: "))
#    user_one = User(name, age)
#    user_two = None
#    new_user = input("Would you like to register a new person? Type 'No' to create your bank: ")
#    if new_user.lower() == 'yes':
#        name = input("Please enter your name: ")
#        age = int(input("Please enter your age: "))
#        user_two = User(name, age)
#        print("Thank you for registering 2 people. Please create your bank accounts.")
#        user_one_balance = bank_creation()
#        user_two_balance = bank_creation()
#        user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
#        user_two_bank = Bank(user_two.name, user_two.age, user_two_balance)
#        flag = options(user_two)
#        if flag == False:
#            break
#    else:
#        user_one_balance = bank_creation()
#        user_one_bank = Bank(user_one.name, user_one.age, user_one_balance)
#        flag = options(user_two)
#        if flag == False:
#            break

#### Example Code 2  https://www.codespeedy.com/python-program-to-create-bank-account-class/     ####

#class Bank_Account:
#    def __init__(self):
#        self.balance=0
#        print("Welcome to Deposit & Withdrawal Machine!")
#        
#    def deposit(self):
#        amount=float(input("Enter amount to be deposited: "))
#        self.balance += amount
#        print("Amount Deposited: ",amount)
#    def withdraw(self):
#        amount = float(input("Enter amount to withdraw: "))
#        if self.balance>=amount:
#            self.balance-=amount
#            print("You withdraw: ",amount)
#        else:
#            print("Insufficient balance ")
#    def display(self):
#        print("Net Available Balance=",self.balance)
##creating an object of class
#s = Bank_Account()
#
##calling functions with that class
#s.deposit()
#s.withdraw()
#s.display()


#### Example Code 3  https://coderzway.com/bank-account-program-in-python/ ####

#is_logined = False
#is_quit = False
#
#user = {
#    'name': '',
#    'balance': 0
#}
#
#def create_user():
#    name = input('Enter your name: ')
#    user['name'] = name
#    global is_logined
#    is_logined = True
#
#def withdraw_money():
#    try:
#        w_amount = int(input('How much money you want to withdraw : '))
#        if w_amount > user['balance']:
#            print('Your account does not have that much money')
#        elif w_amount == 0:
#            print('What you are fooling around here')
#        else:
#            user['balance'] = user['balance'] - w_amount
#            print(f'{w_amount} has been withrawn from your account your total balance left is {user["balance"]}')
#            print('')
#    except:
#        print('Please enter a number')
#
#def deposit_money():
#    try:
#        d_amount = int(input('How much money you want to deposit : '))
#        user['balance'] = user['balance'] + d_amount
#        print(f'{d_amount} has been deposited to your account your total balance is {user["balance"]}')
#        print('')
#    except:
#        print('Please enter a number')
#
#def show_balance():
#    print(f'Your balance is {user["balance"]}')
#    print('')
#
#def start():
#    while is_quit == False:
#        if is_logined == False:
#            print('Create your account : ')
#            create_user()
#        else :
#            print(f'Welcome to bank {user["name"]} what you want to do ')
#            res = input('Press w for withdraw and d to deposit and b to show your balance and q to Quit: ')
#            if res == 'w':
#                withdraw_money()
#            elif res == 'd':
#                deposit_money()
#            elif res == 'b':
#                show_balance()
#            elif res == 'help':
#                print('Press w for withdrawing money')
#                print('Press d for depositing money')
#                print('Press b for showing your balance')
#                print('Press q for showing quiting the program')
#            elif res == 'q':
#                break
#            else:
#                print('Enter a correct value from given type help for commands')
#        
#start()




 
#### CSD-205_Module9 Bank.py assingment by James Bailey ####

#####################       First Attempt       #####################

#class BankAccount:
    #""" Superclass holding main functions for BankAccounts """
#    def __init__(self, accountNumber, balance):
        #""" Initiate accountNumber and balance attributes """
        #self.accountNumber = accountNumber
        #self.balance = balance

 #   def withdrawl(self):
       # """ set how much is removed from the bankAccount, 
        #    show how much has been removed.
        #"""
#        withdrawl = self.withdrawl
#        return int(withdrawl)
#    print(f"{self.withdrawl} has been removed from your account.")

#    def deposit(self):
        #""" set how much is added to the bankAccount,
         #   show how much has been added.
        #"""
#        deposit = self.deposit
#        return int(deposit)
#    print(f"{deposit} has been added to your account #{self.accountNumber}")


#class CheckingAccount(BankAccount):
    #""" Subclass CheckingAccount using the Superclass BankAccount's attributes and functions. """
    #def __init__(self, fees, minimumBalance):
        #self.balance -= fees
        #self.minimumBalance = minimumBalance

    #def deductFees(self):
        #""" reduce CheckingAccount balance by the ammount, fees. """
        #self.balance -= fees



#class SavingsAccount(BankAccount):
    #""" Subclass SavingsAccount using the Superclass BankAccount's attributes and function. """
    #def __init__(self,interestRate):
        #""" Set the interestRate """
        #self.balance = interestRate


#my_account = BankAccount(1234567890, 200)
#my_account2 = BankAccount(1234567890, 25)



#####################       Second Attempt       #####################

### Works Cited: https://www.geeksforgeeks.org/python-program-to-create-bankaccount-class-with-deposit-withdraw-function/       ###
# Python program to create Bankaccount class
# with both a deposit() and a withdraw() function
#from typing_extensions import Self


#class Bank_Account:
#    def __init__(self):
#        """ Set original balance. """
        # self.balance=int(200)
        # print("Hello!!! Welcome to the Deposit & Withdrawal Machine")
 
    # def deposit(self):
        # """ Set a user input to determine how much to add to the Bank Account. """
        # amount=float(input("Enter amount to be Deposited: "))
        # self.balance += amount
        # print("\n Amount Deposited:",amount)
 
    # def withdrawl(self):
        # amount = float(input("Enter amount to be Withdrawn: "))
        # if self.balance>=amount:
            # self.balance-=amount
            # print("\n You Withdrew:", amount)
        # else:
            # print("\n Insufficient balance  ")
 
    # def get_Balance(self):
        # print("\n Net Available Balance=",self.balance)

# class CheckingAccount(Self):
    # """ Represent Bank_Account to CheckingAccount. """

    # def __init__(self):
        #  """ Initiate the attributes and functions of the superclass Bank_Account. """
        #  super().__init__(self)

    # def duductFees(self):
        # """ Create a $5 fee. """
        # fee = float(5)
        # if self.balance >= int(0):
            # self.balance -= fee
        # else:
            # print("\nYou have incificient funds. Try again later. ")

    # def minimumBalance(self):
        # """ Create a minimum balance to keep the CheckingAcount open. """
    # minimum = float(50)

        
    # def Check_Minimum_Balance(self):
        # if self.balance >= int(50):
            # return self.balance
        # else:
            # print("\n Incenficient balance")

# class SavingsAccount(Bank_Account):
    # """ Represent Bank_Account to SavingsAccount. """
    # def __init__(self):
        # """ Initiate the attributes and functions of the superclass Bank_Account. """
        # super().__init__(self)

    # def addInterest(self):
        # """ 
        # Increment interest to the SavingsAccount.
        # Percentage formula provided by https://qa-faq.com/en/Q%26A/page=879ecf63c10f82a124df6fdfc23cba94
        # """
        # if self.balance >= int(0):
            # self.balance *= float(1.02)
        # else:
            # print("Incifient Funds!")

    
 
# Driver code
  
# creating an object of class
# s = Bank_Account()
  
# Calling functions with that class object
# s.deposit()
# s.withdrawl()
# s.get_Balance()
