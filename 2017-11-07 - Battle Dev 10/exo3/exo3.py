
def arrose_cases(champ, x, y, N):
    for j in (y - 1, y, y + 1):
        for i in (x - 1, x, x + 1):
        	if not (i < 0 or j < 0 or i >= N or j >= N):
	            try:
	                if champ[j][i] != 'X':
	                    champ[j][i] = 'O'
	            except IndexError:
	                pass



def arrose_tout_le_champ(champ, N):
    for y in range(len(champ)):
        for x in range(len(champ[0])):
            if champ[y][x] == "X":
                arrose_cases(champ, x, y, N)



def compte_cases_cultivables(champ):
    i = 0
    for y in range(len(champ)):
        for x in range(len(champ[0])):
            if champ[y][x] == "O":
                i += 1
    return i


def print_champ(champ):
    for y in range(len(champ)):
        for x in range(len(champ[0])):
        	print(champ[y][x], end="")
        print("")

def main():
    N = int(input())
    champ = [list(input()) for _ in range(N)]
    arrose_tout_le_champ(champ, N)
    print(compte_cases_cultivables(champ))


if __name__ == '__main__':
	main()
