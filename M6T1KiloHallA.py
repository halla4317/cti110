# CTI 110
# M6T1: Kilometer Converter
# Norris, A
# Hall, A
# 25 Oct 2017

# Write a program that asks the user to enter a distance in Kilometers
# Conversion formula: miles = kilometers * 0.6214

conversion_factor = 0.6214

#Ask User for Distance in Kilometers
def main():
    kilometers = float(input('Enter a distance in kilometers: '))

# Variable for Kilometers
    show_miles(kilometers)

# Define function for show_miles

def show_miles(km):
    miles = km * conversion_factor

# Print output of kilometers conerted to miles
    print (km, 'kilometers equals',miles,'miles.')

main()

