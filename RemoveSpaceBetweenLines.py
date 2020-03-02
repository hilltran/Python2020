# output = open('/Users/hieu/Desktop/1_Excel/deleteBlankLinesOutputFile3-20.txt', 'w')
output = open('deleteBlankLinesOutputFile3-20.txt', 'w')


#remove blank lines by opening the original file and r = read only
# with open('/Users/hieu/Desktop/1_Excel/removeBlankLine.txt','r') as file:
with open('removeBlankLine.txt','r') as file:
    for line in file:
        if not line.isspace():
            #save each line that has content
            output.write(line)
            # print(line)
            #the print function create an extra line but the actual file doesn't 
# close file once the content has been added.
output.close()  
