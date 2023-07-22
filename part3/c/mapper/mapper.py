
# importing sys module
import sys

for x in sys.stdin: # iterating trough each lines

    index = [] # creating a list to store the index of line which contains double inverted commas

    for a in range(len(x)): # appending the indices of double inverted commas in list
        if x[a] == '\"':
            index.append(a)

    for b in range(len(index)): # iterating through pairs of index to extract elements
        if b %2 == 0:
            text = x[index[b - 1]:index[b] + 1]
            text = text.strip("\"") # removing unnecessary characters
            text = text.strip("=")

            if "CreationDate" in text:
                text2 = x[index[b]:index[b+1] + 1] # extracting the value of userid
                text2 = text2.strip("\"")
                text2 = text2.split(":") # spliting on the basis of : to extract the year-month-date and hour
                print("{}\t{}".format(text2[0],1)) # printing key tab value pairs
