import numpy as np


OUTPUT_CM = "_OUTPUT_CM.txt"
OUTPUT_MR = "_OUTPUT_MR.txt"


def postprocessing_chirac_mitterrand(predictions):
    global OUTPUT_CM

    content = "\n".join(predictions)
    with open(OUTPUT_CM, "w") as file:
        file.write(content)


def postprocessing_movie_reviews(predictions):
    global OUTPUT_MR

    new_predictions = []
    for c in predictions:
        if c == "pos":
            new_predictions.append("M")
        else:
            new_predictions.append("C")
    predictions = new_predictions[:-1]

    np.savetxt(OUTPUT_MR, predictions, fmt="%c")


if __name__ == '__main__':
    pass
