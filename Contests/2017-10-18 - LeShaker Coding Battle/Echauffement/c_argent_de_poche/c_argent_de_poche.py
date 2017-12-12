from statistics import mean

n = input()
l = [float(s) for s in input().split()]

res = round(((20 - (max(l) - min(l))) * mean(l) ** 2) / 100, 2)
print("{:0.2f}".format(res))
