from random import shuffle


def random(photos):
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
                prev_empty_v = len(slides)
            else:
                slides[prev_empty_v] = (slides[prev_empty_v][0], phot_id)
                prev_empty_v = None
    return slides
