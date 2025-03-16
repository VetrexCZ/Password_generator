# Python Password generator !

import random

lower = "abcdefghijklmnopqrstvuwxyz"    # All the strings that will be used to generate the password
upper = "ABCDEFGHIJKLMNOPQRSTVUWXYZ"
symbol = "()[]{};_#*._"
number = "0123456789"

assembly = lower + upper + number + symbol  # assembly of all the strings
length = 10 # Password length                                                                   
password = "".join(random.sample(assembly, length)) # Randomly select the strings from the assembly

print("-" * 33)
print(f"The new generated password is: {password}")
print("-" * 33) 