name = input()
t = set()
g = set()
l = len(name)
for i in range(1, l + 1):
    for j in range(l):
        t.add(name[j:j + i])
# for i in range(1, l):
#     for j in range(l):
#         stroka = name[]
#         if stroka:
#             g.add(stroka)
for i in range(1, l + 1):
    for j in range(l + 1):
        t1 = name[:j]
        t2 = name[j + i:]
        print(len(name[:j] + name[j + i:]), i)
        s = name[:j] + name[j + i:]

        if s:
            g.add(name[:j] + name[j + i:])
print(g == t)
print(g, t)
print(len(g), len(t))