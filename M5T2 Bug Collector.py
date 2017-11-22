# CTI 110
# M5T2
# Hall Airelle
# Mr. Norris
# 09 Oct 2017


# Write a program that tells how many bugs were collected each day

# The range will be one full week 7 days (range 1,8)

# Ask user to put how many number of bugs were collected.

def main ():
    week = range (1,8)
    totalBugs = 0
    for day in week:
        print ('day', day)
        bugs = int(input('Total Bugs on this day:'))
        # Update total bugs
        totalBugs = totalBugs + bugs
    

    # Print the total
    if totalBugs <= 0:
        print ('You havent collected any bugs this week')
    elif totalBugs >= 0:
        print ('You have collected:', totalBugs,'Bugs')

main ()

