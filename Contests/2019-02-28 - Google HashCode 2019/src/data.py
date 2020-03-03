from collections import OrderedDict
import numpy as np

def score(slides, photos):
    """Compute the score.

    Parameters
    -----------        
        slides : list of tuples
            Each item of the list is the tuple of photos ids
        
        photos : dict
            Dict of photos : {"id": {"orientation": "V/H", "tags": ["tag1", "tag2"]}}
    """
    total_score = 0
    for prev, curr in zip(slides, slides[1:]):
        prev_tags = set()
        for phot_id in prev:
            tags = photos[phot_id]["tags"]
            prev_tags |= set(tags)
        
        curr_tags = set()
        for phot_id in curr:
            tags = photos[phot_id]["tags"]
            curr_tags |= set(tags)
        
        common_tags = curr_tags & prev_tags
        prev_curr = prev_tags - common_tags
        curr_prev = curr_tags - common_tags

        total_score += min(len(common_tags), len(prev_curr), len(curr_prev))
    return total_score


def detailed_score(slides, photos):
    """Compute the detailedscore.

    Parameters
    -----------        
        slides : list of tuples
            Each item of the list is the tuple of photos ids
        
        photos : dict
            Dict of photos : {"id": {"orientation": "V/H", "tags": ["tag1", "tag2"]}}
    """
    scores = []
    for prev, curr in zip(slides, slides[1:]):
        prev_tags = set()
        for phot_id in prev:
            tags = photos[phot_id]["tags"]
            prev_tags |= set(tags)
        
        curr_tags = set()
        for phot_id in curr:
            tags = photos[phot_id]["tags"]
            curr_tags |= set(tags)
        
        common_tags = curr_tags & prev_tags
        prev_curr = prev_tags - common_tags
        curr_prev = curr_tags - common_tags

        scores.append(min(len(common_tags), len(prev_curr), len(curr_prev)))
    return scores


def parse_input(file):
	with open(file) as f:
		lines = f.readlines()[1:]

	pictures = OrderedDict()
	for i in range(len(lines)):
		line = lines[i]
		orientation, _, *tags = line.split()
		pictures[i] = {
			"orientation": orientation,
			"tags": list(tags)
		}
	return pictures


if __name__ == '__main__':
	parse_input("../data/e_shiny_selfies.txt")
