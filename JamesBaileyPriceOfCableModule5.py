###     Module3 Price Of FiberOpticCable per foot Calculator        ###

# import the .math fuction
import math
# Display Welcome Message
welcomeMessage = "Welcome to the price calculator per foot of Fiber Optic Cable"
print(welcomeMessage)
print()

# Get the Company name from the User
companyName = input("Enter the name of your Company")

# Get the ammount in Feet Of Cable that is needed

ammountFOC = int(input("Please enter the ammount of Fiber Optic Cable needed in 'Feet'.\nPlease use whole numbers only."))

# Find the totalDiscount to give depending on the ammountFOC needed and multiply
if ammountFOC <= 100:
    totalDiscount = 1.8
elif ammountFOC <= 250:
    totalDiscount = 1.7
elif ammountFOC <= 500:
    totalDiscount = 1.5

totalPrice = abs(ammountFOC * totalDiscount)

# Display the totalPrice and the Company name
# Convert int(totalPrice) to str(totalPrice), then concatenate with companyName
# Display ammountFOC needed
# Display totalPrice
# Display message including companyName, ammountFOC and totalPrice
finalMessage = f"Hello {companyName}\nThe total ammount of cable you have chosen is, {ammountFOC}feet.\nThe total for this purchase before taxes, will run you about ${totalPrice} dollars."
print()
print(finalMessage)
