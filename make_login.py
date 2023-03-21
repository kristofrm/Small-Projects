#Kristof Rohaly-Medved
#CS21
#Program to read employee info from file and create login info from read data

import random

def main():
    line_count = 0
    mywords = ("Soccer", "Football", "Basketball", "Rugby", "Frisbee", "Volleyball", "Chess", "Golf", "Baseball", "Lacrosse")
    #Read in employee info
    employee_info = input('Input file: ')
    try:
        infile = open(employee_info, 'r')
    except IOError:
        print('Error opening input file. Exiting program ...')
    else:
        line = infile.readline()
        line_count+=1
        while line != '':
            try:
                line = line.rstrip()
                #Split and store employee information
                employee_list = line.split(',')
                first_name = employee_list[0]
                last_name = employee_list[1]
                dob = employee_list[2]
                #first or last name has numbers
                for ch in first_name:
                    if ch.isdigit():
                        has_digit_first = True
                    else:
                        has_digit_first = False
                for ch in last_name:
                    if ch.isdigit():
                        has_digit_last = True
                    else:
                        has_digit_last = False
                if has_digit_first == True or has_digit_last == True: #don't write, try next line
                    (f'Invalid data in line {line_count}. Skipping to next line ...')
                    line = infile.readline()
                    line_count+=1
                else: #continue with data processing
                    month = dob.split('/')[0]
                    day = dob.split('/')[1]
                    year = dob.split('/')[2]
                    #month, day, or year error
                    try:
                        if int(month)<1 or int(month)>12 or int(day)<1 or int(day)>31 or int(len(year))<4:
                            (f'Invalid data in line {line_count}. Skipping to next line ...')
                            line = infile.readline()
                            line_count+=1
                            #don't write, try next line
                        else: #continue with data processing
                            username = make_user_name(first_name,last_name,year)
                            password = make_password(dob, mywords)
                            #Write username and password to output file
                            outfile = open('login_info.txt','a')
                            outfile.write(f'{first_name} {last_name}\'s username is: {username} password is: {password}\n')
                            line = infile.readline()
                            line_count+=1
                    except ValueError: #don't write, try next line
                        print(f'Invalid data in line {line_count}. Skipping to next line ...')
                        line = infile.readline()
                        line_count+=1
            except IndexError:  #don't write, try next line
                print(f'Invalid data in line {line_count}. Skipping to next line ...')
                line = infile.readline()
                line_count+=1
        print('Username and password data successfully written to login_info.txt')

#Function that uses employee info to create a username
def make_user_name(first, last, year):
    LAST_NAME_MIN = 7
    NUM_LETTERS_MAX = 8
    first = first.lower()
    last = last.lower()
    #Convert last name to only letters
    for ch in last:
        if ch == "'":
            last = last.replace("'", '')
        if ch == '-':
            last = last.replace('-', '')
    #Create username based on last name length
    if len(last) >= LAST_NAME_MIN:
        username = first[0]+last[0:LAST_NAME_MIN]+year
    else:
        index_first = NUM_LETTERS_MAX-len(last)
        username = first[0:index_first]+last+year
    return username

#Function that uses employee info to create a password
def make_password(dob, mywords):
    word = mywords[random.randint(0,len(mywords)-1)]
    #Split dob into month, day, year
    dob_list = dob.split('/')
    #Convert month and day to two digits
    if len(dob_list[0]) < 2:
        dob_list[0] = '0'+ dob_list[0]
    if len(dob_list[1]) < 2:
        dob_list[1] = '0'+ dob_list[1]
    #Return password
    return dob_list[0]+word+dob_list[1]

main()
    
    
