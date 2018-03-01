from parser import Ride, manhattan

def random_this(nb_vehicule, client_list, T):
    v = list(range(nb_vehicule))
    s = sorted(client_list, key = lambda c: c.latest)

    ret = [[ve, [cl], cl.distance_totale((0, 0))] for ve, cl in zip(v, s)]
    for c in s[nb_vehicule:]:
        ret = sorted(ret, key=lambda r: r[2])
        ret[0][1].append(c)
        ret[0][2] += c.distance_totale(ret[0][1][-1].finish)
    ret = [(r[0], [c.id_ride for c in r[1]]) for r in ret]
    return ret

def select_smartly(nb_vehicule, client_list, T):
    v = list(range(nb_vehicule))
    s = sorted(client_list, key = lambda c: c.latest)

    ret = [[ve, [cl], cl.distance_totale((0, 0))] for ve, cl in zip(v, s)]
    for c in s[nb_vehicule:]:
        ret = sorted(ret, key=lambda r: r[2])
        if c.distance_totale(ret[0][1][-1].finish) <= c.latest:
            ret[0][1].append(c)
            ret[0][2] += c.distance_totale(ret[0][1][-1].finish)
    ret = [(r[0], [c.id_ride for c in r[1]]) for r in ret]
    return ret

def smalls_first(nb_vehicule, client_list, T):
    v = list(range(nb_vehicule))
    s = sorted(client_list, key= lambda c : c.distance_trajet)

    ret = [[ve, [cl], cl.distance_totale((0, 0))] for ve, cl in zip(v, s)]
    for c in s[nb_vehicule:]:
        ret = sorted(ret, key=lambda r: r[2])
        if c.distance_totale(ret[0][1][-1].finish) <= c.latest:
            ret[0][1].append(c)
            ret[0][2] += c.distance_totale(ret[0][1][-1].finish)
    ret = [(r[0], [c.id_ride for c in r[1]]) for r in ret]
    return ret


def nearest_first(nb_vehicule, client_list, T, B):
    v = list(range(nb_vehicule))
    s = client_list
    temp = Ride(0, (0, 0), (0, 0), 0, 0)
    ret = [[ve, [temp], 0] for ve, cl in zip(v, s)]
    for c in s:
        ret = sorted(ret, key=lambda r: (c.distance_trajet + B) / c.distance_totale(r[1][-1].finish))
        #ret = sorted(ret, key=lambda r: c.distance_totale(r[1][-1].finish) + r[2])
        selected = False
        i = 0
        while not selected and i < nb_vehicule:
            if c.distance_totale(ret[i][1][-1].finish) + ret[i][2] <= c.latest and c.earliest <= manhattan(c.start, ret[i][1][-1].finish):
                ret[i][1].append(c)
                ret[i][2] += c.distance_totale(ret[i][1][-1].finish) + 1
                selected = True
            i += 1
    ret = [(r[0], [c.id_ride for c in r[1][1:]]) for r in ret]
    return ret

def big_first(nb_vehicule, client_list, T):
    v = list(range(nb_vehicule))
    s = sorted(client_list, key= lambda c : c.distance_trajet)

    ret = [[ve, [cl], cl.distance_totale((0, 0))] for ve, cl in zip(v, s)]
    for c in s[nb_vehicule:]:
        ret = sorted(ret, key=lambda r: -r[2])
        if c.distance_totale(ret[0][1][-1].finish) <= c.latest:
            ret[0][1].append(c)
            ret[0][2] += c.distance_totale(ret[0][1][-1].finish)
    ret = [(r[0], [c.id_ride for c in r[1]]) for r in ret]
    return ret

def v_first(nb_vehicule, client_list, T, B):
    v = list(range(nb_vehicule))
    s = client_list
    temp = Ride(0, (0, 0), (0, 0), 0, 0)
    ret = [[ve, [temp], 0] for ve, cl in zip(v, s)]
    prev = []
    while prev != ret:
        prev = list(ret)
        for vec in ret:
            s = sorted(s, key = lambda c: (c.distance_trajet + B) / c.distance_totale(vec[1][-1].finish))
            selected = False
            i = 0
            while not selected and i < len(s) and vec[2] < T:
                c = s[i]
                if c.distance_totale(vec[1][-1].finish) + vec[2] <= c.latest and c.earliest <= manhattan(c.start, vec[1][-1].finish):
                    vec[1].append(c)
                    vec[2] += c.distance_totale(vec[1][-1].finish)
                    s = s[i+1:] + s[:i-1]
                    selected = True
                i += 1

    ret = [(r[0], [c.id_ride for c in r[1][1:]]) for r in ret]
    return ret
