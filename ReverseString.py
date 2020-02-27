stringg= 'tetete reverse'
rev_verse = stringg[::-1]
md_2 = stringg[len(stringg)::-1]
print(rev_verse, md_2)

rev_string = ''
index_len = len(stringg)-1
#index starts from zero so len must be minus 1 to ensure it starts from the last letter. 
while index_len > 0:
    rev_string += stringg[index_len]
    index_len -= 1
print(rev_string)