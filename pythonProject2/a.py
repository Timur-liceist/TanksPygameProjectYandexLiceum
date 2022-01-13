n = int(input())
name = list(map(int, input().split()))
zimax = max(name[0], name[1])
pred_max = min(name[0], name[1])
print(pred_max, end=" ")
for i in range(2, n):
    if name[i] >= zimax:
        pred_max = zimax
        zimax = name[i]
    elif name[i] > pred_max:
        pred_max = name[i]
    print(pred_max, end=" ")
