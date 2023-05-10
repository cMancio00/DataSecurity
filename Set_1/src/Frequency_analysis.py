import numpy as np
from os import mkdir
from os.path import exists
from lib.plotter import make_histogram
from lib.text_processing import process_text_file
import logging

if not exists("Logs"):
    mkdir("Logs")
logging.basicConfig(format='%(message)s\n', filename='Logs/frequency_analysis.log', filemode='w', level=logging.INFO)

def calculate_index_of_coincidence(frequency:dict)->float:
    index_of_coincidence = 0.0
    for key in frequency:
        index_of_coincidence += frequency[key] ** 2
    logging.info("[INDEX OF COINCIDENCE]\n{index_of_coincidence}".format(index_of_coincidence = index_of_coincidence))
    return index_of_coincidence

def calculate_shannon_entropy(frequency:dict)->float:
    shannon_entropy = 0.0
    for key in frequency:
        shannon_entropy += (frequency[key]) * np.log2(frequency[key])
    shannon_entropy *= -1
    logging.info("[SHANNON ENTROPY]\n{shannon_entropy}".format(shannon_entropy = shannon_entropy))
    return shannon_entropy


def main():
    for i in range(1, 5):
        logging.info("[{i}-GRAM FREQUENCY]".format(i = i))
        frequency = process_text_file("Text/MobyDick_Chapter_1.txt", i)
        calculate_index_of_coincidence(frequency)
        calculate_shannon_entropy(frequency)
        if i == 1:
            make_histogram(frequency)
        logging.info(frequency)
        print("\033[1;32mDone with empirical distribution of {i}-gram\033[0;0m\nCheck log file for more information".format(i = i))

if __name__ == "__main__":
    main()