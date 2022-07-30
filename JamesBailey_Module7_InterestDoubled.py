####    JAMES BAILEY MODULE 7 INTEREST DOUBLED      ####

###########################                 Third Attempt                   ############################
# Initial investment = i = 0
#i = 0
# final investment = f = 0
#f = 0
# interest reate = r = 0.0
#r = float(0.0)
# total count of years = y = 0
#y = int(0)
# get initial investment
#i = float(input("Enter initial investment"))
# get interest rate
#r = float(input("Enter interest rate as 0.xx"))

#finish_loop = f >= i * 2


#while finish_loop:
#    f = i * r
#    y = y + 1
#print(f"Your initial investment of ${i} will take {y} Years to double. At which point it will be ${f}.")



######################              First Attempt               ######################################
# Set variables for prompts

prompt = "Enter intial investment"
prompt2 = "Enter interest rate as : 0.xx"

# Set an empty variable for initialInvestment
initialInvestment = float(0)

# Set an empty variable for interestRate
interestRate = float(0.0)

# Set an empty variable to countYears
countYears = float(0.0)

# Ask User for the amount of their initialInvestment
initialInvestment = input(prompt)

# Ask User for the interRate of their initialInvestment
interestRate = input(prompt2)

# Convert interestRate and initialInvestment
initialInvestment = float(initialInvestment)
interestRate = float(interestRate)

# Set an empty variable for finalInvestment
finalInvestment = initialInvestment * int(2)

# Create While loop that sets a maximum value for finalInvestment to stop at initialInvestment * 2
while initialInvestment <= finalInvestment:
    initialInvestment = initialInvestment * interestRate +  finalInvestment
    countYears = countYears + 1
print(f"It will take {countYears}Years to double your investment of ${initialInvestment} to a total of ${finalInvestment}.")



############        Second Attempt     #################################
#initialInvestment = int(0)
#interestRate = float(0.0)
#finalInvestment = int(0)
#initialInvestment = int(input(prompt))
#countYears = int(0)
#interestRate = float(input(prompt2))
#while True:
#    if finalInvestment >= initialInvestment * int(2):
#        print(f"It will take {countYears} Years to double your investment of ${initialInvestment} to a total of ${finalInvestment}.")
#    else:
#        finalInvestment = initialInvestment * interestRate
#        countYears = countYears + 1
