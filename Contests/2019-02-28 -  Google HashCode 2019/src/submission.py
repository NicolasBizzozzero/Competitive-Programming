


def submission_file(slides, filename="submission.txt"):
    """Prepare the submission file

    Parameters
    -----------
        slides : list of tuples
            Each item of the list is the tuple of photos ids

    Example
    ---------
    >>> slides = [(0,), (1, 2)]  # First slide has photo 0, seconde 1 & 2
    >>> submission_file(slides)
    """
    with open(filename, "w") as f:
        nb_slides = len(slides)
        f.write(f"{nb_slides}\n")
        for item in slides:
            for photo_id in item:
                f.write(f"{photo_id} ") 
            f.write("\n")
    