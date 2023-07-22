
# importing modules
import sys
from prettytable import PrettyTable

def median_calc(alist): # function to calculate median of an unsorted list
    alist = sorted(alist) # sorting the list
    length = len(alist)
    if length % 2 == 0: # if lenght is even then median is avg of mid two elements
        med = (int(alist[int(length/2)-1]) + int(alist[int(length/2)]) )/2
    else: # if lenght is odd then median is mid element
        med = int(alist[length//2])
    return med

current_word = None
current_count = 0

word2 = None
total_words = 0
median_list = []
myTable = PrettyTable(["Dates","Median per months"]) # creating a table object

for line in sys.stdin:
    line = line.strip()
    word, length = line.split('\t', 1)
    length = int(length)
    count = 1
    lis = word.split("-")
    word2 = lis[0] + "/" + lis[1]

    if current_word == word2:
        current_count += count
        median_list.append(length)
    else:
        if current_word:
            total_words = total_words + count
            myTable.add_row([current_word, median_calc(median_list)])
            median_list = []

        current_count = count
        current_word = word2
        median_list.append(length)

if current_word == word2:
    median_list.append(length)
    current_count += count
    myTable.add_row([current_word, median_calc(median_list)])

print(myTable)
print ('{}{}'.format('Total numbe no of dates are ',total_words+1))