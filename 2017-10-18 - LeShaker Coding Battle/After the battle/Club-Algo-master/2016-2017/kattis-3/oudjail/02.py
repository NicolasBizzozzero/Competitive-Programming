def print_policies(stdin) :
    #print(stdin)
    state = stdin[0]
    up, down, prf = 0, 0, 0
    p = stdin[1]

    if state == 'D' :
        up += 1
    elif p == 'D' :
        up += 2
    # Down rules
    if state == 'U' :
        down += 1
    elif p == 'U' :
        down += 2

    prf = 1 if state != p else 0
    state = p

    for i in range(2, len(stdin)):
        p = stdin[i]
        # Up rules
        if p == 'D' :
            up += 2

        # Down rules
        if p == 'U' :
            down += 2

        # Pref rules
        if state != p:
            prf += 1

        #print("state", state, "p :", p, "up :", up, "down :", down, "prf :", prf)
        state = p

    print(up)
    print(down)
    print(prf)

if __name__ == '__main__':
    print_policies(input())
