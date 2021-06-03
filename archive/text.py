inp = open(r'C:\Users\Neocsis\Desktop\test.txt')
outp = open(r'C:\Users\Neocsis\Desktop\lemmas.txt', 'w')
for line in inp:
    linelist = line.split(' \t')
    outp.write(linelist[1][3:] + ' ' + linelist[3] + '\n')
# inp = open('en_out.txt', encoding='utf-8')
# D = {}
# for line in inp:
#     linelist = line.split(' ')
#     linelist[1] = float(linelist[1])
#     D[linelist[0]] = linelist[1]

# inp.close()
# print(D)