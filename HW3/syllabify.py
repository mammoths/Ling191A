import re

############
# Task 1
############


son = { 'AA': 4, 'AE' : 4, 'AH' : 4, 'AO' : 4, 'AW' : 4, 'AY' : 4,
             'B'  : 0, 'CH' : 0, 'D' : 0, 'DH' : 0, 'EH' : 4, 'ER' : 4,
             'EY' : 4, 'F': 0, 'G': 0, 'HH': 0, 'IH': 4, 'IY': 4, 'JH': 0,
             'K': 0, 'L': 2, 'M': 1, 'N': 1, 'NG': 1, 'OW': 4, 'OY': 4,
             'P': 0, 'R': 2, 'S': 0, 'SH': 0, 'T': 0, 'TH': 0, 'UH': 4,
             'UW': 4, 'V': 0, 'W': 3, 'Y': 3, 'Z': 0, 'ZH': 0}


testFile = open("test.txt", "r")  
tester = testFile.readline()

## Make a new list that just equates to one input string.

def Reverse(lst): 
    lst.reverse() 
    return lst 


#syllabify takes as input a list of phonemes, and outputs a astring where the syllables
# are separated by +
def syllabify(raw):
    
    raw = raw.split()
    

    
    syllabified = []#initialize a list to hold the syllabified word
    onset = []
    coda = []
    nuclei = []
    onsetMax = 0;
    syllable = [] 

    for n in reversed(raw):
        #check each element if it exists in in our sonorant dict
        if (n not in son):
            syllabified.append(n)
            continue
            ## add it to the list anyway.
        elif (n in son):
            ### If the element is a phoneme we recognize
            level = son.get(n)
            if (level == 4 and coda == []):
                ## Our syllable ends in a vowel, no coda. 
                nuclei.append(n)
                syllable.append(n)
                
                syllabified.append(Reverse(syllable))
                
                syllable = []
                nuclei = []
                continue
            elif (level == 4 and coda != []):
                 nuclei.append(n)
                 syllable.append(n)
                 syllabified.append('+')
                 syllabified.append(Reverse(syllable))
                 
                 syllable = []
                 continue                 
            elif (level != 4):
                #  Our consonant. 
                # if nucleus is empty during this encounter..
                if (nuclei == []):
                    coda.append(n)
                    syllable.append(n)
                    continue
                elif (nuclei != []):
                    if (level - onsetMax >= 2):
                        onset.append(n)
                        onsetMax = level 
                        syllable.append(n)
                        continue
                    else:
                        syllable.append(n)
                        syllabified.append(Reverse(syllable))
                        #
                        syllable = []
                        
                        coda = []
                        coda.append(n)
                        nuclei = []
                        onset = []
            else:
                 syllabified.append(Reverse(syllable))
                # syllabified.append('+')
                 syllable = []
                        
                 coda = []
                 coda.append(n)
                 nuclei = []
                 onset = []
                
    if (syllabified[0] == '+'):
        syllabified.pop(0)
         #extraneous + sign.
    
    
    
    return(Reverse(syllabified))
            
     


###########
# Task 2
###########

testFile = open("test.txt", "r") 
output = open("output.txt", "w")
for line in testFile.readlines():
  
    result = str(syllabify(line))
    
    
    result = result.replace(',' , '')
    result = result.replace('[' , '')
    result = result.replace(']' , '')
    
   
    
    res = str(result)[1:-1] 
    res = res.replace("'", "")
    res = res.replace('"', "")
   
    
    output.write(str(res) + '\n')
    
    
    
    
    ## now output result to output.txt
    
    
# Read in test.txt, 

#syllabify each line, and write out output.txt
    






