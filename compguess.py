import random

def main():
    print()
    print()
    print('Think of a number between 1 and 100')
    print('I\'ll try to guess it within 7 tries')
    print('If my guess is wrong, tell me if your')
    print(' number is above or below my guess')
    print()
    print()
    print('  Shall we start?', end='')
    if biquery('Y', 'n') == 'y':
        start_game()
    else:
        end_game()

def start_game():
    print()
    lower = 1
    upper = 100
    tries = 7
    while True:
        print()
        if tries == 0:
            comp_lose()
        comp_guess = round(((upper - lower) / 2) + lower)
        tries -= 1
        print('Is your number {}?'.format(str(comp_guess)), end='')
        if biquery('y','N') == 'n':
            print('  Is your number above or below {}?'.format(comp_guess), end='')
            if biquery('a','b') == 'a':
                lower = comp_guess + 1
            else:
                upper = comp_guess - 1
        else:
            comp_win(tries)


def comp_win(tries):
    print()
    print()
    print('  I found your number in {} tr'.format(7-tries), end='')
    if tries == 6:
        print('y!')
    else:
        print('ies')
    print()
    print()
    exit()


def comp_lose():
    print()
    r = random.randint(1,3)
    if r == 1:
        print('You\'re lying to me!')
    elif r == 2:
        print('You must\'ve changed your number!')
    elif r == 3:
        print('  Are you sure about that?')
    print()
    print()
    exit()

def end_game():
    print('    Would you like to close the program?', end='')
    if biquery('Y','n') == 'y':
        print()
        print()
        exit()
    else:
        print('Alright, let\'s start the game then')
        start_game()

def biquery(c1, c2):

    print(' ({}/{}) '.format(c1, c2), end='')

    cap_c = 0
    if c1 == c1.upper():
        cap_c = 1
    elif c2 == c2.upper():
        cap_c = 2

    i = input().strip().lower()

    while True:
        if i == c1.lower() or i == c2.lower():
            break
        if cap_c > 0:
            if i == '':
                break
        print("    Type in the letter '{}' or '{}'. ({}/{}) ".format(c1.lower(), c2.lower(), c1, c2), end='')
        i = input().strip().lower()
    if cap_c == 1:
        if i == c1.lower() or i == '':
            return c1.lower()
        else:
            return c2
    elif cap_c == 2:
        if i == c2.lower() or i == '':
            return c2.lower()
        else:
            return c1
    else:
        if i == c1:
            return c1
        else:
            return c2

main()
