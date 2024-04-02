s = input().lower().split()
d = {}
for i in range(len(s)):
    a = s.count(s[i])
    if s[i] not in d:
        d[s[i]] = a
for key, value in d.items():
    print(key, value)