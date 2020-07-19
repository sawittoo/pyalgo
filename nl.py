import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1], "r")
else:
    f = sys.stdin

def nl(line):
    num=0
    for k in line:
        if k != '\n':
            num += 1
            print('%2d %s' %(num, k), file=sys.stdout, end='')
        else:
            print(' ', file=sys.stdout)

while True:
    s = f.readlines()
    if not s: break
    nl(s)
