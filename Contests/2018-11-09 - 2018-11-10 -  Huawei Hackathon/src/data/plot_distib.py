import matplotlib.pyplot as plt
import numpy as np

def plot_histo(file_name):
    true_label = 0
    false_label = 0

    y = []
    with open(file_name, 'r') as f:
        line = str(f.readlines()[0])
        for i in line:
            y.append(int(i))
            if int(i) == 1:
                true_label += 1
            else:
                false_label += 1
        print('true: ', true_label, 'false: ', false_label)

    x = np.arange(2)
    plt.figure()
    plt.bar(x, [true_label, false_label])
    plt.xticks(x, ('true_label', 'false_label'))
    plt.savefig('distribution_label.png')

plot_histo("../../../hackathon/true_labels_training.txt")

