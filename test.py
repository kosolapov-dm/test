s = input()
print(s[0], end='')
c = 1
for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        c += 1
    else:
        print(c, end='')
        print(s[i + 1], end='')
        c = 1
print(c)










