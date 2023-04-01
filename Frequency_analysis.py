import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from os import mkdir
from collections import Counter

def read_text_file(text_file: str) -> str:
        text = open(text_file, "r")
        while True:
            line = text.readline()
            if not line:
                break
            yield line

def remove_special_characters(line: str) -> str:
    characters_to_remove = [" ",",",".",";","`","'","!","?","(",")","[","]","{","}","<",">","/",":", \
                            "\"","|","@","#","$","%","^","&","*","-","+","=","_","~","0","1","2","3","4","5","6","7","8","9"]
    for character in characters_to_remove:
        line = line.replace(character, "")
    return line.upper()

def sort_by_name(dictionary: dict[str, float]) -> dict[str, float]:
    return {key: value for key, value in sorted(dictionary.items(), key=lambda item: item[0])}

def calculate_frequency(dictionary: dict[str, int]) -> dict[str, float]:
    total = sum(dictionary.values())
    return {key: value/total for key, value in dictionary.items()}


def process_text_file(text: str) -> dict[str, int]:
    text_gen = read_text_file(text)
    count = Counter()
    for line in text_gen:
        line = remove_special_characters(line)
        count.update(line)
    count = dict(count)
    count.pop("\n")
    frequency = calculate_frequency(count)
    return sort_by_name(frequency)
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

def main():

    frequency = process_text_file("MobyDick_Chapter_1.txt")
    make_histogram(frequency)


if __name__ == "__main__":
    main()