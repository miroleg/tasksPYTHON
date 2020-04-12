import sys
text = sys.stdin.read()
f1 = text.split()

f3 = f1[0]
f4 = f1[1]
a = eval(f3)
b = eval(f4)
c = a + b
print(c)
