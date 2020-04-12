import sys


fout = open("output.txt", "w")
fin = open("input.txt", "r")

n = int(fin.readline())

d = []*n
c = []*n
z = []*n

i = 1
while ( i <= n ):
    text = fin.readline()
    words = text.split()
    wordcount = len(words)
    # print('Wordcount:', wordcount, words )
    d.append(words[0])
    c.append(int(words[1]))
    kolz = int(words[2])
    z.append(kolz)
    print('Word:', d, c, z )
    print('\n')
    iz =1
    while iz <= kolz:
        text = fin.readline()
        print(iz, 'z  = ', text)
        iz += 1

    i += 1
    # читаем кол ингридиентов
k = int(fin.readline())
ik = 1
while ik <= k:
    text = fin.readline()
    print(ik, 'k text = ', text)
    ik += 1
m = int(fin.readline())
im = 1
while im <= m:
    text = fin.readline()
    print(im, 'm text = ', text)
    im += 1
fout.close()
fin.close()
