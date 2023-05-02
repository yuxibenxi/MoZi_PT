
a = 1000000

all = open("mozi.all.tsv", "r", encoding="utf-8")
cut = open("mozi.cut.tsv", "w", encoding="utf-8")

for l in all.readlines():
    if a > 0:
        cut.write(l)
        a-=1

all.close()
cut.close()