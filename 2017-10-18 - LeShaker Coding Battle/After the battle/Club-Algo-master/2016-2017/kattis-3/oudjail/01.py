tok = 'simon says'
ntok = len(tok)

def pstdin():
    sentence = []
    t = int(input())
    for i in range(t):
        sentence.append(input())

    return sentence

def print_sentence(ss):
    for s in ss:
        if s.startswith(tok) :
            print(s[ntok + 1:])
        else :
            print('')

if __name__ == '__main__':
    print_sentence(pstdin())
