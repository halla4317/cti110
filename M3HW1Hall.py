# cti 110
# M3HW1Hall - Age Clasifier
# halla
# 20 Sept 2017


# Ask for the age of the User
# If the User is less then 1 it will print out Infant
# If the User is less then 13 it will print out Child
# If the User is more then 13 but less then 20 it will print out Teenager
# If the User is older then 20 it will print out adult

userAge = input('What is your age?')

# Variables

userAge = int (userAge)

# Commands to Execute

if userAge <= 1:
    print ('You a baby...')
elif userAge <= 13:
    print ('You must be a child. Stay off my damn computer')
elif userAge <= 20:
    print ('Wassup Young boi or girl, you gotta be a teenager')
elif userAge >= 20:
    print ('You grown as hell')
    




