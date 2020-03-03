import os
import collections

from operator import itemgetter

from core import Problem, Number, main


Input = collections.namedtuple("Input", ["M", "N", "slices"])
Solution = collections.namedtuple("Solution", ["pizzas", "nb_pizzas"])

PATH_DIR_INPUTS = os.path.join("..", "inputs", "2019_pizza")
PATH_DIR_OUTPUTS = os.path.join("..", "outputs", "2019_pizza")


class PracticeProblem(Problem):
    def parse_input(self, path_file_input: str) -> Input:
        with open(path_file_input, 'r') as fp:
            lines = fp.readlines()
        M, N = list(map(int, lines[0].rstrip().split(" ")))
        slices = list(map(int, lines[1].rstrip().split(" ")))
        return Input(M, N, slices)

    def score(self, inp: Input, solution: Solution) -> Number:
        if len(solution.pizzas) == 0:
            return 0
        elif len(solution.pizzas) == 1:
            return inp.slices[solution.pizzas[0]]
        return sum(itemgetter(*solution.pizzas)(inp.slices))

    def solve(self, inp: Input) -> Solution:
        return self._solve_reversed_subslices(inp)

    def _solve_reversed(self, inp: Input) -> Solution:
        """ Iterate through the reversed slices list, then greedely add slices if possible. """
        pizzas = []
        nb_slices = 0
        for i, pizza in enumerate(reversed(inp.slices)):
            if nb_slices + pizza > inp.M:
                continue
            else:
                nb_slices += pizza
                pizzas.append(len(inp.slices) - 1 - i)
        return Solution(pizzas, len(pizzas))

    def _solve_reversed_subslices(self, inp: Input) -> Solution:
        """ Apply _solve_reversed on all slices, then on the subslices list without the last element, then on the
        subslices list without the second-to-last element, etc.
        """
        # First run
        solution = self._solve_reversed(inp)
        max_score = self.score(inp, solution)
        best_solution = solution

        for i in range(1, len(inp.slices)):
            new_solution = self._solve_reversed(Input(inp.M, inp.N, inp.slices[:-i]))
            new_score = self.score(inp, new_solution)

            if new_score > max_score:
                best_solution = new_solution
                max_score = new_score
        return best_solution


def func_convert(solution: Solution) -> str:
    return "{nb_pizzas}\n{pizzas}".format(**solution._asdict())


if __name__ == "__main__":
    main(
        problem_class=PracticeProblem,
        func_convert=func_convert,
        path_dir_inputs=PATH_DIR_INPUTS,
        path_dir_outputs=PATH_DIR_OUTPUTS,
    )
