###    James Bailey Module 4 Tuples April 03, 2022   ###


horrorIcons = ("Jack Torrance", "Jason Vorhees", "Carrie White", "Annabelle", "Ghostface", "Regan MacNeil", "Charles Lee Ray", "Michael Myers", "Kandarian Demons", "Xenomorph", "Annie Wilkes", "Pennywise", "Pinhead", "Hannibal Lecter", "Babadook", "Candyman", "Samara Morgan", "Norman Bates", "Leatherface", "Damien",)

print(horrorIcons)
print()
for Icons in horrorIcons:
    print(f"Do you know {Icons.title()}?\n")
print()
i = len(horrorIcons) -1
while i >= 0 :
    print(f"If you haven't guessed, {horrorIcons[i]} is a Horror Movie Icon!\n")
    i -= 1


