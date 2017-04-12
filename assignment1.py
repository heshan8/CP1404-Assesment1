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
        reading_list.sort()
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
    with open("books.csv", "w", newline='') as c:
        edit = csv.writer(c)
        edit.writerows(reading_list)
    if menu_choice == "Q":
        print("Have a nice day :)")
        exit


def show_list(reading_list, books):
    if books == "r":
        print("List of required books:")
    elif books == "c":
        print("List of completed books")
    elif books == "m":
        books = "r"
    count = 0
    total = 0
    for item in reading_list:
        if books in item[3]:
            print("{}. {:20}   $ {:10} ({})".format(count, item[0], item[1], item[2], item[3]))
            count += 1
            total += float(item[1])

    if count == 0:
        if books == "r":
            print("No required books to display")
        elif books == "c":
            print("No completed items to display")
        else:
            print("No items exist in the list")
    else:
        print("Total expected price for {} items: ${}".format(count, total))




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
#done




