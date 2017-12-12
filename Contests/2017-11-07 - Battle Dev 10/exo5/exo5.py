from math import sqrt, pow, floor
from itertools import combinations, permutations



def distance(p1, p2):
	p1 = map(int, p1)
	p2 = map(int, p2)
	x1, y1, z1 = p1
	x2, y2, z2 = p2
	return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2) + pow(z2 - z1, 2))


def test_chemin(stations):
	dist = 0
	stats = stations[:]
	while len(stats) > 1:
		dist += distance(stats[0], stats[1])
		stats.pop(0)
	return dist


def make_perm_correcte(chemin, bout_min, bout_max):
	chem_correct = [bout_min]
	y_avant = bout_min[1]
	avance = True
	for x, y, z in chemin:
		if avance:
			if y < y_avant:
				chem_correct += [bout_max]
				avance = False
		else:
			if y > y_avant:
				chem_correct += [bout_min]
				avance = True
		chem_correct += [[x, y, z]]
		y_avant = y
	if avance:
		chem_correct += [bout_max]
	if chem_correct[-1] != bout_min:
		chem_correct += [bout_min]
	return chem_correct


def main():
	N = int(input())
	stations = [input().split() for _ in range(N)]
	stations.sort(key=lambda tup: tup[1])
	bout_min, bout_max = stations[0], stations[-1]
	stations = stations[1:-1]
	min_dist = None
	for perm in permutations(stations):
		chemin = make_perm_correcte(perm, bout_min, bout_max)
		curr_dist = test_chemin(chemin)

		if (min_dist is None) or min_dist > curr_dist:
			min_dist = curr_dist

	print(int(floor(min_dist)))
	
 
if __name__ == '__main__':
	main()
