"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
MINIMUN_CHARGE = 35.00

# Character costs
FREE_LETTER_COUNT = 5
EXTRA_CHAR_CHARGE = 4.00
GOLD_LEAF_CHAR = 15.00

# Wood Costs
OAK_WOOD_CHARGE = 20.00

# User Imput
numChars = int(input("Enter the number of characters in the sign: "))
woodType = input("Enter the type of wood ('oak' or 'pine'): ").lower()
color = input("Enter the color of the characters ('gold', 'black', or 'white'): ").lower()

charge = MINIMUN_CHARGE

# Write assignment and if statements here as appropriate.

# Calculate extra charges for more than included five
if numChars > FREE_LETTER_COUNT:
  charge += (numChars - FREE_LETTER_COUNT) * EXTRA_CHAR_CHARGE

# Check if user wants oak wood
if woodType == "oak":
  charge += OAK_WOOD_CHARGE

# Check if user wants gold leaf characters
if color == "gold":
  charge += GOLD_LEAF_CHAR

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
