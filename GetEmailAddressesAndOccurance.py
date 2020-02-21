# 21-2-2020 A program to read through email log, 
# using a dictionary to count how many messages came from each email address, and print the dictionary.
# relating to Task9_Excercise3.py

fhand = open('mbox-short.txt')
word_count = {}
for lines in fhand:
    words = lines.split()
    if len(words) == 0 or words[0] != "From": continue
    for word in words:
        if '@' not in word: continue
        if word in word_count.keys():
            word_count[word] += 1
        else:
            word_count[word] = 1
print(word_count)
