import os, math, nltk
from nltk.stem import WordNetLemmatizer

inp = open('en_full_2.txt')
outp = open('en_out_2.txt', 'w')
# outp_2 = open('en_out_2.txt', 'w')
# outp_full = open('en_full_2.txt', 'w')

for line in inp:
    line = line.split(' ')
    x = (22484400 - int(line[1])) / 22484400
    y = pow(x, 50)
    outp.write(line[0] + ' ' + str(y) + '\n')




# nltk.download('punkt')
# nltk.download('wordnet')
# word_net_lemma = WordNetLemmatizer()
# dictInp = dict()
# for line in inp:
#     line = line.split(' ')
#     sentence_words = nltk.word_tokenize(line[0])
#     word_list = [word_net_lemma.lemmatize(x, pos="v") for x in sentence_words]
#     # print(word_list)
#     line[0]=str(word_list[0])
#     if line[0] is not "":
#         if line[0] in dictInp : 
#             dictInp[line[0]]+=int(line[1])
#         else : dictInp[line[0]]=int(line[1])

# dictInp = dict(sorted(dictInp.items(), key=lambda item: item[1], reverse=True))

# for k in dictInp:
#     outp_full.write(k + ' ' + str(dictInp[k]) + '\n')

# for k in dictInp:
#     x = (22484400 - int(dictInp[k])) / 22484400
#     y = pow(x, 50)
#     outp.write(k + ' ' + str(y) + '\n')

# outp_2.close()
# outp_full.close()
outp.close()
inp.close()


