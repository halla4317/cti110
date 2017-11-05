# CTI 110
# M5HW2: Running Total
# Norris. A
# Hall, A
# 19 Oct 2017

# Write a program that asks the user to calculate student's total
# Variable
def main():
    total = 0
    score = 0

    # Command For Input of Numbers and Command for Total
    for i in range (4):
        repeat = True
        while repeat:
            score = int (input('Next Score: '))
            if score < 0:
                repeat = False
            else:
                totalScore = total + score
        print ('Total is: ', totalScore)

main()




    
