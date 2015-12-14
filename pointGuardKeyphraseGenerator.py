#!/usr/bin/python
import sys

# Utility to create a set of memorable 10-letter phrases with no duplicate 
# letters, using any list of words as input. These phrases can be used as 
# keys in a simple cipher for numerical combinations.

# Based on a system invented by Donald McLeod Vince Gayton Sr., my great-
# grandfather, to document the combination locks on his luggage, and passed
# down through four generations to me.

# Open the input file (passed as the argument to the script)
with open(sys.argv[1]) as f:
  words = f.readlines()

# Create a list of 5-letter words with no duplicate letters
cleanedwords = []
for wordunstripped in words:
  word = wordunstripped.strip()
# TODO strip punctuation (apostrophes are sneaking through)
  if len(word) > 4 and len(word) < 6:
    letters=list(word)
    if len(letters) == len(set(letters)):
      cleanedwords.append(word)

# Iterate through the list of cleaned words and add a second word with no
# duplicates. This creates a 10-letter phrase with no duplicate letters.
keyphrases = []
for word in cleanedwords:
  for secondword in cleanedwords:
    letters = list(word)
    letters.extend(list(secondword))
    if len(letters) == len(set(letters)):
      keyphrases.append (word + " " + secondword)
print len(keyphrases)

# Output the key phrases to a text file.
with open("keyphrases.txt", "w") as text_output:
  for keyphrase in keyphrases:
    line_out = keyphrase + "\n"
    text_output.write(line_out)

# exit with success message
print ("Created a list of key phrases with " + str(len(keyphrases)) + " entries.")
