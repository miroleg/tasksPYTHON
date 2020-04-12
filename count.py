import sys
stroka = sys.argv[1]
bukva = sys.argv[2]
#print (stroka,bukva)
last_pos = 0
pos_bukva = 0
kol_bukv = 0
while pos_bukva >= 0:
    pos_bukva =stroka.find(bukva,last_pos)
    if pos_bukva >= 0:
        #print(pos_bukva)
        kol_bukv += 1
        last_pos = pos_bukva + 1
else:
    print (kol_bukv)
