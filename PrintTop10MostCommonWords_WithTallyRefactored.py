# Print the top 10 most common words related to Task10_Playground.py, refactored on 24-2-20

# fhand = open('/Users/hieu/Documents/DS_Study_20_Notes/5_Weeks_Python/romeo.txt') path on my mac
##WITHOUT REFACTORING in below between the  ___________________
# ___________________
# counts = {}
# for lines in fhand:
#     line = lines.split()
#     for word in line:
#         counts[word] = counts.get(word,0) + 1

# list_counts = []
# for k,v in counts.items():
#     key_val = (v,k)
#     list_counts.append(key_val)
# list_sorted = sorted(list_counts, reverse=True)
# # k is the key and v is the value turn it into a list so it can be sorted

# count = 0
# for v,k in list_sorted:
#     # for loop to go through the list
#     while count < 10:
#         # the while is to print up to 10 and then
#         print(list_sorted[count])
#         count += 1
#     quit()
# ___________________

## Refactored 
fhand = open('romeo.txt') 
counts = dict()
for line in fhand:
    words = line.split()
    for word in words :
        counts[word] = counts.get(word, 0 ) + 1

list_w = list()
for key, val in counts.items():
    list_w += [[val, key]]
    #This here was not refactored but in original it is equivalent to line 14 - 15, this code is shorter.

list_w = sorted(list_w, reverse=True)

for val, key in list_w[:10]:
    print(val, key)
    #since it is sorted only need to select the index from 0-9. 




