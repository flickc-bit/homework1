# analytics_generator.py
# MPCS 51042 Section 2. Autumn 2025.
#
# This program should read a checkout history log and generate a comprehensive report.
#
#  Input File: checkout_history.txt
# 
#  Expected Output: see file analytics_generator_expected_output.txt

from collections import Counter
import os
import sys

file = "checkout_history.txt"       # Initializes the file

if not os.path.exists(file):      # If we don't have access to the desired file, we print the following statement and then exit
    print("ERROR: The desired input file was not found.")
    sys.exit(1)

if os.path.getsize(file) == 0:      # If the file is completely empty, we can't do anything with it so we print out the following statement and then exit the code
    print("ERROR: The desired input file was not found.")
    sys.exit(1)

checkouts = []      # Initializes a list we will be using

total_lines = 0      # Initializes the total number of lines
with open(file, "r") as f:      # Opens the file, reads every lines and increments total_lines accordingly
    for line in f:
        total_lines += 1
        parts = [part.strip() for part in line.strip().split(',')]
        checkout = {        # First strips all the information in the input file and then stores it conviently in checkout which will then be appended in checkouts
            "checkout_date": parts[0],
            "book_id": parts[1],
            "citizen_name": parts[2],
            "book_status": parts[3],
            "book_title": parts[4],
            "book_author": parts[5],
        }
        checkouts.append(checkout)

all_books_used = []     # Initializes a list that keeps track of books we have seen
total_books = 0     # Int that stores total books
for row in checkouts:
    if((row["book_title"], row["book_author"]) not in all_books_used):      # Checks if title and author for each book is unique
        total_books += 1
    all_books_used.append((row["book_title"], row["book_author"]))

book_counts = Counter(all_books_used)       # Initializes a counter of all_books_used

counter = 1
checkout_list = ""
most_popular_book = ""

for (title, author), count in book_counts.most_common():  # .most_common sorts by most checkouts
    checkout_list += f"{counter}. {title} written by {author} ({count} checkouts)\n"        # Writes out the counter (1-n). then the title, author and how many times it's been checkedout 
    if counter == 1:        # Will always make the first book the most popular book because it has been already sorted from most popular to least
        most_popular_book = f"{title} ({count} - consider additional copies)"
    counter += 1

all_patrons = []        # New list that counts all the patrons
total_patrons = 0       # Keeps track of how many unique patrons there is
repeated_patrons = ""
for row in checkouts:       # Reiterates over checkouts, if someone isn't in all_patrons we increment total_patrons and then add them to all_patrons list
    if(row["citizen_name"]) not in all_patrons:
        total_patrons += 1
    elif(repeated_patrons != ""):       # Now we know this name is in all_patrons, so we check if it's empty, if not we need a comma to format it correctly
        repeated_patrons += f', {row["citizen_name"]}'
    else:       # It's the last test case but we don't need a comma anymore
        repeated_patrons += f'{row["citizen_name"]}'
    all_patrons.append((row["citizen_name"]))

if(repeated_patrons == ""):     # If nothing is in repeated_patrons, we print this information out to the user
    repeated_patrons = "There is no active patrons with multiple checkouts.\n"

patron_counts = Counter(all_patrons)        # Count patrons so we know all their information

counter = 1
patron_list = ""
for citizen_name, count in patron_counts.most_common():     # Reiterates over the now sorted list of patrons
    patron_list += f"{counter}. {citizen_name} ({count} checkouts)\n"       # Lists the n number of patron, name and then how many times they came up in the system (# of checkouts)
    counter += 1

currently_checked_out = []      # Makes a new list for currently checked out patrons
for row in checkouts:       # Iterates and grabs all information from checkouts
    currently_checked_out.append(((row["citizen_name"]), (row["book_title"]), (row["checkout_date"]), (row["book_status"])))

counter = 1
total_checked_out = 0
checkout_order = ""     # After estalishing out variables, we loop through currently_checked_out
for (citizen_name, book_title, checkout_date, book_status) in currently_checked_out:
    if(book_status == "active"):     # Checks active meaning in use (not in the library), adds to checkedout_order and increments accordingly
        checkout_order += (f"- {book_title} ({citizen_name} since {checkout_date})\n")
        total_checked_out += 1

avg_checkouts_per_citizen = total_lines/total_patrons       # Calculates avg_checkouts_per_citizen
return_rate = f"{(total_checked_out/total_books)*100:.1f}"


# prints out everything necessary using a cmbination of strings and variables as listed above
print(f"=== LIBRARY USAGE ANALYTICS ===\n\nMost Popular Books:\n{checkout_list}\nMost Active Patrons:\n{patron_list}\nCurrently Checked Out:\n{checkout_order}\nSummary Statistics:\n- Total checkouts processed: {total_lines}\n- Unique books: {total_books}\n- Unique patrons: {total_patrons}\n- Average checkouts per patron: {avg_checkouts_per_citizen}\n- Books currently checked out: {total_checked_out}\n- Return rate: {return_rate}%\n\nAlerts:\n-  High demand book: {most_popular_book}\n- Active patrons: {repeated_patrons} (multiple checkouts)\n\nYour program should handle:\n- Malformed lines in input files (skip with error message)\n- Empty files\n- Missing files (graceful error handling)")
