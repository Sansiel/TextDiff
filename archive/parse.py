import os

inp = open('lemmas.txt')
D = {}
for line in inp:
    linelist = line.split(' ')
    linelist[1] = int(linelist[1])
    D[linelist[0]] = linelist[1]

inp.close()


dirin = 'texts'
dirout = 'textsout'
txtlist = os.listdir(dirin)
for text in txtlist:
    inp = open(dirin + '\\' + text)
    outp = open(dirout + '\\' + text, 'w')
    words = 0
    summ = 0
    wordsall = 0
    wordsnum = 0
    for line in inp:
        line = line.lower()

        line = line.replace(',', '')
        line = line.replace('.', '')
        line = line.replace('\n', '')
        line = line.replace('(', '')
        line = line.replace(')', '')
        line = line.replace('\t', ' ')

        linelist = line.split(' ')
        wordsall += len(linelist)

        for word in linelist:
            if word.isalpha():
                wordsnum += 1

                if word.endswith('ed'):
                    word = word[:len(word) - 2]

                if word.endswith("'s") or word.endswith("s'"):
                    word = word[:len(word) - 2]

                if word.endswith('s'):
                    if word[:len(word) - 1] in D:
                        summ += pow(D[word[:len(word) - 1]], 2)
                        words += 1


                elif word in D:
                    words += 1
                    summ += pow(D[word], 2)

    x = summ / words / 1000000
    inp.close()
    outp.write(str(x)[:4] + '\n' + str(wordsall) + '\n' + str(wordsnum) + '\n' + str(words) + '\n')
    outp.close()
    
    
#print(x)
#print(wordsall)
#print(wordsnum)
#print(words)