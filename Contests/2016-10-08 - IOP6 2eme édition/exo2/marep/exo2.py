import fileinput


def parse_input(size):
    lst_input = []

    with fileinput.input(files=('1.in')) as file:
        for line in file:
            lst_input.append(line)

    return lst_input[1:]

def print_solution(case_number, solution):
    if solution == True:
        solution = "VRAI"
    else:
        solution = "FAUX"
    print("Cas #" + str(case_number) +": " + str(solution))


if __name__ == '__main__':
    with fileinput.input(files=('1.in')) as file:
        for line in file:
            nb_of_input = int(line)
            break

    lst_input = parse_input(nb_of_input)
    
    for index_element in range(len(lst_input)):
        


        print_solution(index_element+1, solution)
