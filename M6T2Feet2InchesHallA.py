# This command will convert feet to inches
# 30 Oct 2017
# CTI 110 FeetToInches_Hall
# Hall, A
# Norris, A

# Varibale for inches

inchesFoot = 12

# Commands for finding feet to inches

def main():
    feet = int(input('Enter a number of feet:'))
    print (feet, 'equals', feet_to_inches(feet), 'inches.')

def feet_to_inches(feet):
    return feet * inchesFoot

main()



  



