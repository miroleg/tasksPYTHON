import sys
# int_numb = int(sys.argv[1])
int_numb = 32

def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


ss2 = convert_base(int_numb, to_base=2, from_base=10)
ss8 = convert_base(int_numb, to_base=8, from_base=10)
ss16 = convert_base(int_numb, to_base=16, from_base=10).lower()
print(int_numb, ss2, ss8, ss16)

# f1 = input('******* > :' )
f1 = "1 1"
f2 = f1.split(' ')
f3 = f2[0]
f4 = f2[1]
a1 = eval(f3)
a2 = eval(f4)
print( a1 + a2 )





fout = open("output.txt", "w")
fin = open("input.txt", "r")
f1 = fin.readline()
print(f1)
f2 = f1.split(' ')
f3 = f2[0]
f4 = f2[1]
a1 = eval(f3)
a2 = eval(f4)
print( a1 + a2 )
line = str(a1 + a2)
fout.write(line + '\n')
fout.close()
fin.close()


text = sys.stdin.read()
words = text.split()
wordcount = len(words)
print('Wordcount:', wordcount)
