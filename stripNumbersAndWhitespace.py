#!/usr/bin/python
import sys

# Utility to strip numbers and whitespace from a text file

# Open the input file (passed as the argument to the script)
with open(sys.argv[1]) as f:
  words = f.readlines()

cleanedwords = []
for wordunstripped in words:
  wordnodigits = ''.join(i for i in wordunstripped if not i.isdigit())
  word = wordnodigits.strip()
  print(word)
  cleanedwords.append(word)

cleanedwords.sort()

# Output the key phrases to a text file.
with open("cleanedInput.txt", "w") as text_output:
  for cleanedword in cleanedwords:
    line_out = cleanedword + "\n"
    text_output.write(line_out)

# exit with success message
print ("Created a list of words with " + str(len(cleanedwords)) + " entries.")
