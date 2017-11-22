# This program should display a letter grade for 5 test grades and the average test score
# 4 Nov 2017
# CTI-110 M6HW1-Test Average and Grade
# Hall, A


def main (): #Def Function

# This is function that will ask for score and will return letter grade
    total = 0
    for times in range(1,6):
        score = int(input('Whats your score:'))
        
        total += score
    

    average = calc_average(total)

    print ('Your  average is:', average ,'and your letter grade is', (determine_grade(score)))
# Function will average out the 5 scores
def calc_average(score):
    return score / 5

# Function will determine the grade and print out grade after determining decimal
def determine_grade(grade):
    if 90 <= grade <= 100:
        return ('Your grade is A')
    elif 80 <= grade <= 89:
        return ('Your grade is B')
    elif 70 <= grade <= 79:
        return ('Your grade is C')
    elif 60 <= grade <= 69:
        return ('Your grade is D')
    elif 0 <= 59:
        return ('Failed')

    


main()
    
