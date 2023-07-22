
# import sys because we need to read and write data to STDIN and STDOUT
import sys

# reading entire line from STDIN (standard input)
for x in sys.stdin:
    index = [] # creating a list to store the index of line which contains double inverted commas

    for a in range(len(x)): # appending the indices of double inverted commas in list
        if x[a] == '\"':
            index.append(a)

    for b in range(len(index)): # iterating through pairs of index to extract elements
        if b %2 == 0:
            text = x[index[b - 1]:index[b] + 1]
            text = text.strip("\"") # to remove unwanted characters
            text = text.strip("=")
            if "Tags" in text:
                text2 = x[index[b]:index[b+1] + 1]  # extracting the value of tags
                text2 = text2.split(";&lt;") # extracting different elements of tags
                for y in text2: # iterating upon differrnt tags
                    y = y.replace("&gt","")
                    y = y.replace("\"&lt", "")
                    y = y.replace("\"", "")
                    y = y.replace(";", "")
                    print("{}\t{}".format(y,1)) # printing key tab value pairs
