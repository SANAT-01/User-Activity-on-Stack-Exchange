
# importing module
import sys
from prettytable import PrettyTable

# initializing some variables
current_word = None
current_count = 0
word = None
hours = [0]*24 # to hold the no of post in each hour from may 2014 to sep 2017
years = [0]*8 # # to hold the no of post in each year from may 2014 to sep 2017

total_words = 0
maxi = 0
mini = 64851

myTable = PrettyTable(["Dates","Count"]) # creating table with these column names

for line in sys.stdin: # iterating trough each lines

    line = line.strip()

    word, count = line.split('\t', 1) # spliting the lines on the basis of tabs

    try:
        count = int(count)
    except ValueError:
        continue

    word2 = int(word[len(word) - 2:]) # to extract the hour part from word and setting it as index for hour list
    word3 = int(word.split("-")[0]) # to extract the year part from word
    word3_index = word3 - 2014  # creating index for year list (range 0 to 7)
    # adding and storing total no of post in each year and each hour
    hours[word2] = hours[word2] + count
    years[word3_index] = years[word3_index] + count

    if current_word == word:
        current_count += count
    else:
        if current_word:
            total_words = total_words + 1
            if int(current_count) > maxi :
                maxi = current_count
            if int(current_count) < mini :
                mini = current_count
            rows = [current_word.replace("T"," : "),current_count]
            myTable.add_row(rows) # adding these rows to mytable
        current_count = count
        current_word = word

# to not skip the last line of the
if current_word == word:
    rows = [current_word.replace("T"," : "),current_count]
    myTable.add_row(rows)

print(myTable)
print ('{}\t{}'.format('Total are ',total_words+1))
print("The ratio of the peak to lowest user activity per hour is",maxi/mini,"with max and min ",maxi,mini)
print()

# table for hours and count
myTable2 = PrettyTable(["Hour","Count"])
for z in range(24):
    myTable2.add_row([z,hours[z]])
print(myTable2)
print("The ratio of the peak to lowest user activity per hour is",max(hours)/min(hours),"with max and mini",max(hours),min(hours))

print()
# table for years and count
myTable3 = PrettyTable(["Years","Count"])
for z in range(8):
    col1 = z+2014
    myTable3.add_row([col1,years[z]])
print(myTable3)
print("The ratio of the peak to lowest user activity per hour is",max(years)/min(years),"with max and mini",max(years),min(years))