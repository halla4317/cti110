# I was supposed to put a comment here
# My Last Name

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
    F_score = 0
    # TO DO: define the rest of the scores

    
    score = int(input('Enter grade: '))
    

    if score >= A_score:         
        print('Your grade is: A! You did great...have you been studying?')
    else:
        if score >= B_score: 
            print('Your grade is: B! Not bad at all Ms Smith.')
        else:
            if score >= C_score:
                print('Your grade is: C, I think you can do better')    
            else:
                if score >= D_score:
                    print('Your grade is : D..a damn D..Linx said What the fuck! ')
                else:            
                    print('Your grade is: F...Are you  fucking kidding me?') # TO DO: finish this

            







# program start
main()
