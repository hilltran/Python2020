
# 26-2-20 Relating to Task10_Excercise3.py update version. this program take the all the text 
# from a file and tally the number of each letter of the alphabet. 
# This update has gives the client what files they want to have letter count instead of the preset file. 

# fhand = open('/Users/hieu/Documents/DS_Study_20_Notes/5_Weeks_Python/mbox.txt')
# fhand = open('mbox.txt')

while True:
    file_name  = input('Enter file name with extension and if on Mac also path: ')
    if file_name == 'exit':
            exit()
    #this gives the customer option to exit, for whatever reason they have the choice not proceed.
    try:
        fhand = open(file_name)
        break
    except:
        print('Please enter correct file name or type "exit" to quit')
        continue

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
