import sys
st = sys.argv[1]
st_n = ''
i = len(st)-1
j = 0
while i >= 0:
    j += 1
    st_n=st_n +st[i]
    if j>=3 :
        st_n=st_n + " "
        j=0
    i -= 1
else:
    st=''
    i = len(st_n)-1
    while i >= 0:
        st=st+st_n[i]
        i -= 1
print(st)
