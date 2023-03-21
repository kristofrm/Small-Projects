#Kristof Rohaly-Medved
#CS21
#Program to process grades from a file and write data to output files

#Function that reads input file data and writes output file data
def main():
    infilename = get_file_name('grade input')
    try:
        grade_infile = open(infilename, 'r')
    except IOError:
        print('Could not open input file. Exiting now ...')
    else:
        outfilename = get_file_name('outputting individual student grades')
        report_filename = get_file_name('grade report')
        
        #Initiate histogram counters
        As = 0
        Bs = 0
        Cs = 0
        Ds = 0
        Fs = 0
        
        #Initiate highest/lowest grade counters
        lowest_grade = 100
        highest_grade = 0
        
        #Initiate counters to calculate average overall grade later
        total_grade = 0
        grade_count = 0
        
        #Initiate loop that reads, processes, and outputs grade information
        NUM_TESTS = 6
        line = grade_infile.readline()
        try:
            while(line != ''):
                score = 0
                possible = 0
                student = line.rstrip()
                
                #Get scores for all 6 tests
                for count in range(NUM_TESTS):
                    score += int(grade_infile.readline())
                    possible += int(grade_infile.readline())
                    
                #Calculate and output letter grade to outfile
                grade = (score/possible)*100
                letter_grade = determine_grade(grade)
                grade_outfile = open(outfilename, 'a')
                grade_outfile.write(f'{student} {letter_grade}\n')
                
                #Add letter grade to histogram count
                if letter_grade == 'A':
                    As += 1
                elif letter_grade == 'B':
                    Bs += 1
                elif letter_grade == 'C':
                    Cs += 1
                elif letter_grade == 'D':
                    Ds += 1
                elif letter_grade == 'F':
                    Fs += 1
                    
                #Run letter grade through highest/lowest grade checker
                if grade > highest_grade:
                    highest_grade = grade
                elif grade < lowest_grade:
                    lowest_grade = grade
                    
                #Update values for calculating overall average grade
                total_grade += grade
                grade_count += 1
                
                #Read line for next student name
                line = grade_infile.readline()

            #Close letter grade output file
            grade_outfile.close()
        
        except ValueError:
            print(f'Invalid data found in {line.rstrip()}\'s file. Creating grade reports with existing data ...')
        else:
            #Write grade stats to grade report output file
            try:
                report_outfile = open(report_filename, 'a')
            except IOError:
                print('Could not open grade report output file. Exiting now ...')
            else:
                try:
                    average_grade = total_grade/grade_count
                    report_outfile.write(f'Highest grade: {highest_grade:.1f}\n')
                    report_outfile.write(f'Lowest grade: {lowest_grade:.1f}\n')
                except ZeroDivisionError:
                    print('Average could not be calculated.')
                    report_outfile.close()
                else:
                    report_outfile.write(f'Average grade: {average_grade:.1f}\n')
                    for n in range(3):
                        report_outfile.write("\n")
                    report_outfile.write(f'HISTOGRAM\n')
                    report_outfile.close()

                    #Write histogram data to grade report output file
                    histogram('A', As, report_filename)
                    histogram('B', Bs, report_filename)
                    histogram('C', Cs, report_filename)
                    histogram('D', Ds, report_filename)
                    histogram('F', Fs, report_filename)
        
#Function that gets and returns file name inputs
def get_file_name(label):
    filename = input(f'What is the name of the file to use for {label}? ')
    return filename

#Function that returns corresponding letter grade from numeric grade
def determine_grade(grade):
    if grade >=90:
        letter = 'A'
    elif grade < 90 and grade >= 80:
        letter = 'B'
    elif grade < 80 and grade >= 70:
        letter = 'C'
    elif grade < 70 and grade >= 60:
        letter = 'D'
    elif grade < 60:
        letter = 'F'
    return letter

#Function that writes histogram data to the grade stats output file
def histogram(category, count, outname):
    report_outfile = open(outname, 'a')
    report_outfile.write(f'{category}: ')
    for i in range(count):
        report_outfile.write('*')
    report_outfile.write('\n')
    report_outfile.close

main()
