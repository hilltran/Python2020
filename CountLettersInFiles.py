
#Relating to Task10_Excercise3.py

# fhand = open('/Users/hieu/Documents/DS_Study_20_Notes/5_Weeks_Python/mbox.txt')
fhand = open('mbox.txt')

letter_count = {}
for lines in fhand:
    lines = lines.rsplit()
    for i in lines:
        for char in i:
            if char.isalpha() == True:
                char = char.lower()
                letter_count[char] = letter_count.get(char,0) + 1

# print(letter_count)
list_tup = []
for key, val in letter_count.items():
    list_tup += [(val,key)]

list_tup.sort(reverse=True)
# print(list_tup)
for k in list_tup:
    print(k)
