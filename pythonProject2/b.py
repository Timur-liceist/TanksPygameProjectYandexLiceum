n, a, b, w, h = map(int, input().split())
# 11 2 3 21 25
low = 0
right = max(w, h)
# w // a + h // b or w // b + h // a
while right > low:
    middle = (right + low) // 2
    # if w // (a + middle * 2) + h // (b + middle * 2) <= n or w // (b + middle * 2) + h // (a + middle * 2) <= n:
    if w // (a + middle * 2) + h // (b + middle * 2) <= n:
        right = middle - 1
    elif w // (a + middle * 2) + h // (b + middle * 2) > n:
        print(1)
        low = middle + 1
        break
    # elif w // (a + middle * 2) + h // (b + middle * 2) > n or w // (b + middle * 2) + h // (a + middle * 2) > n:
print(low + 1)