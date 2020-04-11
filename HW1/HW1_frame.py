


#################
# Task 1
#################

## Michelle Vo
## Ling 191A Spring 2020
## HW 1

# Ask the user for a sentence:

sen = input("Please type a sentence:\n")

# Count words in the sentence
 
splitSentence = sen.split()
wordCount = len(splitSentence)
 
 
# Count occurrences of the letter 'e'

n_e = sen.count('e') 


# make sure to create an error message if the number is zero!  Do that here:

if n_e > 0:
    x = n_e

try:
  x
except:
  print("Error: There are 0 instances of 'e'")
  
# Print out what you found:

print("There were " + str(wordCount) + " words, and " + str(n_e) + " instances of the letter 'e' in \"" + str(sen) + "\"") 



#################
# Task 2
#################


# First, read in the file

f = open("shakespeare-hamlet.txt", "r") 
hamlet = f.read()
# Count words in the file:
hamletSplit = hamlet.split()
hamWordCount = len(hamletSplit) 

# Count number of e's in the file:
ham_e = hamlet.count('e') 

print("There are " + str(hamWordCount) + " words, and " + str(ham_e) + " instances of the letter 'e' in Shakespeare's Hamlet")    


######################
## Task 3
######################

ham = open("shakespeare-hamlet.txt", "r")

empty = []
characterList = []


for num, line in enumerate(ham.readlines()):
    hamletLine = line.strip() #strip whitespace each line
    splitHam = hamletLine.split()
    if splitHam != empty:
        character = splitHam[0]
        if "." in character:
            if character not in characterList:
                characterList.insert(num, character)
            
            
## print(characterList)
print(len(characterList))








 