# import json
# import os

# # File path for storing the library data
# LIBRARY_FILE = "library.txt"


# def save_library(books):
#     """Save the library data to a file"""
#     try:
#         with open(LIBRARY_FILE, "w") as file:
#             json.dump(books, file, indent=4)
#         print(f"Library saved to {LIBRARY_FILE}")
#     except Exception as e:
#         print(f"Error saving library: {e}")


# def load_library():
#     """Load the library data from a file"""
#     if os.path.exists(LIBRARY_FILE):
#         try:
#             with open(LIBRARY_FILE, "r") as file:
#                 books = json.load(file)
#             print(f"Library loaded from {LIBRARY_FILE}")
#             return books
#         except Exception as e:
#             print(f"Error loading library: {e}")
#             return []
#     else:
#         print(f"No library file found. Starting with an empty library.")
#         return []


# # Initialize the Books list from the file
# Books = load_library()


# def libManager():
#     global Books
#     print(
#         "------------------Welcome to the Personal Library Manager!------------------"
#     )
#     # initializing condition so that we can exit it later
#     condition = True
#     while condition:

#         print(
#             "~~~~~~~~~~~~~~~~~~~~~~~~~\n1. Add a Book\n2. Remove a Book\n3. Search For a Book\n4. Display All Books\n5. Display Statistics\n6. Save Library\n7. Exit\n~~~~~~~~~~~~~~~~~~~~~~~~~"
#         )
#         opt = input("Enter Your Choice in Numbers (1,2,3,...):")
#         try:
#             # ADDING A BOOK
#             if int(opt) == 1:
#                 title = input("Enter the Book's Title: ")
#                 author = input("Enter the Book's Author: ")
#                 year = input("Enter the Publication Year: ")
#                 genre = input("Enter the genre (Fiction,Horror,...): ")
#                 isRead = input("Have you Read this Book? (yes/no):")
#                 book = {
#                     "title": title.lower(),
#                     "author": author.lower(),
#                     "year": int(year),
#                     "genre": genre.lower(),
#                     "isRead": True if isRead == "yes" else False,
#                 }
#                 Books.append(book)
#                 print("Book Added Successfully!")
#             # REMOVING A BOOK
#             elif int(opt) == 2:
#                 print("You Opt 2")
#                 if len(Books) > 0:
#                     bookTitle = input(
#                         "Enter the title of the book you want to remove: "
#                     )
#                     # Books = list(filter(lambda book: book.get("title") != bookTitle, Books)) #filter method
#                     Books = [
#                         book for book in Books if book.get("title") != bookTitle
#                     ]  # list comprehension method
#                     print("Book removed successfully! ")
#                 else:
#                     print("Please add a book first")
#             # SEARCH FOR A BOOK
#             elif int(opt) == 3:
#                 print("Search by: \n1. Title\n2. Author")
#                 choice = input("Enter your Choice (1 or 2): ")
#                 # search by title
#                 if int(choice) == 1:
#                     title = input("Enter the title: ")
#                     matchBooks = [book for book in Books if book.get("title") == title]
#                     if len(matchBooks) > 0:
#                         print("Matching Books: ")
#                         for i, book in enumerate(matchBooks):
#                             print(
#                                 f"{i+1}. {book.get('title')} by {book.get('author')} ({book.get('year')}) - {book.get('genre')} - {'Read' if book.get('isRead') else 'Unread'}"
#                             )
#                     else:
#                         print("No Book Found!")
#                 # search by author
#                 elif int(choice) == 2:
#                     author = input("Enter the Author: ")
#                     matchBooks = [
#                         book for book in Books if book.get("author") == author
#                     ]
#                     if len(matchBooks) > 0:
#                         print("Matching Books: ")
#                         for i, book in enumerate(
#                             matchBooks
#                         ):  # enumerate will break each list item into a tuple,as it returns tuples of (index, item)
#                             print(
#                                 f"{i+1}. {book.get('title')} by {book.get('author')} ({book.get('year')}) - {book.get('genre')} - {'Read' if book.get('isRead') else 'Unread'}"
#                             )
#                     else:
#                         print("No Book Found!")

#             # DISPLAY ALL BOOKS
#             elif int(opt) == 4:
#                 if len(Books) > 0:
#                     print("Your Library: ")
#                     for i, book in enumerate(Books):
#                         print(
#                             f"{i+1}. {book.get('title')} by {book.get('author')} ({book.get('year')}) - {book.get('genre')} - {'Read' if book.get('isRead') else 'Unread'}"
#                         )
#                 else:
#                     print("Please add a book first! ")
#             # DISPLAY STATISTICS
#             elif int(opt) == 5:
#                 totalBooks = len(Books)
#                 print(f"Total Books: {totalBooks}")
#                 if len(Books) > 0:
#                     readBooks = sum(1 for book in Books if book.get("isRead"))
#                     percent = (readBooks / totalBooks) * 100
#                     print(f"Percentage Read: {percent:.2f}%")
#                 else:
#                     print("Please add a Book first !")
#             # SAVE FILE
#             elif int(opt) == 6:
#                 save_library(Books)
#             # EXIT
#             elif int(opt) == 7:
#                 print("Library saved to file. Goodbye!")
#                 return
#             else:
#                 print("Please select from numbers given above!")
#         except:
#             print("Something went Wrong")
#             return


# libManager()


import json
import os

# File path for storing the library data
LIBRARY_FILE = "library.txt"


def save_library(books):
    """Save the library data to a file"""
    try:
        with open(LIBRARY_FILE, "w") as file:
            json.dump(books, file, indent=4)
        print(f"Library saved to {LIBRARY_FILE}")
    except Exception as e:
        print(f"Error saving library: {e}")


def load_library():
    """Load the library data from a file"""
    if os.path.exists(LIBRARY_FILE):
        try:
            with open(LIBRARY_FILE, "r") as file:
                books = json.load(file)
            print(f"Library loaded from {LIBRARY_FILE}")
            return books
        except Exception as e:
            print(f"Error loading library: {e}")
            return []
    else:
        print(f"No library file found. Starting with an empty library.")
        return []


# Initialize the Books list from the file
Books = load_library()


def libManager():
    global Books
    print(
        "------------------Welcome to the Personal Library Manager!------------------"
    )
    # initializing condition so that we can exit it later
    condition = True
    while condition:

        print(
            "~~~~~~~~~~~~~~~~~~~~~~~~~\n1. Add a Book\n2. Remove a Book\n3. Search For a Book\n4. Display All Books\n5. Display Statistics\n6. Save Library\n7. Exit\n~~~~~~~~~~~~~~~~~~~~~~~~~"
        )
        opt = input("Enter Your Choice in Numbers (1,2,3,...):")
        try:
            # ADDING A BOOK
            if int(opt) == 1:
                title = input("Enter the Book's Title: ")
                author = input("Enter the Book's Author: ")
                year = input("Enter the Publication Year: ")
                genre = input("Enter the genre (Fiction,Horror,...): ")
                isRead = input("Have you Read this Book? (yes/no):")
                book = {
                    "title": title.lower(),
                    "author": author.lower(),
                    "year": int(year),
                    "genre": genre.lower(),
                    "isRead": True if isRead.lower() == "yes" else False,
                }
                Books.append(book)
                print("Book Added Successfully!")
            # REMOVING A BOOK
            elif int(opt) == 2:
                if len(Books) > 0:
                    bookTitle = input(
                        "Enter the title of the book you want to remove: "
                    )
                    original_length = len(Books)
                    Books = [
                        book for book in Books if book.get("title") != bookTitle.lower()
                    ]  # list comprehension method
                    if len(Books) < original_length:
                        print("Book removed successfully!")
                    else:
                        print(f"No book with title '{bookTitle}' found.")
                else:
                    print("Please add a book first")
            # SEARCH FOR A BOOK
            elif int(opt) == 3:
                print("Search by: \n1. Title\n2. Author")
                choice = input("Enter your Choice (1 or 2): ")
                # search by title
                if int(choice) == 1:
                    title = input("Enter the title: ")
                    matchBooks = [
                        book for book in Books if book.get("title") == title.lower()
                    ]
                    if len(matchBooks) > 0:
                        print("Matching Books: ")
                        for i, book in enumerate(matchBooks):
                            print(
                                f"{i+1}. {book.get('title').title()} by {book.get('author').title()} ({book.get('year')}) - {book.get('genre').title()} - {'Read' if book.get('isRead') else 'Unread'}"
                            )
                    else:
                        print("No Book Found!")
                # search by author
                elif int(choice) == 2:
                    author = input("Enter the Author: ")
                    matchBooks = [
                        book for book in Books if book.get("author") == author.lower()
                    ]
                    if len(matchBooks) > 0:
                        print("Matching Books: ")
                        for i, book in enumerate(matchBooks):
                            print(
                                f"{i+1}. {book.get('title').title()} by {book.get('author').title()} ({book.get('year')}) - {book.get('genre').title()} - {'Read' if book.get('isRead') else 'Unread'}"
                            )
                    else:
                        print("No Book Found!")

            # DISPLAY ALL BOOKS
            elif int(opt) == 4:
                if len(Books) > 0:
                    print("Your Library: ")
                    for i, book in enumerate(Books):
                        print(
                            f"{i+1}. {book.get('title').title()} by {book.get('author').title()} ({book.get('year')}) - {book.get('genre').title()} - {'Read' if book.get('isRead') else 'Unread'}"
                        )
                else:
                    print("Please add a book first! ")
            # DISPLAY STATISTICS
            elif int(opt) == 5:
                totalBooks = len(Books)
                print(f"Total Books: {totalBooks}")
                if len(Books) > 0:
                    readBooks = sum(1 for book in Books if book.get("isRead"))
                    percent = (readBooks / totalBooks) * 100
                    print(f"Percentage Read: {percent:.2f}%")

                    # Add genre statistics
                    genres = {}
                    for book in Books:
                        genre = book.get("genre")
                        if genre in genres:
                            genres[genre] += 1
                        else:
                            genres[genre] = 1

                    print("\nGenre Distribution:")
                    for genre, count in genres.items():
                        print(f"- {genre.title()}: {count} books")
                else:
                    print("Please add a Book first!")
            # SAVE FILE
            elif int(opt) == 6:
                save_library(Books)
            # EXIT
            elif int(opt) == 7:
                save_library(Books)  # Save library before exiting
                print("Goodbye!")
                return
            else:
                print("Please select from numbers given above!")
        except Exception as e:
            print(f"Something went wrong: {e}")
            return


libManager()
