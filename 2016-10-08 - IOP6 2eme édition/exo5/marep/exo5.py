import fileinput


def parse_input():
    lst_input = []
    nb_of_input = 0

    with fileinput.input(files=('0.in')) as file:
        for line in file:
            if fileinput.isfirstline():
                nb_of_input = int(line)
            lst_input.append(line.split())  

    return lst_input[1:]

def get_variables(input):
    N = input[0]
    R = input[1]
    P = input[2]
    S = input[3]
    return N, R, P, S

def breed(horse1, horse2):
    if horse1 == 'P':
        if horse2 == 'S':
            return 'S'
        elif horse2 == "R":
            return "P"
        else:
            return "IMPOSSIBLE"
    elif horse1 == "R":
        if horse2 == "P":
            return "P"
        elif horse2 == "R":
            return "IMPOSSIBLE"
        else:
            return "R"
    else:
        if horse2 == "S":
            return "IMPOSSIBLE"
        elif horse2 == "R":
            return "R"
        else:
            return "S"

def this_config_works(R, P, S):
    if (P < 0) or (R < 0) or (S < 0):
        return "A"
    if (R == 1 and P == 1):
        return "PR"
    elif (R == 1 and S == 1):
        return "RS"
    elif (S == 1 and P == 1):
        return "PS"
    return "A"

def get_config_horses(N, R, P, S):
    if N == 1:
        return this_config_works(R, P, S)

    else:
        if (R == 0) or (P == 0) or (S == 0):
            return "IMPOSSIBLE"

        config1 = "RP" + get_config_horses(N-1, R-1, P, S)
        config2 = "PS" + get_config_horses(N-1, R, P-1, S)
        config3 = "SR" + get_config_horses(N-1, R, P, S-1)

        if (config1[-1] != "A"):
            return config1
        if (config2[-1] != "A"):
            return config2
        if (config3[-1] != "A"):
            return config3
        else:
            return "IMPOSSIBLE"


def print_solution(case_number, solution):
    if solution == "A" or (solution[-10:] == "IMPOSSIBLE"):
        solution = "IMPOSSIBLE"
    print("Cas #" + str(case_number) + ": " + str(solution))


if __name__ == '__main__':
    lst_input = parse_input()
    
    for index_element in range(len(lst_input)):
        nb_phrases = lst_input[index_element]

        solution = get_config_horses(int(N), int(R), int(P), int(S))

        print_solution(index_element+1, solution)