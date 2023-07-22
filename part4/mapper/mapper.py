
# importing sys module
import sys

for x in sys.stdin: # reading each lines from the comment.xml file

    index = [] # creating a list to hold the index of line containing ' " '

    for a in range(len(x)): # append the indeces of ' " '
        if x[a] == '\"':
            index.append(a)

    for b in range(len(index)):
        if b %2 == 0:
            text = x[index[b - 1]:index[b] + 1] # iterating over pair of pair of two indeces of index list
            text = text.strip("\"")
            text = text.strip("=")
            if "Text" in text: # if the column is text
                text3 = x[index[b]:index[b + 1] + 1] # extract the value
                text3 = text3.strip("\"")
                length = len(text3) # finding the length of text
            if "CreationDate" in text: # if the column is creationdate
                text2 = x[index[b]:index[b+1] + 1] # extract the value
                text2 = text2.strip("\"")
                text2 = text2.split("T") # finding the year-month-date
                print("{}\t{}".format(text2[0],length))


