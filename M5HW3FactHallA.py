# CTI 110
# M5HW3 Factorial
# Norris, A
# Hall. A
# 24 Oct 2017


#Calculating the factorial of a number


def main():

    for i in range(1,6):
        userInteger = int(input("Please enter a number: "))
        while userInteger < 1:
            userInteger = int(input("Please enter a positive number: "))

        factorial = 1
        
        for currentNumber in range( 1, userInteger + 1): 
            factorial = factorial * currentNumber


        print("The factorial of", userInteger, "is", factorial)




main() 
