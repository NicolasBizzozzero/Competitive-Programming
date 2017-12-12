from itertools import permutations



def combinaison_match(A, B):
	if len(A) != len(B):
		return False
	for a, b in zip(A, B):
		if ((a == 'A' and b != "T") or\
			(a == 'T' and b != "A") or\
			(a == 'C' and b != "G") or\
			(a == 'G' and b != "C")):
			return False
	return True



def main():
	N = int(input())
	brins = [input() for _ in range(N)]
	for perm in permutations(brins, len(brins)):
		for i in range(1, len(perm)):
			comb = perm[:i], perm[i:]
			if combinaison_match("".join(comb[0]), "".join(comb[1])):
				print(" ".join(comb[0]), "#", " ".join(comb[1]), sep="")
				return


if __name__ == '__main__':
	main()
