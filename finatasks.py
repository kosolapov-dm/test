n = int(input())
x = 1
print(1, end=' ')
for i in range(1, n + 1):
    if x == n:
        break
    if i > 1:
        for j in range(i):
            x += 1
            print(i, end=' ')
            if x == n:
                break
