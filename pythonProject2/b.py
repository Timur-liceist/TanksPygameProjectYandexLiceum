n, a, b, w, h = map(int, input().split())
# 11 2 3 21 25
low = 0
right = max(w, h)
# w // a + h // b or w // b + h // a
while right - low > 1:
    middle = (right + low) // 2
    if (w // (a + middle * 2)) * (h // (b + middle * 2)) < n or (w // (b + middle * 2)) * (h // (a + middle * 2)) < n:
        right = middle
    else:
        low = middle

if((w // (a + right * 2)) * (h // (b + right * 2)) >= n or (w // (b + right * 2)) * (h // (a + right * 2)) >= n):
    print(right)
else:
    print(low)