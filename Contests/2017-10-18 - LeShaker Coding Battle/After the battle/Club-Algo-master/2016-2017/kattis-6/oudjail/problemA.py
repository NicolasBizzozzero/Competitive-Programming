from functools import cmp_to_key


def soluc():
	n = int(input())
	lines = []
	for l in range(n):
		lines.append(input().split(' '))
		divide = False
		if lines[l][0].isdigit():
			tmp = lines[l][0]
			lines[l][0] = lines[l][1]
			lines[l][1] = tmp
			divide = True
		lines[l][1] = int(lines[l][1])
		if (divide):
			lines[l][1] /= 2
	return sorted(lines, key=cmp_to_key(lambda a, b: a[1] - b[1]))



if __name__ == '__main__':
	sol = soluc()
	for s in sol:
		print(s[0])
