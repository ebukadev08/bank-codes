import math
cb = 0
print("welcome to the online banking application")

def signin():
    global name # username
    global pin # password
    global cb # cureent balance
    cb = 0
    name = str(input("please create your username: "))
    pin = str(input("please create your 6 digit pin: "))
    if len(pin) == 6:
        pin = pin
    else:
        print("The pin has to be in 6 digits")
        newpin = str(input("please create your 6 digit pin: "))
        if len(newpin) != 6:
            print("The pin has to be in 6 digits")
            signin()
        else:
            pin = newpin
    print("Thanks for creating your bank account")
    exist()
            

def forgetpin(): 
    global pin
    recoverypin = str(input("please create your 6 digit pin: "))
    if len(recoverypin) != 6:
        print("The pin has to be in 6 digits")
        forgetpin()
    else:
        print("The new pin has been stored, please log in")
        pin = recoverypin
        login()

def depositinterest(p,r,t):
    # A = pe^(rt) whsich is the formula to calculate the compound

    p = float(p)
    r = float(r)
    t = float(t)
    rt = r * t
    e = math.exp(rt)
    # calculation
    a = p * e # future value of your investment
    return a

def login():
    global name, pin, cb
    # name1 represent username
    # pin1 represent password
    name1 = str(input("please enter your username: "))
    pin1 = str(input("please enter your pin: "))
    if name1 == name and pin1 == pin:
        print("welcome to the online banking application"+ " " + name)
        print("please choose the menu d own here")
        listmenu = ["1-Deposit","2-Withdraw","3-Tranfer","4-Check Balance","5-Deposit interest rate","6-Calculate comnpound interest", "7-Exist"]
        for b in listmenu:
            print(b)
        choose = int(input("please the number of your choice: "))
        
        if choose == 1:
            d = int(input("Enter the amount of your deposit: "))
            cb += d
            print("Your current balance is"+" "+ str(cb))
        elif choose == 2:
            w = int(input("Enter the amount of money you want to enter: "))
            if w > cb:
                print("your current balance is not sufficient for this transaction")
                login()
            else:
                cb -= w
            print(f"{w} has been withdrawn from your account, your current balance {cb}")
        elif choose == 3:
            dest = input("please enter the acconut number of your destination in 8 digits: ")
            if len(dest) == 8 and dest.isdigit():
                amount = int(input("please enter the amount of money you want to tranfer: "))
                if amount > cb:
                    print("your current balance is not sufficient for this transaction")
                    login()
                else:
                    cb -= amount
                    print(f"{amount} was transfered to {dest}, Your current balance is {cb}")
            else:
                print("The transaction has been rejected since the account is invalid")
                login()
        elif choose == 4:
            print("Your account balance is"+ str(cb))
        elif choose == 5:
            if cb > 50000:
                rate = 3
            elif cb > 30000:
                rate = 2
            else:
                rate = 1.5
                print(f"Your deposit interest rate"+ {rate} + "%")
        elif choose == 6:
            listOption = ["1-calculate your deposit compound interest based on your Current balance", "2-Calculate your deposit compound interest based on your deposit input"]
            for n in listOption:
                print(n)
            choose = int(input("please enter your choice from the option above: "))
            if choose == 1:
                timing = float(input("How many year do you want to invest your money?: "))
                if cb > 50000:
                    ratex = 3/100
                elif cb > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print(f"Your current balance in {timing} years will be: ")
                print(depositinterest(cb,ratex,timing))
            elif choose == 2:
                timming1 = float(input("How many year do you want to invest your money?: "))
                money = float(input("Please enter the amount of money you would like to deposit: "))
                if money > 50000:
                    ratex = 3/100
                if money > 30000:
                    ratex = 2/100
                else:
                    ratex = 1.5/100
                print("Your current balance in"+ " " + "timming"+ " " + "year will be")
                print(depositinterest(money,ratex,timming1))
        elif choose == 7:
            exist()
        else:
            print("Option is not available")
            login()
    else:
        print("Either of your username or password is wrong, did you create your account.")
        list1 = ["1-yes", "2-no"]
        for i in list1:
            print(i)
        inp = int(input("Enter your choice: "))
        if inp == 1:
            list2 = ["1-do you want to attempt to login agin?", "2-you forget your pin: "]
            for e in list2:
                print(e)
            thenanswer = str(input("Enter your choice: "))
            thenanswer = int(thenanswer)
            if thenanswer == 1:
                login()

            elif thenanswer == 2:
                forgetpin()
            else:
                print("option is not available")
                login()
        elif inp == 2:
            print("please create your account")
            signin()
    exist()

def mainmenu():
    print( "1. Sign In\n2. Log In")
    optionone = int(input("Choose an option: "))
    if optionone == 1:
        signin()
    if optionone == 2:
        login()
    else:
        print("Option not available")
        mainmenu()
    exist()

def exist():
    answer = str(input("do you still want to conduct transaction?, Yes or No: " )).lower()
    if answer == "yes":
        login()
    elif answer == "no":
        print("Thank you for using this app")

    else:
        print("Option not available")
    mainmenu()

mainmenu()