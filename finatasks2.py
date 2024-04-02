lst = [int(i) for i in input().split()]
x = int(input())

if lst.count(x) == 0:
    print("Отсутствует")
else:
    for j in range(len(lst)):
        if lst[j] == x:
            print(j, end=' ')

