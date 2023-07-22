
# importing sys module
import sys

for x in sys.stdin:  # iterating trough each lines

    index = [] # creating a list to store the index of line which contains double inverted commas
    flag = False # creating a flag to check whether a given line contains viewcount or not

    for a in range(len(x)): # appending the indices of double inverted commas in list
        if x[a] == '\"':
            index.append(a)

    for b in range(len(index)): #  iterating through pairs of index to extract elements
        if b %2 == 0:
            text = x[index[b - 1]:index[b] + 1]
            text = text.strip("\"") # removing unnecessary characters
            text = text.strip("=")

            if "ViewCount" in text:
                text2 = x[index[b]:index[b+1] + 1] # extracting the value of viewcount
                text2 = text2.strip("\"")
                flag = True # setting flag as true, means this line has a viewcount

            if "Title" in text:
                text3 = x[index[b]:index[b+1] + 1] #  extracting the value of viewcount
                text3 = text3.strip("\"")
                print("{}\t{}\t{}".format(text2,1,text3)) # printing key tab value pairs

    if flag:
        continue
    else:
        print("{}\t{}\t{}".format(0,1,"Empty")) # printing key tab value pairs if viewcount not present in line, means viewcount is zero
