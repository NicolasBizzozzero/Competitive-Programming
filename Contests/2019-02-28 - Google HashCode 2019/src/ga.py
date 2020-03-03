import numpy as np
import random
from main import random_
from data import detailed_score, parse_input, score
from submission import submission_file
from multiprocessing import Pool

from functools import partial


def swap_zeros(slides, photos):
    sc = detailed_score(slides, photos)
    mask = [i for i, score in enumerate(sc) if score == 0]
    to_rand = [i for i, score in enumerate(sc) if score == 0]
    slide_copy = [a for a in slides]

    random.shuffle(to_rand)
    for i, j in zip(mask, to_rand):
        slides[i] = slide_copy[j]
    return slides


def global_swap_function(slides):
    slide1, slide2 = np.random.choice(len(slides), size=2, replace=False)
    slides[slide1], slides[slide2] = slides[slide2], slides[slide1]


def vertical_swap_function(slides):
    mask_vertical = [i for i, slide in enumerate(slides) if len(slide) == 2]
    slide1, slide2 = np.random.choice(mask_vertical, size=2, replace=False)
    slides[slide1], slides[slide2] = slides[slide2], slides[slide1]


def global_swap_batch_function(slides):
    slide1, slide2 = np.random.choice(len(slides), size=2, replace=False)
    slide1, slide2 = (slide1, slide2) if slide1 < slide2 else (slide2, slide1)

    max_batch_size = min(slide2 - slide1, len(slides) - slide2)
    batch_size = random.randint(1, max_batch_size - 1)

    slides[slide1:slide1 + batch_size], slides[slide2:slide2 +
                                               batch_size] = slides[slide2:slide2 + batch_size], slides[slide1:slide1 + batch_size]


def mutation(slides, photos, global_swap=0.2, vertical_swap=0.1, global_swap_batch=0.05, nb_sample=10):
    for _ in range(nb_sample):
        if random.random() < global_swap:
            global_swap_function(slides)
        if random.random() < vertical_swap:
            vertical_swap_function(slides)
        if random.random() < global_swap_batch:
            global_swap_batch_function(slides)
    swap_zeros(slides, photos)
    return slides


def cross(slides1, slides2, sc1, sc2, photos):
    used_ids = set()
    unused_ids = set(list(photos.keys()))

    doublons = []

    prop = sc1 / sc2
    w1 = prop / (prop + 1)
    w2 = 1 / prop

    new_slides = []
    for slide1, slide2 in zip(slides1, slides2):
        if random.random() < w1:
            new_slides.append(slide1)

            for photo_id in slide1:
                if photo_id in used_ids:
                    doublons.append(
                        (photo_id, len(new_slides) - 1, photos[photo_id]["orientation"]))
                else:
                    used_ids = used_ids + set([photo_id])
                    unused_ids = unused_ids - set([photo_id])
        else:
            new_slides.append(slide2)

    # Remove doublons
    hor_unused = {
        id_ for id_ in unused_ids if photos[id_]["orientation"] == "H"}
    ver_unused = {
        id_ for id_ in unused_ids if photos[id_]["orientation"] == "V"}

    for id_, pos, ori in doublons:
        if ori == "H":
            a = random.choice(hor_unused)
            new_slides[pos] = (id_,)
            hor_unused -= set([a])
        else:
            if new_slides[pos][0] == id_:
                a = random.choice(hor_unused)
                new_slides[pos] = (id_, new_slides[pos][1])
                hor_unused -= set([a])
            else:
                a = random.choice(hor_unused)
                new_slides[pos] = (new_slides[pos][0], id_)
                hor_unused -= set([a])

    return new_slides


if __name__ == "__main__":
    filename = "e_shiny_selfies.txt"
    pictures = parse_input(f"../data/{filename}")

    nb_individu = 100
    individus = [random_(pictures) for i in range(nb_individu)]

    best_score = 0
    best_one = None
    i = 0
    mutate = partial(mutation, photos=pictures)
    with Pool() as pool:
        while True:
            i += 1
            individus = pool.map(mutate, individus)
            scores = [(i, score(individu, pictures))
                      for i, individu in enumerate(individus)]
            scores = sorted(scores, key=lambda s: s[1], reverse=True)
            keep = scores[:len(scores) // 2]
            keep = [individus[k[0]] for k in keep]

            offset = len(scores) // 2
            for i in range(len(scores) // 2):
                id_slides1, id_slides2 = np.random.choice(
                    len(scores) // 2, size=2, replace=False)
                id_slides1 += offset
                id_slides2 += offset

                sc1 = scores[id_slides1][1]
                sc2 = scores[id_slides2][1]
                slides1 = individus[id_slides1]
                slides2 = individus[id_slides2]

                new_slide = cross(slides1, slides2, sc1, sc2, pictures)
                keep.append(new_slide)

            if max(scores) > best_score:
                best_score = max(scores)
                argmax = 0
                for i, sc in enumerate(scores):
                    if sc == best_score:
                        argmax = i
                        break
                best_one = individus[argmax]
            print(best_score)
            submission_file(best_one, "../output/soumission_" + filename)
