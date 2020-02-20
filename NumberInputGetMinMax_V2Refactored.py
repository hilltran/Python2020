
#Functions for Github push 20 Feb 2020 Version 2 - Task8_Excercise6.py
# the maximum and minimum of the numbers at the end when the user enters "done". 
#the program stores the numbers the user enters in a list and using the max() and min() functions to 
# compute the maximum and minimum numbers after the loop completes.
#Code was refactored later during the day on 20 Feb 2020.

stored_numbers = []
while True:
    number_entered = input("Please enter number ")
    if number_entered == 'done':
        break
    try:
        number_entered = float(number_entered)
    #except clause is to safe guard against errors and only numbers can be entered even if it's with decimal point. 
    except:
        print("Error must be numeric value")
        continue
    stored_numbers.append(number_entered)

# if statement to safe guard against trackback error if the first input is 'done'
if len(stored_numbers) == 0:
    quit()
print(f'Minimium number is {min(stored_numbers)} \nMaximium number is {max(stored_numbers)}')
