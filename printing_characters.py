# Name: Jamaica C. Palillo
# Section: BSCPE 1-5

# Exercise 3: Print characters from a string that are present at an even index number.

# Create input to accept a string from user

input_word = str (input ("Enter a word: "))
len (input_word)

# Get only the characters present at an even index number
for i in range (len(input_word)):
    if (i % 2):
        print (input_word [i])


            

