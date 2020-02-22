# Print the top 10 most common words related to Task10_Playground.py

# fhand = open('/Users/hieu/Documents/DS_Study_20_Notes/5_Weeks_Python/romeo.txt') my Mac path
fhand = open('romeo.txt')
counts= {}
for lines in fhand:
    line = lines.split()
    for word in line:
        counts[word] = counts.get(word,0) + 1

list_counts = []
for k,v in counts.items():
    list_counts += [[v,k]]
list_sorted = sorted(list_counts, reverse=True)
# k is the key and v is the value turn it into a list so it can be sorted

count = 0
for v,k in list_sorted:
    # for loop to go through the list
    while count < 10:
        # the while is to print up to 10 and then
        print(list_sorted[count])
        count += 1
    quit()


