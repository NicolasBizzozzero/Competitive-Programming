import fileinput


def parse_input(size):
    lst_input = []

    with fileinput.input(files=('1.in')) as file:
        for line in file:
            lst_input.append(line)

    return lst_input[1:]

def print_solution(case_number, solution):
    print("Cas #" + str(case_number) +": " + str(solution))


def count_char(string):
    char_dic = {}
    for char in string:
        if char in char_dic.keys():
            char_dic[char] += 1
        else:
            char_dic[char] = 1
    return char_dic


def delete_chars_from_dict(chars_to_delete, dict):
    for char in chars_to_delete:
        if char in dict.keys():
            del dict[char]

def remove_one_occurence_from_dict(chars_to_delete, dict):
    for char in chars_to_delete:
        if char in dict.keys():
            dict[char] -= 1
        if dict[char] <= 0:
            del dict[char]


def get_numbers_from_str(dico):
    number = ""

    # get ZERO
    while True:
        if "Z" in dico:
            number += "0"
            remove_one_occurence_from_dict("ZERO", dico)
        else:
                break
    # get SEPT
    while True:
        if "P" in dico:
            number += "7"
            remove_one_occurence_from_dict("SEPT", dico)
        else:
            break
    # get HUIT
    while True:
        if "H" in dico:
            number += "8"
            remove_one_occurence_from_dict("HUIT", dico)
        else:
            break
    # get NEUF
    while True:
        if "F" in dico:
            number += "9"
            remove_one_occurence_from_dict("NEUF", dico)
        else:
            break
    # # get QUATRE
    # if "Q" and "U" and "A" and "T" and "R" and "E" in dico:
    #     number += "4"
    #     remove_one_occurence_from_dict("QUATRE", dico)

    # get TROIS
    while True:
        if "O" in dico:
            number += "3"
            remove_one_occurence_from_dict("TROIS", dico)
        else:
            break

    # get CINQ
    while True:
        if "C" in dico:
            number += "5"
            remove_one_occurence_from_dict("CINQ", dico)
        else:
            break
    # get SIX
    while True:
        if "S" in dico:
            number += "6"
            remove_one_occurence_from_dict("SIX", dico)
        else:
            break
    # get Deux
    while True:
        if "X" in dico:
            number += "2"
            remove_one_occurence_from_dict("DEUX", dico)
        else:
            break
    # get QUATRE
    while True:
        if "Q" in dico:
            number += "4"
            remove_one_occurence_from_dict("QUATRE", dico)
        else:
            break
    # get Un
    while True:
        if "U" in dico:
            number += "1"
            remove_one_occurence_from_dict("UN", dico)
        else:
            break
    return number

def sort_solution(solution):
    solution = sorted(solution)
    new_solution = ""
    for c in solution:
        new_solution += c

    return new_solution



if __name__ == '__main__':
    with fileinput.input(files=('1.in')) as file:
        for line in file:
            nb_of_input = int(line)
            break

    lst_input = parse_input(nb_of_input)
    
    for index_element in range(len(lst_input)):
        dico = count_char(lst_input[index_element])
        delete_chars_from_dict("\n", dico)
        solution = get_numbers_from_str(dico)
        solution = sort_solution(solution)
        print_solution(index_element+1, solution)
