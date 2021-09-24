from Account import Account
from User import User

print( "***** Bank Account MENU *****\n1) Add an account\n2) Deposit to an account\n3) Withdraw from an account" )
print( "4) See the information of all accounts")
option = input( "Select an option: " )

while( option == "1" or option == "2" or option == "3" or option == "4" ):
    if( option == "1" ):
        firstName = input( "Please give me your first name: ")
        lastName = input( "Please give me your last name: ")
        age = input( "Please give me your age: ")
        newUser = User( firstName, lastName, int(age) )
        accountNo = input( "Type you account No: ")
        newAccount = Account( int(accountNo), newUser )
    if( option == "4" ):
        Account.printAllAccountsInfo()
    print( "***** Bank Account MENU *****\n1) Add an account\n2) Deposit to an account\n3) Withdraw from an account" )
    print( "4) See the information of all accounts")
    option = input( "Select an option: " )    

print( "End of the program" )
#michaelUser = User( "Michael", "Miller", 30 )
#alvaroUser = User( "Alvaro", "Sanchez", 35 )

#michaelAccount = Account( 12345, michaelUser )
#alvaroAccount = Account( 22222, alvaroUser )

#michaelAccount.deposit( 10000.0 )
#alvaroAccount.deposit( 1000.0 )

#michaelAccount.transfer( alvaroAccount, 2000.0 )

#Account.printAllAccountsInfo()


#michaelAccount.withdraw( 100.0 )
#michaelAccount.deposit( 1000.0 )
#michaelAccount.printInfo()
#michaelAccount.withdraw( 500.0 )
#michaelAccount.printInfo()

#michaelAccount.withdraw( 100.0 ).deposit( 1000.0 ).printInfo()
#michaelAccount.withdraw( 500.0 ).printInfo()

#Account.changeBankName( "The Coding Dojo Bank" );
#print( Account.allBankAccounts )

#Account.printAllAccountsInfo()

#result = Account.doesAccountHasMoreThan1000( michaelAccount )
#print( result )