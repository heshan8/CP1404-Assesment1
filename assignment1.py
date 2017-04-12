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
            show_list(reading_list, menu_choice.lower())
        elif menu_choice == "C":
            print("p")
        elif menu_choice == "A":
            print(add_book(reading_list, menu_choice.lower))
        elif menu_choice == "M":
            show_list(reading_list, menu_choice.lower())
            mark_book(reading_list)
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


def show_list(reading_list, book):
    if book == "r":
        print("List of required books:")
    elif book == "c":
        print("List of completed books")
    elif book == "m":
        book = "r"
    count = 0
    total = 0
    for items in reading_list:
        if book in items[3]:
            print("{}. {:34} By: {:13}  Pages:({})".format(count, items[0], items[1], items[2], items[3]))
            count += 1
            total += int(items[2])

    if count == 0:
        if items == "r":
            print("No required books to display")
        elif items == "c":
            print("No completed items to display")
        else:
            print("No items exist in the list")
    else:
        print("Total pages for {} books: {}".format(count, total))

def mark_book(reading_list):
    valid_booknumber = False
    while not valid_booknumber:
        book_number = int(input("Enter the valid number of the book to mark as completed: "))
        count = -1
        for book in reading_list:
            if book[3] == "r":
                count += 1
                if count == book_number:
                    book[3] = "c"
                    print(book[0], "is marked as completed" )
                    valid_booknumber = True
                    break
            elif count == book_number:
                print("Warning, the book was not marked")
                valid_booknumber = True
                break
        if not valid_booknumber:
            print("Invalid book number, try again")

def add_book(reading_list):
    book_list = []
    book_name = str(input("Enter the name of the book you want to add: "))
    while not book_name.isalnum():
        print("Cannot leave input as blank")
        book_name = str(input("Please enter the name of the book: "))
    book_list.append(book_name)
    valid_book = False
    while not valid_book:
        author = (input("Enter writer of the book: "))
        string = check_string(author)
        if not string:
            print("Invalid name, Please enter a valid name")
        else:
            string = True
    book_list.append(author)


def check_string(author):
    try:
        str(author)
        return True
    except ValueError:
        return False





main()

#     else:
#         input("Input Error! Enter any key to try again.")
#
#
# print("Program exiting")
#
# def required_items():
#done




