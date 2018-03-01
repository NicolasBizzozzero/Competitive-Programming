# code pour parser in
import numpy as np


INSTANCES_DIR = "instances"
instances = [
    "{}/a_example.in".format(INSTANCES_DIR),
    "{}/b_should_be_easy.in".format(INSTANCES_DIR),
    "{}/c_no_hurry.in".format(INSTANCES_DIR),
    "{}/d_metropolis.in".format(INSTANCES_DIR),
    "{}/e_high_bonus.in".format(INSTANCES_DIR)]


def manhattan(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


class Ride:
    def __init__(self, id_ride, init, end, earliest, latests):
        self.id_ride = id_ride
        self.start = init
        self.finish = end
        self.earliest = earliest
        self.latest = latests
        self.distance_trajet = manhattan(init, end)

    def __repr__(self):
        return str(self.__dict__)

    def distance_totale(self, pos_vehicule):
        return manhattan(pos_vehicule, self.start) + self.distance_trajet

    def gains_possibles(self, t_debut, t_fin, B):
        total = 0
        if t_fin <= self.latests:
            total += manhattan(self.start, self.finish)
        if t_debut == self.earliest:
            total += B
        return total


def get_score_solution(solution):
    if not solution_valide(solution):
        return -np.inf


def read(file_in):
    "nb_vehic, [clients], temps, bonus"
    f = open(file_in, 'r')
    txt = f.read()
    f.close()

    L = txt.split(chr(10))
    R, C, F, N, B, T = map(int, L[0].split())

    rides = []
    for i, t in enumerate(L[1:]):
        try:
            a, b, x, y, s, f = map(int, t.split())
            rides.append(Ride(i, (a, b), (x, y), s, f))
        except:
            pass
    return F, rides, T, B


def write(file_out, L):
    "[(id, [trajets])]"
    f = open(file_out, 'w')
    L = sorted(L)
    for i, trajets in L:
        s = str(len(trajets)) + ' ' + ' '.join(map(str, trajets)) + chr(10)
        f.write(s)
    f.close()


def parse_machines(file="machines_list.txt"):
    with open(file) as file:
        return [machine for machine in file.read().split("\n")if machine]


def compute_score(file):
    pass


def LANCE_LE_PROGRAMME_BORDEL():
    import glouton
    for i in instances:
        F, rides, T, B = read(i)
        s = glouton.v_first(F, rides, T, B)
        write(i[:-3] + ".out", s)


if __name__ == '__main__':
    LANCE_LE_PROGRAMME_BORDEL()
