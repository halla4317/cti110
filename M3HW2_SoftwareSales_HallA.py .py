# CTI 110
# Airelle Hall
# Norris. A
# 20 Sept 2017

#  Software Sales

#  Write a program that asks users for the numbers of packaged purchased
numberOfPackages = int(input('How many packages do you have?' ))

# Each package is $99.00
packagePrice = 99.00


if numberOfPackages < 10:
        discount = 0
elif numberOfPackages < 20:
        discount = 0.10
elif numberOfPackages < 50:
        discount = 0.20
elif numberOfPackages < 100:
        discount = 0.30
else:
        discount = 0.40

subTotal = numberOfPackages * packagePrice
discountAmount = discount * subTotal
total = subTotal - discountAmount

print ("\nYour discount is:$ " + format (discountAmount, " ,.2f")
        + "\nYour total is:$" + format (total, ",.2f"))


# Variables for quantity discount


# 10 - 19 10%
# 20 - 49 20%
# 50 - 99 30%
# 100 or more 40%






