NROW = 8
NCOL = 8

def pstdin():
    return [input() for i in range(NROW)]

def algo(board):
    print(board)

if __name__ == '__main__':
    algo(pstdin())
