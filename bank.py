bank = ['TD Bank','TD Bank']
kind = ['Checking', 'Saving']
balance = [0, 0]

accounts = [bank, kind, balance]



def home(i):
    if i == -1:
        print("Welcome to Universal Bank")
        print("The go-to place for all banking\n")
    print("Choose one of the options below")
    print("1. Balance")
    print("2. Withdrawel")
    print("3. Deposit")

    choice = input("\n-- ")
    if is_number(choice):
        choice = int(choice)

    if choice >= 1 and choice <= 3:
        if choice == 1:
            balance(-1)
        if choice == 2:
            withdrawel(-1)
        if choice == 3:
            deposit(-1)
    else:
        print("Sorry, but that is not an available option")
        print("Lets try that again\n")
        home(0)
        

def select_account(i):
    if i == -1:
        print("\nSelect an account")
    
    for x in range(0, len(accounts[0])):
        print(str(x+1) + ". " + accounts[0][x] + ", " + accounts[1][x])
        
    choice = input("\n-- ")
    
    if is_number(choice):
        choice = int(choice)
    else:
        print("What you entered seems to not be a number")
        print("Let's try that again\n")
        return select_account(0)
        
    if (choice >= 1 and choice <= (len(accounts[0]) + 1)):
        return choice - 1
    else:
        print("Sorry, that number does not correspond to one of your accounts")
        print("Let's try that again\n")
        return select_account(0)




def is_number(string):
    decimalPoint = 0
    for x in range(0, len(string)):
        if not((string[x] >= '0' and string[x] <= '9') or string[x] == '.'):
            return False
        if string[x] == '.':
            decimalPoint += 1
    if decimalPoint > 1:
        return False
    return True




def balance(i):
    if i == -1:
        i = select_account(-1)
        if i == -1:
            withdrawel(-1)
        
    print("\n$%.2f\n" % round(accounts[2][i],2))
    
    home(0)




def withdrawel(i):
    if i == -1:
        i = select_account(-1)
        if i == -1:
            withdrawel(-1)
        
    amount = input("\nHow much would you like to withdrawel? \n\n-- $")
    if is_number(amount):
        amount = float(amount)
        if (accounts[2][i]-amount) >= 0:
            accounts[2][i] = accounts[2][i] - amount
            print("\nYour withdrawel of $%.2f was successful!\n" % round(amount,2))
        else:
            print("\nSorry, but you don't have $%.2f in this account\n" % round(amount,2))
    else:
        print("\nThe amount that you entered seems to not be a number")
        print("Let's try that again\n")
        withdrawel(i)
    
    home(0)




def deposit(i):
    if i == -1:
        i = select_account(-1)
        if i == -1:
            deposit(-1)
        
    amount = input("\nHow much would you like to deposit? \n\n-- $")
    if is_number(amount):
        amount = float(amount)
        accounts[2][i] = accounts[2][i] + amount
        print("\nYour deposit of $%.2f was successful!\n" % round(amount,2))
    else:
        print("\nThe amount that you entered seems to not be a number")
        print("Let's try that again\n")
        withdrawel(i)

    home(0)



home(-1)
