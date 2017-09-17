import random


def main():
    number = random.randint(1,10)

    print()
    print()
    print("    You'll be given 5 tries to guess")
    print("      a random number from 1 to 10  ")
    print()
    print()

    print("You can start guessing")
    guess = 0
    tried = []
    while True:
        try:
            guess = int(input(" + "))
        except ValueError:
            print("That's not a number!")
            print()
        else:

            if guess > 10 or guess < 1:
                print("Number must be between 1 and 10")
                print()
                print("You still have " + str(5 - len(tried)) + " more tr", end="")
                if len(tried) < 4:
                    print("ies")
                else:
                    print("y")
                continue

            already_guessed = False
            for num in tried:
                if guess == num:
                    print(str(num) + " was already guessed")
                    print()
                    already_guessed = True
                    continue
            if already_guessed:
                print("You still have " + str(5 - len(tried)) + " more tr", end="")
                if len(tried) < 4:
                    print("ies")
                else:
                    print("y")
                continue

            tried.append(guess)
            if guess == number:
                break
            elif len(tried) == 5:
                print()
                print("You are out of guesses")
                print("The number was " + str(number))
                print()
                exit()
            else:
                print(str(guess) + " is ", end="")
                if guess < number:
                    print("less", end="")
                else:
                    print("greater", end="")
                print(" than the random number")
                print()

                print("You have ", end="")
                if len(tried) < 4:
                    print("another " + str(5 - len(tried)) + " more guesses")
                else:
                    print("1 more try")

    print()
    print()
    print("Correct! The number was " + str(number) + ", it took you " + str(len(tried)) + " tr", end="")
    if len(tried) == 1:
        print("y", end="")
    else:
        print("ies", end="")
    print(" to find the random number")
    print()
    print()

main()
