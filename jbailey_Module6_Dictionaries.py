###     James Bailey CSD-250 Module 6 Dictionaries. (Due April 10th, 2022)      ###

## Create 10 different Key:Value pairs. Display all of the Key, and ask user to select one to display it's Value ##

# Key: Value Pairs
horrorIcons =    {
    'jack torrens' : 'the shining',
    'carrie white' : 'carrie',
    'annabelle' : 'annabelle',
    'ghostface' : 'scream',
    'regan mcNeil' : 'the exorcist',
    'charles lee ray' : "child's play",
    'michael myers' : 'halloween',
    'kandarian demons' : 'evil dead',
    'xenomorph' : 'alien',
    'annie wilkes' : 'misery',
    'pennywise' : 'IT',
    'pinhead' : 'hellRaiser',
    'hannibal lecter' : 'silence of the lambs',
    'babadook' : 'babadook',
    'candyman' : 'candyman',
    'samara morgan' : 'the ring',
    'norman bates' : 'psycho',
    'leatherface' : 'texas chainsaw massecacre',
    'damien' : 'the omen',

}
# Loop through the dictionary and print all of they keys
for character in horrorIcons.keys():
    print(character.title())
    
# let the user choose one of the keys from the list and type it in a new variable
userChoice = input("Chose one of the names to find what film they came from")
choice = str(userChoice)
if userChoice.lower() in horrorIcons.keys():
    #print(horrorIcons[choice])
    #############################It seems all I was missing as the .lower() at the end of my new variable given by the User Input's Choice. SERIOUSLY I WAS THAT CLOSE!!??#########################
    print(horrorIcons[userChoice.lower()])
# find the user input against the keys in the dictionary, then print that key's value.

### Been at it, researching for over 8 hours. I don't believe this to be in the course material. Not Happy!

else:
    print("\n\nI can't find it.")