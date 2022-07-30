###     Module3 Price Of FiberOpticCable per foot Calculator        ###

# import the .math fuction
import math
# Display Welcome Message
welcomeMessage = "Welcome to the price calculator per foot of Fiber Optic Cable"
print(welcomeMessage)
print()

# Get the Company name from the User
companyName = input("Enter the name of your Company")

# Get the ammount of Fiber Optic Cable (ammountFOC) in feet 
# Make the ammoundFOC an INT by using the int(), and abs() functions
# # Author: Ryan Reyes (github.com/TechProofreader)
# Program Name: Materials Calculator Script
# Version: 1.0

ammountFOC = int(input("Please enter the ammount of Fiber Optic Cable needed in 'Feet'.\nPleases use whole numbers only."))

# Multiply input(ammountFOC) by .87 cents
totalPrice = abs(ammountFOC * 1.87)

# Display the totalPrice and the Company name
# Convert int(totalPrice) to str(totalPrice), then concatenate with companyName
# Found this through ---- askpython.com/python/string/pythion-concatenate-string-and-int  ----
# Also found the f" string {str} and then some number {int}"...
# ...did the same thing as converting the integer into a string with str()
# f string is accreditted to  ---- realpython.com/python-f-strings/  ----
finalMessage = f"Hello {companyName}\nThe total for your project before taxes is going to run you about ${totalPrice} dollars"
print()
print(finalMessage)
