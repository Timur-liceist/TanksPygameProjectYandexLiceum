l = int(input())
# r = map(int, input().split())
r = int(input())
t = 0
for i in range(l, r + 1):
    if list(map(int, list(str(i)))) == sorted(list(map(int, list(str(i))))):
        t += 1
print(t)