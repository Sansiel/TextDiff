import os, math
from pymystem3 import Mystem

inp = open('en_out.txt')
D = {}
for line in inp:
    linelist = line.split(' ')
    linelist[1] = float(linelist[1])
    D[linelist[0]] = linelist[1]

inp.close()


dirin = 'texts'
dirout = 'textsout'
txtlist = os.listdir(dirin)
mystem = Mystem()
for text in txtlist:
    words = 0
    summ = 0
    inp = open(dirin + '\\' + text)
    outp = open(dirout + '\\' + text, 'w')

    text = ''.join(inp.readlines())
    wordlist = mystem.lemmatize(text.lower())
    lemmas = [x for x in wordlist if x.isalpha() and x in D]

    for lemm in lemmas:
        summ += D[lemm]
        words += 1

    x = summ / pow(words, 0.98) * 100
    inp.close()
    outp.write('\n' + str(x) + '\n')
    outp.close()
    