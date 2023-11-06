class BankAcct(object):
    def __init__(self, *arg): # aNum, bal
        if len(arg)==0:
            self.acctNum = ""
            self.balance = 0
        elif len(arg)==1:
            self.acctNum = arg[0]
            self.balance = 0
        else:
            self.acctNum = arg[0]
            self.balance = arg[1]

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False

    def deposit(self, amount):
        if (amount <= 0):
            return "Can't deposit non-positive amount"
        self.balance += amount
        return 

    def print(self):
        print("Account Number:", self.acctNum)
        print("Balance:", self.balance)

def transfer(fromAcct, toAcct, amount):
    if fromAcct.withdraw(amount):
        toAcct.deposit(amount)
    else:
        print("Money not enough")

ba1 = BankAcct()
ba2 = BankAcct(1234, 99.99)

ba1.deposit( 1000 );
ba2.withdraw( 50.25 );     
    
transfer( ba1, ba2, 50.0);
print("printing ba1");
ba1.print();
    
print("printing ba2");
ba2.print();

transfer( ba2, ba1, 100)
print("printing ba1");
ba1.print();
    
print("printing ba2");
ba2.print();
    
