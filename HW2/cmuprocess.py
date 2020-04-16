
## Ling 191A Spring 2020
## Michelle Vo
## Homework 2 


################
# Task 2
################

cmu = {}
empty = list()

# orthography is key
# transcription is value, as a list of phonemes. 

cmudict = open("cmudict.txt", "r") 

for line in cmudict.readlines(): 
     cmuLine = line.strip()
     splitCMUList = cmuLine.split()
     if splitCMUList != empty: # nonempty line
         orthography = splitCMUList[0]
         if ";;;" in orthography:
             continue
         else: 
             # first item is a word.
             if orthography not in cmu:
                 value = splitCMUList[1:] #gets whole list except head. 
                 cmu[orthography] = value 
               

## Task 2 Test Cases:
                 
print(cmu['ZYLKA'])
print(cmu['WHITEN(1)'])
print(cmu['CRUMB'])

################
# Task 3
################

subtlexList = []

subtlex = open("subtlexUS.txt", "r")
for line in subtlex.readlines():
    subtlexLine = line.strip()
    splitSubtlexList = subtlexLine.split()
    word = splitSubtlexList[0]
    subtlexList.append(word.upper()) #populates subtlex with uppercase words
   

for word in list(cmu.keys()):
    if word not in subtlexList:
        cmu.pop(word)  
     


## Task 3 Test Cases

keys = sorted(cmu.keys())[0:9]
print(*[str(x)+": "+str(cmu[x]) for x in keys],sep='\n')

keys = sorted(cmu.keys())[-10:-1]
print(*[str(x)+": "+str(cmu[x]) for x in keys],sep='\n')





#############
# Task 4
#############

entries = sorted(cmu.keys())

                    
baddies = []
for entry in entries:
    baddies.append(entry+"S")
    baddies.append(entry+"ES")
    baddies.append(entry+"ING")
    baddies.append(entry+"ED")
    baddies.append(entry+"D")
    # Your code here

for baddie in baddies:
    if baddie in cmu:
        cmu.pop(baddie)



## Task 4 Test 
keys = sorted(cmu.keys())[-11010:-11000]
print(*[str(x)+": "+str(cmu[x]) for x in keys],sep='\n')


################
# Task 5
################

# import re
# It is probably technically possible to do this task without re, but it will be easier with it

vowels = ["AA","AE","AH","AO","AW","AY","EH","ER","EY","IH","IY","OW","OY","UH","UW"]
# You might need these. 
# NOTE! you'll have to strip out the numbers that occur after every vowel in CMU's transcription

onsets = {}
codas = {}


## isVowel helper function checks if element is a vowel

def isVowel(element):
    return ("0" in element or "1" in element or "2" in element or element in vowels)


for entry in cmu.keys(): 
    transcription = cmu[entry]  
    onset = ""
    coda = ""
    ## Compute the Onset
    for h_element in transcription:
        if isVowel(h_element):
            if onset in onsets:
                onsets[onset] = onsets[onset] + 1 
            else:
                onsets[onset] = 1; #add onset to the dictionary.
            break
        
        onset += h_element
    ## Compute the Coda
    for t_element in reversed(transcription):
        if isVowel(t_element):
            if coda in codas:
                codas[coda] = codas[coda] + 1
            else:
                codas[coda] = 1; #add coda to the dictionary
            break
        coda = t_element + coda
        



        
#onset is a substring until the first value is met. 
# Onsets are sequences of consonants before the first vowel of a word
# Codas are sequences of consonants after the last vowel. 
# onsets[onset] = count
# codas[coda] = count 




print(codas["LD"]) # Should be 144
print(codas["NT"]) # Should be 789
print(codas["RK"]) # Should be 49
print(onsets["TR"])  # should be 354
print(onsets["SPL"]) # should be 18
print(onsets["SKR"]) # should be 59


# At the end you should get:
# 144 occurrences of 'ld' as a coda
# 789 occurrences of 'nt' as a coda
# 49  occurrences of 'rk' as a coda
# 59  occurrences of 'skr' as an onset
# 18 occurrences of 'spl' as an onset
# 354 occurrences of 'tr' as an onset


## Note that in the homework's test case for Task 4, the Stress numbers have been removed, and in Task 3 they are not.
## My implementation does not remove the numbers from the transcription (and that is not asked of by the spec). 
## Instead, when computing coda or onset, I break off the element when a vowel or stress digit is encountered. 



## This implementation prints the desired output. 







