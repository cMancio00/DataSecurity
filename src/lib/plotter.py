import seaborn as sns
from matplotlib import pyplot as plt
from os import mkdir

def make_histogram(frequency: dict[str, float]):
    sns.set_theme()
    plt.title("Frequency analysis")
    plt.xlabel("Letters")
    plt.ylabel("Frequency")
    sns.barplot(x=list(frequency.keys()), y=list(frequency.values()), palette="Blues_d")
    try:
        plt.savefig("Pictures/Frequency_analysis.png")
    except FileNotFoundError:
        mkdir("Pictures")
        plt.savefig("Pictures/Frequency_analysis.png")
    print("\033[0;32mSaved Histogram to Pictures/Frequency_analysis.png\033[0;0m")