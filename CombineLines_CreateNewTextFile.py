#22-2-20 A script for removing the line breaks in Youtube video transcript to be continous. There two option, with or  = to open the original file
#create a new file with combinetext.txt if not already exist with that name. 
# fnew = open('/Users/hieu/Documents/DS_Study_20_Notes/5_Weeks_Python/combinetext2.txt', 'w') with path on my Mac
fnew = open('combinetext2.txt', 'w')

# Option: 1
# with open('/Users/hieu/Documents/DS_Study_20_Notes/5_Weeks_Python/YoutubeFindingWhatUWant.txt') as fhand:
#     lines = " ".join(lines.strip() for lines in fhand)
    # add the content to the file
#     fnew.write(lines) 

# Option: 2 
# fhand = open('/Users/hieu/Documents/DS_Study_20_Notes/5_Weeks_Python/YoutubeFindingWhatUWant.txt') with path on my Mac
fhand = open('YoutubeFindingWhatUWant.txt')
lines = " ".join(lines.strip() for lines in fhand)
# add the content to the file
fnew.write(lines)
# close that file. 
fnew.close() 
