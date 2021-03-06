import time
import sys

# filename is pulled from command line, otherwise use "data.txt"
if len(sys.argv) > 1:
    file = open(sys.argv[1], "r")
else:
    file = open("data.txt", "r")
# read file and create list with " " as delimeter
uList = list(map(int, file.read().split(" ")))
# remove first index which we don't need in this program
n = uList[0]
del uList[0]
oList = []

# start timer
start_time = time.time()

# iterate through unsorted list and sort items in the sorted list
for i in range(0, n):
    # if list is empty, add first item
    if(not len(oList)):
        oList.append(uList[i])
    else:
        # bool to check if we've inserted the item
        insert = False
        # iterate through sorted list and until a smaller number is found
        for j in range(len(oList), 0, -1):
            if(oList[j - 1] <= uList[i]):
                # insert the item and exit loop
                oList.insert(j, uList[i])
                insert = True
                break
        # if end of loop is reached without insert, insert item at beginning of list
        if not insert:
            oList.insert(0, uList[i])

# write data to file
first = True
with open("insert.txt", "w") as file:
    for item in oList:
        if first:
            file.write("%s" % item)
            first = False
        else:
            file.write(" %s" % item)
    file.write("\n")

# print sort time
# print("%s seconds" % (time.time() - start_time))
