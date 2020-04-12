import sys
st = sys.argv[1]
st_n = ''
i = len(st)-1
while i >= 0:
    st_n=st_n +st[i]
    i -= 1
else:
    print(st_n)
