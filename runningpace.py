# Define again() function to ask user if they want to use the calculator again
def again():
    calc_again = input('''
Do you want to calculate again?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()
    elif calc_again.upper() == 'N':
        print('See you later.')
    else:
        again()

def calculate():        
    print('Enter distance in km')
    distance = int(input(''))
    print('Enter finishing time in minutes')
    time = int(input(''))
    
    pace = (time / distance)
    minutes = int(pace)

    afterdecimal = pace - int(pace)
    seconds = round((afterdecimal*60))

    print('You will have to run ' + str(minutes) + ' minutes and ' + str(seconds) + ' seconds per kilometer') 

    again()
        
calculate()
