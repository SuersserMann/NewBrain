a = input().split()
a = a[0]

left = 0
right = 0
z = []
c = 0
r1 = 0
r2 = 0
for i in range(len(a)):
    c = len(z)
    if a[i] not in z and c < 2:
        if c == 1:
            mid = i
        z.append(a[i])

    if a[i] not in z and c >= 2:
        z.pop(0)
        right = i - 1
        if right - left > r2 - r1:
            r1, r2 = left, right
        left = mid
    if a[i] in z:
        right = i
        if right - left > r2 - r1:
            r1, r2 = left, right
print(r2 - r1 + 1)
