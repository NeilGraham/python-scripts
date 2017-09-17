list = []

def main():
    print()
    print("This program will record items into a list and then print it")

    print()
    print("[Type BACK to undo the previous action]")
    print("[When you are finished, type DONE]")

    # Set a title for the list
    print()
    print("Enter a title for the list")
    print("[You'll be able to change the title at any time by typing in TITLE]")
    title = query_user()
    if title.strip() != "":
        print("     The title has been set to \"" + title + "\"")
    else:
        print("     The list has no title")
        print("     You can add a title at any point while adding items")

    # Add items to the list
    print()
    print("You can now start adding items into the list:")
    answer = ""
    while answer.upper() != "DONE":
        if answer.upper() == "BACK":
            if len(list) == 0:
                title = set_title(title)
            else:
                remove_last_item()
        elif answer.upper() == "TITLE":
            title = set_title(title)
        elif answer != "":
            add_item(answer)
        print()
        answer = query_user()

    #Once the list has been completed, print list
    print_list(title, list)

def add_item(item):
    list.append(item)
    print("     " + item + " has been ADDED to the list")

def remove_last_item():
    print("     " + list[len(list) - 1] + " has been REMOVED from the list")
    del list[len(list) - 1]

def query_user():
    return input(" + ").strip()

def set_title(title):
    print()
    if title != "":
        print("What would you like to change the title to?")
    else:
        print("What would you like the title to be?")
    title = query_user()
    print("     The title has been changed to " + title)

    print()
    print("You can continue adding items to the list")
    return title

def print_list(title, list):
    print()
    if len(list) == 0:
        print("Your list is empty!")
        print()
        return None

    # If the list has a title, include tabs when printing
    #  the items in the list
    tab = False
    if title.strip() != "":
        print("  " + title + ":")
        tab = True
    for item in list:
        if tab:
            print("  ", end="")
        print("  " + item)
    print()

#Call the main function
main()
