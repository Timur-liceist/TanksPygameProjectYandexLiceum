name = input()
t = set()
g = set()
l = len(name)
for i in range(1, l + 1):
    for j in range(l):
        t.add(name[j:j + i])
for i in range(1, l):
    for j in range(l):
        stroka = ""
        for h in range(l):
            if h < j:
                stroka += name[h]
            elif h > i:
                stroka += name[h]
        if stroka:
            g.add(stroka)
print(g == t)
print(g, t)
print(len(g), len(t))