"""
CP1404 Assignment -1-
Reading list by Tharindu Heshan
Add github link
"""
main_menu = "\nMain Menu:\n R - Show list of required books\n C - Show list of completed books\n" \
            " A - Add a new book\n M - Mark a book as completed\n Q - Quit"

import csv

def main():
    with open('books.csv', 'r') as f:
        edit = csv.reader(f)
        reading_list = list(edit)
        reading_list.sort()
    print("Reading List 1.0 - by Tharindu Heshan")
    print(main_menu)

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





