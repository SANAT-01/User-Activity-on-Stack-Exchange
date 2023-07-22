
# importing module
from operator import itemgetter
import sys
from prettytable import PrettyTable

#initializing some variables
current_word = None
current_count = 0
word = None

viewcount = [0,0,0,0,0,0,0,0,0,0] # to store top 10 viewcount
lines = [0]*10 # to store top 10 title

times = 0 # How many posts were viewed a given number of times

for line in sys.stdin: # iterating trough each lines
    line = line.strip()

    if line == "":
        continue

    word, count, x = line.split('\t', 2) # spliting the lines on the basis of tabs

    try:
        count = int(count)
    except ValueError:
        continue
    # counting the no of post with post with viewcount = times
    if word == str(times):
        current_count = current_count + count
    if max(viewcount) < int(word):
        if max(viewcount) > min(viewcount):
            index = viewcount.index(min(viewcount))
            viewcount[index] = int(word)
            lines[index] = x
        else:
            index = viewcount.index(max(viewcount))
            viewcount[index] = int(word)
            lines[index] = x
    elif min(viewcount) < int(word):
        index = viewcount.index(min(viewcount))
        viewcount[index] = int(word)
        lines[index] = x

print('{} {} for viewcount {}'.format('Total no of comments are', current_count, times))
print("Change manually the value of variable \'times\' to count total no of comments with a given viewcount ")
print("Top 10 most viewed posts on DataScienceExchange are ")

mytable = PrettyTable(["ViewCount", "Title"]) # # creating table with these column names
for y in range(10):
    rows = [viewcount[y], lines[y]]
    mytable.add_row(rows)
print(mytable) # printing table in a structured format