'''Design an application where user will input two dates.
    1. His/her date of birth in DD/MM/YY format.
    2. Current (Present day) date in DD/MM/YY format.
Your app will calculate and let the user know how many days that person survived in this world.'''

# Importing the required modules
import sys
import datetime

# Defining the main function
def main():
    '''This is the main function'''
    # Getting the user input
    date_of_birth = input('Enter the date of birth: ')
    current_date = input('Enter the current date: ')
    # Calling the function to get the result
    result = life_duration(date_of_birth, current_date)
    # Printing the result
    print(result)

# Defining the function to get the life duration
def life_duration(date_of_birth, current_date):
    '''This function gets the life duration'''
    # Converting the date of birth to datetime
    date_of_birth = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
    # Converting the current date to datetime
    current_date = datetime.datetime.strptime(current_date, '%d/%m/%Y')
    # Getting the life duration
    life_duration = current_date - date_of_birth
    # Returning the result
    return life_duration

# Calling the main function
if __name__ == '__main__':
    main()
