from sys import exit
out = open("output.txt")
corr = open("correct.txt")



# prints out word and syllable level accuracy as well as misparsed words
def evaluate(output, correct):
    corrsyl = 0.0
    totsyl = 0.0
    totword = 0.0
    corrword = 0.0
    for oline, cline in zip(output, correct):
        totword += 1

        ophones = ''.join(oline.split()[1:])
        cphones = ''.join(cline.split()[1:])

        #eval exits if the number of syllables or lines don't match up
        if len(ophones) != len(cphones):
            print("the following lines don't match up - please check your syllabification:\n", oline, "\n", cline)
            exit()

        same = True
        osylls = ophones.split('+')
        csylls = cphones.split('+')
        #print osylls
        for os, cs in zip(osylls,csylls):
            #print '\t', os
            totsyl += 1
            if os == cs:
                corrsyl += 1
            else:
                same = False
        if same: corrword += 1
        else:
            print("Misparsed:\t", cphones, "\tas\n\t\t", ophones)

    print("syllable level accuracy is\t{:.6f}".format(corrsyl/totsyl))
    print("word level accuracy is\t\t{:.6f}".format(corrword/totword))


evaluate(out.readlines(),corr.readlines())
