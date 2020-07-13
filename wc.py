import sys

if len(sys.argv) > 1:
    f = open(sys.argv[1], "r")
else:
    f = sys.stdin

s = f.read()
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
