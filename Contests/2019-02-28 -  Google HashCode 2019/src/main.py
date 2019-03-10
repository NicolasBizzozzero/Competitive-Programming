import math
import sys
from random import shuffle

from data import parse_input, score
from submission import submission_file


def _baseline_algo(pictures):
	output  = []
	i_picture = 0
	while pictures.get(i_picture, False):
		if pictures[i_picture]["orientation"] == "H":
			output.append((i_picture,))
			i_picture += 1
		elif pictures[i_picture]["orientation"] == "V" and \
		     pictures.get(i_picture + 1) and \
		     pictures[i_picture + 1]["orientation"] == "V":
			output.append((i_picture, i_picture + 1))
			i_picture += 2
		else:
			# output.append((i_picture,))
			i_picture += 1
	return output


def random_(photos):
    """Comme son nom l'indique."""
    ids = list(photos.keys())
    shuffle(ids)

    slides = []
    prev_empty_v = None
    for phot_id in ids:
        if photos[phot_id]["orientation"] == "H":
            slides.append((phot_id,))
        else:
            if prev_empty_v is None:
                slides.append((phot_id,))
                prev_empty_v = len(slides) - 1
            else:
                slides[prev_empty_v] = (slides[prev_empty_v][0], phot_id)
                prev_empty_v = None
    
    if prev_empty_v is not None:
        slides = slides[:prev_empty_v] + slides[prev_empty_v + 1:]
    return slides



def bruteforce_random(file_input, fileoutput):
	pictures = parse_input(file_input)
	best_score = 0
	best_slides = None
	while True:
		output = random_(pictures)
		curr_score = score(output, pictures)

		if curr_score > best_score:
			best_score = curr_score
			best_slides = output

			sys.stdout.write('\r')
			sys.stdout.write("Best score : " + str(curr_score))
			sys.stdout.flush()
			submission_file(output, "../output/bruteforce/soumission_" + fileoutput + "_" + str(curr_score) + ".txt")


def main(file_input, fileoutput):
    pictures = parse_input(file_input)
    output = random_(pictures)
    submission_file(output, "../output/soumission_" + fileoutput)
    print("Score for", fileoutput, ":", score(output, pictures))



filenames = ["a_example.txt", "b_lovely_landscapes.txt", "c_memorable_moments.txt", "d_pet_pictures.txt", "e_shiny_selfies.txt"]


if __name__ == "__main__":
    # for filename in filenames:
    #     main(f"../data/{filename}", filename)
    bruteforce_random("../data/d_pet_pictures.txt", "d_pet_pictures.txt")
