
#Functions for Github push 20 Feb 2020 Version 1 - Task8_Excercise6.py
# the maximum and minimum of the numbers at the end when the user enters "done". 
#the program stores the numbers the user enters in a list and using the max() and min() functions to 
# compute the maximum and minimum numbers after the loop completes.

number_entered = input("please enter number as numeric: ")

def check_num(input_val):
    try:
        input_val = float(input_val)
        return input_val
    except:
        print("Error must be numeric value")
    
stored_numbers = []
while number_entered != None:
    if number_entered == 'done':
        break
    check_num(number_entered)
    if number_entered.isnumeric():
        stored_numbers.append(int(number_entered))
        # stored_numbers.append(float(number_entered))
    number_entered = input("please enter number as numeric: ")

if len(stored_numbers) == 0:
    quit()

print(min(stored_numbers), max(stored_numbers))
print(stored_numbers)