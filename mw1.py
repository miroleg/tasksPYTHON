
import sys
st = sys.argv[1]
st_m = ''
st_w = ''
i = 0
kol_m = 0
kol_w = 0
while i <= (len(st)-1):
    if st[i] == "m" :
        st_m = st_m + "*"
        kol_m += 1
        i += 1
    else:
        if st[i] == "w" :
            st_w = st_w + "*"
            kol_w += 1
            i += 1
        else:
             i += 1
        #print (i)
else:
    if kol_m > 0:
        st_m = ' '+ st_m
    st_m = 'm ('+str(kol_m)+')'+ st_m
    print (st_m)
    if kol_w > 0:
        st_w = ' '+ st_w
    st_w = 'w ('+str(kol_w)+')'+ st_w
    print (st_w)
