n, l = [int(s) for s in input().split()]

pr = False
for i in range(10 ** (l - 1), 10 ** l):
    i = str(i)
    for j in range(1, len(i)):
        a, b = i[:j], i[j:]

        if a[0] == '0' or b[0] == '0':
            continue

        if ((int(a) ** 2) + (2 * int(b))) == n:
            print(a + b)
            pr = True

if not pr:
    print("Zut !")
