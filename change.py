# Author: Ruben Hernandez
# GitHub username: hernrube
# Date: 7/04/2024
# Description: Asks the user for a number in cents and
#              output prints how many of each coin it will be.
print("Please enter an amount in cents less than a dollar.")
num=int(input())
quarter=num//25
dime=num%25//10
nickel=num%25%10//5
penny=num%25%10%5//1
print("Your change will be:")
print("Q:", quarter)
print("D:", dime)
print("N:", nickel)
print("P:", penny)


