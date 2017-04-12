"""
CP1404 Assignment -1-
Reading list by Tharindu Heshan
Add github link
"""
MAIN_MENU = "\nMain menu:\n R - Show list of required books\n C - Show list of completed books\n" \
            " A - Add a new book\n M - Mark a book as completed\n Q - Quit"

import csv

def main():
    with open('books.csv', 'r') as c:
        edit = csv.reader(c)
        reading_list = list(edit)
    print("Reading List 1.0 - by Tharindu Heshan")
    print(MAIN_MENU)
    menu_choice = input("Enter choice: ").upper()
    while menu_choice != "Q":
        if menu_choice == "R":
            print("N")
        elif menu_choice == "C":
            print("p")
        elif menu_choice == "A":
            print("p")
        elif menu_choice == "M":
            print("p")
        else:
            print("Invalid input, Try again.")
        print(MAIN_MENU)
        menu_choice = input("Enter choice: ").upper()
    with open("books.csv", "a", newline='') as c:
        edit = csv.writer(c)
        edit.writerows(reading_list)
    print("Have a nice day :)")




main()
#     choice = True
#     (main_menu)
#     choice = str(input())
#     menu_choice = str(input())
#     if menu_choice.lower() == 'r':
#         print("Required Books:")
#         required_items()
#     elif menu_choice.lower() == 'c':
#         print("Completed Items:")
#         list_items_completed()
#     elif menu_choice.lower() == 'm':
#         list_items_required()
#         mark_item_completed()
#     elif menu_choice.lower() == 'a':
#         add_item()
#     elif menu_choice.lower() == 'q':
#         loop = False
#     else:
#         input("Input Error! Enter any key to try again.")
#
#
# print("Program exiting")
#
# def required_items():





