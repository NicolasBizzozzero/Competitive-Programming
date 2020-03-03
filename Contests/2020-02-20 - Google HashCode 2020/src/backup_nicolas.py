""" Code source pour notre solution au problème du Google HashCode 2020.

Auteurs :
  * Nicolas Bizzozzéro
  * Raphaël Sourty

Equipe :
  * IRIT UPS

Résultats après le qualification round :
  * Score : 23,382,831
  * Classement monde : 2793 / 10724
  * Classement France : 228 / 784
"""

import os
import collections
import random
import shutil

from glob import glob

import tqdm

import numpy as np

from core import Problem, Number, main

# TODO: Les fonctions `score` et `score_sans_doublons` fonctionnent mal et ne calcule pas le score réel.


Input = collections.namedtuple("Input", ["B", "L", "D", "book_scores", "librairies", "books"])
Solution = collections.namedtuple("Solution", ["librairies", "books"])

PATH_DIR_INPUTS = os.path.join("..", "inputs", "2020_book_scanning")
PATH_DIR_OUTPUTS = os.path.join("..", "outputs", "2020_book_scanning")


class TemplateProblem(Problem):
    def parse_input(self, path_file_input: str) -> Input:
        with open(path_file_input, 'r') as fp:
            lines = fp.readlines()

        B, L, D = list(map(int, lines[0].strip().split(' ')))
        book_scores = np.asarray(list(map(int, lines[1].strip().split(' '))))
        librairies = []
        books = []
        for i, line in enumerate(lines[2:]):
            line = list(map(int, line.strip().split(' ')))
            if i % 2 == 0:
                librairies.append(np.asarray(line))
            else:
                books.append(np.asarray(line))
        return Input(B=B, L=L, D=D, book_scores=book_scores, librairies=librairies, books=books)

    def score(self, inp: Input, solution: Solution) -> Number:
        def _books_to_score(books):
            return sum(inp.book_scores[b] for b in books)

        return sum(map(_books_to_score, solution.books))

    def score_sans_doublons(self, inp: Input, solution: Solution) -> Number:
        possible_books = np.zeros(shape=(inp.B,))
        for books in solution.books:
            possible_books[books] = 1
        return np.sum(inp.book_scores[np.argwhere(possible_books)], axis=0)

    def solve(self, inp: Input) -> Solution:
        return self._solve_random_onelibrary(inp)

    def _solve_random_onelibrary(self, inp: Input) -> Solution:
        id_library = random.randint(0, inp.L - 1)

        solution_librairies = []
        solution_books = []
        jours_actuel = 0

        ordered_books = np.zeros(shape=(inp.B,))

        for id_library in np.random.choice(a=list(range(inp.L)),
                                           size=random.randint(0, inp.L),
                                           replace=False):
            jours_restants = inp.D - jours_actuel
            if inp.librairies[id_library][1] < jours_restants:
                jours_actuel += inp.librairies[id_library][1]

                # Keep only non-ordered books
                possible_books = np.zeros(shape=(inp.B,))
                possible_books[inp.books[id_library]] = 1
                possible_books = np.argwhere(ordered_books - possible_books == -1).squeeze()

                orderable_books = order_books_by_score_decreasing(inp, possible_books=possible_books,
                                                                  max_books_per_day=inp.librairies[id_library][2],
                                                                  jours_actuel=jours_actuel)
                solution_librairies.append(id_library)
                solution_books.append(orderable_books)
                ordered_books[orderable_books] = 1

        return Solution(librairies=solution_librairies, books=solution_books)

    @classmethod
    def _compute_score(cls, data: Input) -> dict:
        score_library = {}
        for idx, (n_livre, time_signup, scan_per_day) in tqdm.tqdm(enumerate(data.librairies), position=0,
                                                                   disable=True):
            data.books[idx] = list(data.books[idx])
            data.books[idx].sort(reverse=True)
            books = data.books[idx]
            percent_livre_to_keep = ((data.D - time_signup) * scan_per_day) / n_livre
            books = books[0: int(len(books) * percent_livre_to_keep)]
            score_library[idx] = np.sum(books) * scan_per_day / (time_signup**2)
        return score_library

    @classmethod
    def _kpi_librairies(cls, data: Input, drop_prob: float = 0.08) -> Solution:
        """ Computes score per library. """
        score_library = cls._compute_score(data)
        registration_cumul_time = 0
        librairies = []
        books = []
        for id_lib in tqdm.tqdm(sorted(score_library, key=score_library.get, reverse=True), disable=True):
            if random.random() <= drop_prob:
                continue
            if (registration_cumul_time + data.librairies[id_lib][1] + data.librairies[id_lib][2]) <= data.D:
                registration_cumul_time += data.librairies[id_lib][1]
                librairies.append(id_lib)
                books.append(data.books[id_lib])
        return Solution(librairies, books)


def order_books_by_score_decreasing(inp, possible_books, max_books_per_day, jours_actuel):
    # Calcul du nombre de livres commandables avec les jours restants
    jours_restants = inp.D - jours_actuel
    nb_books_orderable = min(len(possible_books), jours_restants * max_books_per_day)

    # On se limite qu'à ce nombre de livres commandables. On trie les livres par leur score puis on tronque la liste
    book_scores = inp.book_scores[possible_books]
    idx_tries = book_scores.argsort()[::-1]
    possible_books = possible_books[idx_tries]
    return possible_books[:nb_books_orderable]


def func_convert(solution: Solution) -> str:
    res = str(len(solution.librairies)) + '\n'
    for library, book in zip(solution.librairies, solution.books):
        res += str(library) + " " + str(len(book)) + "\n"
        res += " ".join(map(str, book)) + "\n"
    return res


def clean_outputs(path_dir_outputs):
    """ Delete all non-best scores for each outputs. """
    for identifier in ("a", "b", "c", "d", "e", "f"):
        best_score = 0
        for file in sorted(glob(os.path.join(path_dir_outputs, identifier + "_*")))[::-1]:
            score = int(file.split("/")[-1].split(identifier + "_")[-1].split(".out")[0])
            if score < best_score:
                os.remove(file)
            else:
                best_score = score


if __name__ == "__main__":
    main(
        problem_class=TemplateProblem,
        func_convert=func_convert,
        path_dir_inputs=PATH_DIR_INPUTS,
        path_dir_outputs=PATH_DIR_OUTPUTS,
        inputs_to_skip=[],
    )
