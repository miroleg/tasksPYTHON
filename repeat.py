import sys
strok = sys.argv[1]
kol_repeat = int(sys.argv[2])
#print (stroka,kolrepeat_)
st_povt = ""
while kol_repeat > 0:
    st_povt = st_povt + strok
    kol_repeat -= 1
else:
    print (st_povt)
