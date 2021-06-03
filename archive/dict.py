import os, math

inp = open('en_full.txt')
outp = open('en_out.txt', 'w')

for line in inp:
    line = line.split(' ')
    x = (22484400 - int(line[1])) / 22484400
    y = pow(x, 50)
    outp.write(line[0] + ' ' + str(y) + '\n')

outp.close()
inp.close()


