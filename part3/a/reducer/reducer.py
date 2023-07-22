#!/usr/bin/env python

from operator import itemgetter
import sys
from prettytable import PrettyTable

# initializing some variables
current_word = None
current_count = 0
word = None
total_words = 0

myTable = PrettyTable(["Tags","No of Tags"]) # creating table with these column names

# read the entire line from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # slpiting the data on the basis of tab we have provided in mapper.py
    word, count = line.split('\t', 1)
    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer
    if current_word == word:
        current_count += count
    else:
        if current_word:
            total_words = total_words + 1
            rows = [current_word,current_count]
            myTable.add_row(rows) # adding these rows to mytable
        current_count = count
        current_word = word


# do not forget to output the last word if needed!
if current_word == word:
    total_words = total_words + 1
    rows = [current_word,current_count]
    myTable.add_row(rows) 

print(myTable) # printing table in a structured format
print ('{}\t{}'.format('Total no of words are ',total_words))
