######################## James Bailey Module 8 Miles to Kilometer ########################

#Function to convert miles to kilometers
def converter(miles):
    km = (miles) * 1.6
    return km
milesToConvert = int(input("Enter the Miles to your destination \nwe'll convert it to kilometers for a round trip"))

# Convert milesToConvert to kilometers by calling the function above

# Display the result of the function
# Only if the input is a numerical value greater than zero
if milesToConvert > 0:
    try:
        kilometers = converter(milesToConvert)
    except ValueError:
        print("Please enter a number.")
    else:
        print("The distance in kilometers is " + str(kilometers))
else:
    print("Try using a number bigger than '0'!")
# Calculate the round-trip in kilometers by doubling the result,
# Display the result
try:
    roundTrip = kilometers + kilometers
except NameError:
    print("No number greater than 0.")
try:
    print("The round-trip in kilometers is " + str(roundTrip))
except NameError:
    print("I have nothing to do without a number")
