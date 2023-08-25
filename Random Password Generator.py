# Random Password Generator
import random

# Set the base data
lowerCase = "abcdefghijklmnopqrstuvwxyz"
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "01234567890"
symbols = "{}[]_-!@#$%^&*()?<>;"

# Merge data into one variable
all = lowerCase + upperCase + numbers + symbols

# Password setting - length and space between characters
length = 10
bufferVariable = ""

password = bufferVariable.join(random.choice(all) for a in range(length))

print(password)

