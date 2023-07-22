# importing required modules

from prettytable import PrettyTable


# it is a function to extract the total no of columns and takes input as file object
def columns(op):
    x = op.readline()  # it will just read the first line, as it is of no use, and also while condition remains true
    column = []  # initializing a column list to hold the unique columns

    while x:  # verify that we are not working upon a empty line

        try:
            x = op.readline()
            x = x.strip(" ")
        except:
            continue

        if "<" in x:  # verify that we are not working upon a unneccesary
            index = []  # initializing the list to hold the indeces of " in the line
            for a in range(len(x)):
                if x[a] == '\"':  # appending the indeces of " from the line
                    index.append(a)

            for b in range(len(index)):  # iterating upon two pair of index elements, so as to satify the requirements
                if b == 0:  # if this then appending the "row Id" element
                    text = x[1:7]

                elif b % 2 == 0:  # extracting only the column names
                    text = x[index[b - 1]:index[b] + 1]
                    text = text.strip('=\"')
                    text = text.lstrip(' ')

                if text in column:  # checking whetehr this is already in the list or not
                    pass
                else:  # if the element is not in list then appending it to the column list
                    column.append(text)

    return column  # returning all unique columns for a single file


total_columns = []  # a list to holds all unique columns of all the 8 files
file_column = []  # a list to hold the unique columns of each file for 8 different files in form of nested list
files = [r"Badges.xml", "Users.xml", r"Votes.xml", r"Comments.xml", r"PostLinks.xml", r"Posts.xml", r"Tags.xml",
         r"PostHistory.xml"]  # 8 different file names

for y in range(
        len(files)):  # a loop to append the unique columns of each file for 8 different files in form of nested list
    file = open(files[y])  # creating file object
    clmn = columns(file)  # calling the function
    file_column.append(clmn)  # appending it to list
    file.close()  # closing the file

for a in range(8):  # loop to append only the unique columns of all 8 files
    for b in range(len(file_column[a])):
        if file_column[a][b] in total_columns:
            continue
        else:
            total_columns.append(file_column[a][b])

# creating a structured table using Prettytable
fields = ["Filename"]  # first column
for b in range(len(total_columns)):  # appending the next few column
    fields.append("Field " + str(b + 1))

myTable = PrettyTable(fields)  # ceating table object using Prettytable
total_columns = sorted((total_columns))
for a in range(8):  # for adding rows
    rows = [files[a]]  # first element as a file name
    for b in range(len(total_columns)):  # adding rows to table
        if total_columns[b] in file_column[a]:  # adding rows to table on the basis of columns in total_columns
            rows.append(total_columns[b])
        else:  # if not present then marked as "X"
            rows.append("X")
    myTable.add_row(rows)  # adding a new row

print(myTable)  # printing the table