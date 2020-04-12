import sys
st = sys.argv[1]
st_n = ''
i = 0
while i <= (len(st)-1):
    if st[i].lower() == st[i] :
        st_n=st_n +st[i].upper()
    else:
        st_n=st_n +st[i].lower()
    i += 1
else:
    print (st_n)
