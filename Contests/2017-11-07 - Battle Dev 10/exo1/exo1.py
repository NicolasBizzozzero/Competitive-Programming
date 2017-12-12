N = int(input())

cartes = []
for _ in range(N):
    a, b = input().split()
    a, b = int(a), int(b)
    cartes.append([a, b])

resulta, resultb = 0, 0
for a, b in cartes:
    if a > b:
        resulta += 1
    elif a < b:
        resultb += 1
print("A" if resulta > resultb else "B")

def main():
	pass


if __name__ == '__main__':
	main()
