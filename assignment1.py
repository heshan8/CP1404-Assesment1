"""
CP1404 Assignment -1-
13/4/2017
Reading list by Tharindu Heshan
Add github link
"""



import csv

MAIN_MENU = "\nMain menu:\n R - Show list of required books\n C - Show list of completed books\n" \
            " A - Add a new book\n M - Mark a book as completed\n Q - Quit" """ efswfsef sdefsd"""

def main():
    with open('books.csv', 'r') as f:
        writer = csv.reader(f)
        reading_list = list(writer)
        reading_list.sort()
    print("Reading List 1.0 - by Tharindu Heshan")
    print(MAIN_MENU)
    menu_choice = input("Enter choice: ").upper()
    while menu_choice != "Q":
        if menu_choice == "R":
            show_list(reading_list, menu_choice.lower())
        elif menu_choice == "C":
            show_list(reading_list, menu_choice.lower())
        elif menu_choice == "A":
            add_book(reading_list)
        elif menu_choice == "M":
            show_list(reading_list, menu_choice.lower())
            mark_book(reading_list)
        else:
            print("Invalid input, Try again.")
        print(MAIN_MENU)
        menu_choice = input("Enter choice: ").upper()
    with open("books.csv", "w", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(reading_list)
    if menu_choice == "Q":
        print("Have a nice day :)")


#  pseudocode:
#     function show_list()
#     if book == "r":
#         print "List of required books"
#     elif book == "c"
#         print "List of completed books"
#     elif book == "m"
#     calculate total number of pages
# if count == 0:
#     if book == "r"
#      print "no required books to display"
#     elif book == "c"
#         print "no completed books to display"
#     elif:
#         print"no books exist"
#     else:
#         display list of completed or required books
def show_list(reading_list, book):
    if book == "r":
        print("List of required books:")
    elif book == "c":
        print("List of completed books:")
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
                    print(book[0], "is now marked as completed" )
                    valid_booknumber = True
                    break
            elif count == book_number:
                print("Warning, the book was not marked")
                valid_booknumber = True
                break
        if not valid_booknumber:
            print("Invalid book number, try again")

# pseudocode:
#   book_list = []
#        get name of book
#        add to book_list
#        get author
#        add to book_list
#        get number of pages
#        add to book_list
#        append new list to reading_list
def add_book(reading_list):
        book_list = []
        book_name = str(input("Enter the name of the book you want to add: "))
        while not book_name:
            print("Input Cannot be blank")
            book_name = str(input("Enter the name of the book you want to add: "))
        book_list.append(book_name)
        author = (input("Enter the writer of the book: "))
        while not author:
            print("Input Cannot be blank")
            author = (input("Enter the writer of the book: "))
        book_list.append(author)
        pages = int(input("Enter the number of pages in the book: "))
        if pages < 1:
            print("Number of pages must be higher than 1")
            pages = (input("Enter the number of pages in the book: "))
        else:
            book_list.append(pages)
        reading_list.append(book_list)
        print("{} By {} ({} Pages) added to reading list".format(book_name, author, pages))

main()

