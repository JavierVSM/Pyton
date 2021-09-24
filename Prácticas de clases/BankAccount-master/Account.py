class Account:
    bankName = "Coding Dojo Bank"
    allBankAccounts = []

    def __init__( self, accountNum, user ):
        self.accountNum = accountNum
        self.user = user # Holding a User object
        self.balance = 0.0
        Account.allBankAccounts.append( self )

    def withdraw( self, amount ):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print( "We cannot process your withdrawal." )
            print( f"You currently have {self.balance}." )
            print( f"And you are trying to withdraw {amount}." )
        return self

    def deposit( self, amount ):
        self.balance += amount
        return self

    def printInfo( self ):
        self.user.printUserInfo() # Calling the printInfo in the User object
        print( f"Account number: {self.accountNum}." )
        print( f"Account balance: {self.balance}." )
        return self

    @classmethod
    def changeBankName( cls, newName ):
        cls.bankName = newName
    
    @classmethod
    def printAllAccountsInfo( cls ):
        for account in cls.allBankAccounts:
            print( account.bankName )
            account.printInfo()

    @staticmethod
    def doesAccountHasMoreThan1000( account ):
        if( account.balance >= 1000 ):
            return True
        else:
            return False

    def validateFunds(self, amount):
        if self.balance > amount:
            return True
        else:
            return False

    def transfer( self, externalAccount, amountToTransfer ):
        if self.validateFunds( amountToTransfer ):
            self.withdraw( amountToTransfer )
            externalAccount.deposit( amountToTransfer )
        else:
            print( "You don't have enough funds to transfer." )