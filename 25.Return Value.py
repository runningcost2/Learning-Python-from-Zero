def open_account():
    print("A new account has been created")

def deposit(balance, money):
    print("Your deposit has been completed. Account balance : {0}".format(balance + money))
    return balance + money

def withdraw(balance, money):
    if balance >= money:
        print("Your withdraw has been completed. Account balance : {0}".format(balance - money))
        return balance - money
    else:
        print("Your withdraw has not been completed. Please check your account balance. Account balance : {0}".format(balance))
        return balance

def withdrawal_fee(balance, money):
    commission = 2
    return commission, balance - money - commission





balance = 0
balance = deposit(balance, 1000)
# # balance = withdraw(balance, 2000)
# balance = withdraw(balance, 500) 
commission, balance = withdrawal_fee(balance, 500)

print("The withdrawal fee is {0} dollar. Account balance : {1}".format(commission, balance))