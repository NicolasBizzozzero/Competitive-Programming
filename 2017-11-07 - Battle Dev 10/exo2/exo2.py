
N = int(input())
P = input()
produits = []
for _ in range(N):
    produit, prix = input().split()
    prix = int(prix)
    produits.append([produit, prix])


minprix = None
for produit, prix in produits:
    if (produit == P) and ((minprix is None) or (minprix > prix)):
        minprix = prix

print(minprix)


def main():
	pass


if __name__ == '__main__':
	main()
