
# importing module
import sys
from prettytable import PrettyTable

#initializing some variables
current_word = None
current_count = 0
word = None
total_words = 0

myTable = PrettyTable(["Badges","No of Badges"]) # creating table with these column names

for line in sys.stdin: # iterating trough each lines
    line = line.strip()
    word, count = line.split('\t', 1) # spliting the lines on the basis of tabs

    try:
        count = int(count)
    except ValueError:
        continue
    # counting Total no of different Badges and no of users in each badges
    if current_word == word:
        current_count += count
    else:
        if current_word:
            total_words = total_words + 1
            rows = [current_word,current_count]
            myTable.add_row(rows) # adding these rows to mytable
        current_count = count
        current_word = word

# to not skip the last line of the
if current_word == word:
    total_words = total_words + 1
    rows = [current_word,current_count]
    myTable.add_row(rows)


print(myTable) # printing table in a structured format
print ('{}\t{}'.format('Total no of different Badges are ',total_words))
