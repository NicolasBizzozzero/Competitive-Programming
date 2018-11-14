import numpy as np
import matplotlib.pyplot as plt

from src.utils.array import get_diagonal_mask


def plot_correlation_matrix(df, size=8, cmap="plasma", masked=False,
                            show=True):
    """ Plot a graphical correlation matrix for each pair of columns in the
    dataframe.

    :param df: pandas DataFrame.
    :param size: Vertical and horizontal size of the plot.
    :param cmap: The ColorMap used to display the result. See :
    https://matplotlib.org/tutorials/colors/colormaps.html
    :param masked: Mask the upper diagonal of the heatmap.
    :param show: Show the result plotted.
    """
    corr = df.corr()

    if masked:
        corr[get_diagonal_mask(corr.values)] = np.nan

    fig, ax = plt.subplots(figsize=(size + 1, size))
    img = ax.matshow(corr, cmap=cmap)
    fig.colorbar(img, ax=ax)
    ax.set_aspect('auto')
    plt.xticks(rotation=90)
    plt.xticks(range(len(corr.columns)), corr.columns)
    plt.yticks(range(len(corr.columns)), corr.columns)

    if show:
        plt.show()


if __name__ == '__main__':
    pass
