
import sys

for x in sys.stdin:

    index = []
    flag = False

    for a in range(len(x)):
        if x[a] == '\"':
            index.append(a)

    for b in range(len(index)):
        if b %2 == 0:
            text = x[index[b - 1]:index[b] + 1]
            text = text.strip("\"")
            text = text.strip("=")

            if "UserId" in text:
                text2 = x[index[b]:index[b+1] + 1]
                text2 = text2.strip("\"")
                print("{}\t{}".format(text2,1))
