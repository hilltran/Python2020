#getting rid of the first word or number on each line from a text file. 
# fhand = open("/Users/hieu/Desktop/1_Excel/30ExcelLessons.txt")
# output = open('/Users/hieu/Desktop/1_Excel/deleteNumber30ExcelLessons3-20.txt', 'w')

fhand = open("30ExcelLessons.txt")
output = open('deleteNumber30ExcelLessons3-20.txt', 'w')

# new_text = []
string_line = " "
for lines in fhand:
    words = lines.split()
    del words[0]
    string_line = ' '.join(map(str, words)) + '\n' #need to add new line ('\n') each time otherwise it joins together as one line.
    # string_line.join(words) 
    #using map() to convert each item in the list to a string, and then join them
    output.write(string_line)
    
output.close()

