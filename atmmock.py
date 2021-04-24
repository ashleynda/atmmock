from pdb import pm

import day as day
#initializing the system
import random
database = {}


def init() :
    print ( "Welcome to Ash bank" )
    haveAccount = int ( input ( "Do you have an account with us: 1. (Yes) 2. (No) \n" ) )
    if haveAccount == 1:
        login ()
    elif haveAccount == 2:
        register()


name = input ( "what is your name? \n" )
allowedUsers = ['Ashley', 'Mike', 'Love']
allowedRequirements = ['email and password']
allowedPassword = ['passwordAshley', 'passwordMike', 'passwordLove']


def login():
    print ( "this is the login function" )


if (name in allowedUsers) :
    password = input ("Your password? \n")
    date = input ("2021-04-24")
    time = input ("11:36pm")

def register():
    print("Register")
    email = input("What is your email address?\n")
    first_name = input("What is your first_name?\n")
    last_name = input("What is your last name?\n")
    password = input("create a password?\n")

    accountnumber = generateAccountNumber

    database[accountNumber] = [ first_name, last_name, email, password]

    print("Account has been created")
    login()


    userId = allowedUsers.index ( name )
    if password == allowedPassword[userId] :
        print ('Welcome %s' % name)
        print ('available options')
        print ('1.Withdraw')
        print ('2. Cash Deposit')
        print ('3.Recharge')
        print ('4.Check balance')
        print ('5.Complaint')
        print ('6. logout')

        selectedOption = int ( input ( 'Please select an option' ) )

        print ( selectedOption )

        if selectedOption == 1 :
            print ( 'you selected %s' % selectedOption )
            print ( 'How much would you like to withdraw?' )
            print ( 'Take your cash' )

        elif selectedOption == 2 :
            print ( 'you selected %s' % selectedOption )
            print ( 'How much would you like to deposit?' )
            print ( 'Current balance.' )

        elif selectedOption == 3 :
            print ( 'you selected %s % selectedOption' )
            print ( 'Which Network?' )
            print = int ( input ( 'phone number' ) )
            print ( 'Amount' )
            print ( 'Successful' )

        elif selectedOption == 4 :
            print ( 'you selected %s % selectedOption' )


        elif selectedOption == 5 :
            print ( 'you selected %s % selectedOption' )
            print ( 'What issue will you like to report?' )

        elif selectedOption == 6:
            print('do you want to perform another transaction')
            print('please select an option 1. yes, 2. no, \n')
            print('logout')

        else :
            print ( 'Invalid Option selected, please try again' )


    else :
        print ( 'Password Incorrect, please try again' )
    else :
        print ( 'Name not found, please try again' )


  def generateAccountNumber():
    return random.randrange[0000000000, 1111111111]

    print(generateAccountNumber())
     init()
