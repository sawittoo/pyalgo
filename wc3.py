import sys

argc = len(sys.argv)
if argc == 1:
    f = sys.stdin
elif argc == 2:
    try:
        f = open(sys.argv[1], "r")
    except FileNotFoundError:
        sys.exit("wc: No Such file or directory:  {}".format(sys.argv[0], sys.argv[1]))
else:
    sys.exit("usage: {} [file]" .format(sys.argv[0]))

s = f.read()
s = s.lower()
s = s.replace(',', ' ')
s = s.replace('.', ' ')
s = s.replace('-', ' ')
s = s.replace('_', ' ')
s = s.replace(';', ' ')
s = s.replace(':', ' ')
s = s.replace("'", ' ')
s = s.replace('"', ' ')
s = s.replace('?', ' ')
s = s.replace('!', ' ')
s = s.replace('(', ' ')
s = s.replace(')', ' ')
s = s.replace('/', ' ')
s = s.replace('[', ' ')
s = s.replace(']', ' ')
words = s.split()

freq = {}
for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

sorted_freq = sorted(freq.items(), key=lambda x: x[1],reverse=True)

i = 0
for (k, v) in sorted_freq:
    if i == 20:
        break
    print("{}: {}".format(k, v))
    i += 1
