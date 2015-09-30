#!/usr/bin/env python



# Import the modules needed to run the script.
import sys, os

# Main definition - constants
menu_actions  = {}

# =======================
#     MENUS FUNCTIONS
# =======================
# Main menu
def main_menu():
    os.system('clear')

    print "Welcome,\n"
    print "Please choose the menu you want to start:"
    print "1. Catalog Items"
    print "2. Service Requests"
    print "3. Infrastructure"
    print "4. Consuption"
    print "\nq. Quit"
    choice = raw_input(" >>  ")
    exec_menu(choice)

    return

# Execute menu
def exec_menu(choice):
    os.system('clear')
    ch = choice.lower()
    if ch == '':
        menu_actions['main_menu']()
    else:
        try:
            menu_actions[ch]()
        except KeyError:
            print "Invalid selection, please try again.\n"
            menu_actions['main_menu']()
    return

# Catalog Menu
def catalog():
    print "Catalog Menu!\n"
    print "b. Back"
    print "q. Quit"
    choice = raw_input(" Catalog >>  ")
    exec_menu(choice)
    return


# Service Request Menu
def requests():
    print "Requests Menu!\n"
    print "b. Back"
    print "q. Quit"
    choice = raw_input(" Requests >>  ")
    exec_menu(choice)
    return

def infrastructure():
    print "Infrastructure Menu!\n"
    print "b. Back"
    print "q. Quit"
    choice = raw_input(" Infrastructure >>  ")
    exec_menu(choice)
    return

def consumption():
    print "Consuption Menu!\n"
    print "b. Back"
    print "q. Quit"
    choice = raw_input(" Consumption >>  ")
    exec_menu(choice)
    return

# Back to main menu
def back():
    menu_actions['main_menu']()

# Exit program
def exit():
    sys.exit()

# =======================
#    MENUS DEFINITIONS
# =======================

# Menu definition
menu_actions = {
    'main_menu': main_menu,
    '1': catalog,
    '2': requests,
    'b': back,
    'q': exit,
}

# =======================
#      MAIN PROGRAM
# =======================

# Main Program
if __name__ == "__main__":
    # Launch main menu
    main_menu()
