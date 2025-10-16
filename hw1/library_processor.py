# library_processor.py
# MPCS 51042 Section 2. Autumn 2025.
#
# This program should read two input files and print specific output to the screen.
#
# Input File 1: current_inventory.txt
# Input File 2: daily_commands.txt
#
# Expected Output: see file library_processor_expected_output.txt

import os
import sys

print("=== LIBRARY OPERATIONS REPORT ===\n\nProcessing daily commands...\n")        # Intro line

file1 = "daily_commands.txt"        # Storing the two important files we have to read
file2 = "current_inventory.txt"

if not os.path.exists(file1):
    print("ERROR: The daily_commands.txt input file was not found.")
    sys.exit(1)

if not os.path.exists(file2):
    print("ERROR: The current_inventory.txt input file was not found.")
    sys.exit(1)

if os.path.getsize(file1) == 0:
    print("ERROR: The daily_commands.txt input file is empty. Please try again with appropriate formating of this file.")
    sys.exit(1)

if os.path.getsize(file2) == 0:
    print("ERROR: The current_inventory.txt input file is empty. Please try again with appropriate formating of this file.")
    sys.exit(1)

total_operations = 0        # Initializing total operations and errorness operations. We get sucessful operations from the difference
err_operations = 0

inventory_list = []     # We have another variable here that lets us store everything from the current_inventory.txt
with open(file2, "r") as f:
    for line in f:
        parts = [part.strip() for part in line.strip().split(',')]
        inventory = {
            "book_id": parts[0],
            "book_title": parts[1],
            "book_author": parts[2],
            "book_status": parts[3],
        }
        inventory_list.append(inventory)        # This will be easy to access

with open(file1, "r") as f:     # Opening daiy_commands
    for line in f:      # Reading each line
        total_operations += 1       # Each line represents an operation, this variable will store how many operations completed
        parts = [part.strip() for part in line.strip().split(',')]
        command = parts[0]      # initializing the command because it's easier to call than parts[0]

        if command == "add" and len(parts) == 4:        # Checks if add and if there's eaxactly four elements, this won't work without exactly four arguments
            new_book = {
                "book_id": parts[3],
                "book_title": parts[1],
                "book_author": parts[2],
                "book_status": "available",
            }
            inventory_list.append(new_book)
            print(f"Command: add {parts[1]} by {parts[2]}\nResult: Added Successfully\n")       # Will successfully add everything time because of the previous if statement
            with open(file2, "w") as f:
                for book in inventory_list:
                    f.write(f"{book['book_id']},{book['book_title']},{book['book_author']},{book['book_status']}\n")        # Add book here
            continue

        if command in ("checkout", "return"):       # Checks for command is equal to checkout or return
            target_id = parts[1]        # We are seaching this right here
            new_status = "checked_out" if command == "checkout" else "available"        # We have to give it checked_out
            print(f"Command: {command} {target_id}")
            found = False

            for book in inventory_list:
                if book["book_id"] == target_id:
                    found = True
                    if command == "checkout" and book["book_status"] == "checked_out":      # Returning/checking logic
                        err_operations += 1
                        print("This book cannot be checked out currently\n")
                    elif command == "return" and book["book_status"] == "available":
                        err_operations += 1
                        print("This book has already been returned\n")
                    elif command == "return":
                        book["book_status"] = new_status
                        print(f"Result: {book['book_title']} returned successfully\n")
                    else:
                        book["book_status"] = new_status
                        print(f"Result: {book['book_title']} checked out successfully\n")
                    break

            if not found:       # Book id was not found
                err_operations += 1
                print("Result: ERROR - Book not found\n")
            continue

        if command == "search":     # Checks for command search now
            search_term = parts[1].lower()
            found_books = []        # Initializes all the found books here
            print(f"Command: search {parts[1]}")
            for book in inventory_list:
                if search_term in book["book_title"].lower() or search_term in book["book_author"].lower():     # Checks for the search term in the book title and its author
                    found_books.append(book)        # If successful, it will add to the variable list

            if not found_books:     # Checks if never found a book
                err_operations += 1
                print("Result: Found 0 book(s):\n")
            else:
                print(f"Result: Found {len(found_books)} book(s):")     # Found x amount of books listed using the len() function
                for b in found_books:
                    status = "Checked Out" if b["book_status"] == "checked_out" else "Available"    # Gives availibility of the book
                    print(f"- {b['book_title']} by {b['book_author']} ({status})")  # Lists out all the books
                print()
            continue


        if(command == "remove"):        # Checks if remove command
            target_id = parts[1]
            found = False
            new_inventory = []          # Initializes a new list
            
            for book in inventory_list:
                if book["book_id"] == target_id:
                    found = True
                    removed_title = book["book_title"]
                    continue
                new_inventory.append(book)      # Won't append the book we are trying to remove using the continue key

            print(f"Command: remove {target_id}")
            if not found:       # Error if book is never found
                err_operations += 1
                print("Result: ERROR - Book not found\n")
            else:
                inventory_list = new_inventory      # Sets inventory_list as the new_inventory without the undesired book
                print(f"Result: {removed_title} removed successfully\n")
            continue

        else:       # Now checks for all other commands given, so we know this will be an error because the command isn't one of the declared ones like above 
            err_operations += 1
            args = " ".join(parts[1:]) if len(parts) > 1 else ""
            print(f"Command: {command} {args}".strip())
            print("Result: ERROR - Unknown command\n")
            continue

print("=== FINAL INVENTORY ===")        # Prints the inventory clearly and rewrites inventory_list
with open(file2, "w") as f:
    for book in inventory_list:
        f.write(f"{book['book_id']},{book['book_title']},{book['book_author']},{book['book_status']}\n")
        print(f"{book['book_id']},{book['book_title']},{book['book_author']},{book['book_status']}")

# Prints out operations completed, successful operations and unsucessful operations with their correspond numbers.
print(f"\nOperations completed: {total_operations}\nSuccessful operations: {total_operations-err_operations}\nErrors encountered: {err_operations}")
