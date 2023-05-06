import sys


a = int(sys.argv[2])

all = open(sys.argv[1], "r", encoding="utf-8")
cut = open(sys.argv[1]+".cut", "w", encoding="utf-8")

for l in all.readlines():
    if a > 0:
        cut.write(l)
        a-=1

all.close()
cut.close()