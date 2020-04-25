
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




#syllabify takes as input a list of phonemes, and outputs a astring where the syllables
# are separated by +
def syllabify(raw):
    
    raw = raw.strip()
    raw = raw.split()
    syllabified = []#initialize a list to hold the syllabified word
    onset = []
    coda = []
    nuclei = []
 
    onsetMax = 0;
    syllable = []## consonants can be added to onset as long as their son diff is 2+
    for n in raw:
        #check each element if it exists in in our sonorant dict
        if (n not in son):
            syllabified.append(n)
        elif (n in son):
            syllable.append(n)
            ### If the element is a phoneme we recognize. 
            level = son.get(n)
            
            if level == 4 and coda != []:
                ## we've got a syllable so pop that onto the return list.
                syllabified.append(syllable)
                syllabified.append("+")
                ## Reset everything..
                syllable = []
                onset = []
                coda = []
                nuclei = [] 
                continue; 
                
            if level == 4 and coda == []: ## We got a value
                nuclei.append(n)
               
                continue
            if onset == [] or nuclei == []: # first consonant
                onset.append(n)
                onsetMax = level
                
                continue
            elif onset != [] and coda == []: 
                if (level - onsetMax >= 2): 
                    if (n == 'S'):
                        coda.append(n)
                        continue
                    else:
                        onset.append(n)
                        onsetMax = level - onsetMax 
                    continue
                else:
                    coda.append(n)      
                    
                    #coda no longer empty so we close onset.
            
                
                    ## add the consonant to coda. 
                
    
    return(syllabified)
            
            
            ## if element in raw is in Son, then 
            ## calculate the Onset (initial consonants.)
            ## calculate the Coda
            ## Nuclei are all vowel sounds sonority 4
            ## AH B 
            ## ZAORP
            ## SH AH N 
            ## three syllables here. 
            
     




###########
# Task 2
###########

    
# Read in test.txt, syllabify each line, and write out output.txt