"""
Replace the contents of this module docstring with your own details
"""
import csv

def main():
    print("Reading List 1.0 - by <Tharindu Heshan>")
    print()
    choice = True
    main_menu()
    choice = str(input())
    menu_choice = str(input())
    if menu_choice.lower() == 'r':
        print("Required Books:")
        required_items()
    elif menu_choice.lower() == 'c':
        print("Completed Items:")
        list_items_completed()
    elif menu_choice.lower() == 'm':
        list_items_required()
        mark_item_completed()
    elif menu_choice.lower() == 'a':
        add_item()
    elif menu_choice.lower() == 'q':
        loop = False
    else:
        input("Input Error! Enter any key to try again.")


print("Program exiting")

def required_items():


 def main_menu():
    print('Menu:')
    print('R - List required books')
    print('C - List completed books')
    print('A - Add new book')
    print('M - Mark a book as completed')
    print('Q - Quit')
    choice = str(input('Pick a choice from above: '))
main()

