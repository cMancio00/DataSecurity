import numpy as np
from os import mkdir
from os.path import exists
from lib.plotter import make_histogram
from lib.text_processing import process_text_file
import logging

if not exists("Logs"):
    mkdir("Logs")
logging.basicConfig(format='%(message)s\n', filename='Logs/frequency_analysis.log', filemode='w', level=logging.INFO)

def main():
    for i in range(1, 5):
        logging.info("[{i}-GRAM FREQUENCY]".format(i = i))
        frequency = process_text_file("Text/MobyDick_Chapter_1.txt", i)
        if i == 1:
            make_histogram(frequency)
        logging.info(frequency)
        print("\033[1;32mDone with empirical distribution of {i}-gram\033[0;0m\nCheck log file for more information".format(i = i))

if __name__ == "__main__":
    main()