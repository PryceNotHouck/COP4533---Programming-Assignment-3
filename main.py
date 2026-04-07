from input_generator import *
from max_subsequence import *
from parse_input import *
import time
from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    # ex_characters = {'a': 2, 'b': 4, 'c': 5}
    # ex_sequences = ['aacab', 'caab']


    #k = number of letters, n = length of strings
    #randomly selects letters to use, constructs two strings randomly of length n given the randomly selected k letters
    # text = generate_input(5, 10)
    
    input_sizes = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
    #generate 10 inputs of length n, dictated by the input_size list (10 total inputs/files)
    for i in range(1,11):
        input_size = input_sizes[i-1]
        text = generate_input(5, input_size)
        filename = f"input{i}.txt"
        with open(filename, "w") as f:
            f.write(text)
            
    #determines runtime for each nth input HVLCS
    runtimes = []
    for n in range(1,11):
        start_t = time.perf_counter()
        with open(f"input{n}.txt", "r") as input_file:
            lines = input_file.read()
        characters, sequences = parse_input(lines)
        value, sequence = max_subsequence(characters, sequences)
        end_t = time.perf_counter()
        runtimes.append(end_t-start_t)
        

    #graph runtimes
    plt.scatter(input_sizes, runtimes, color='red', label='Runtimes')
    z = np.polyfit(x=input_sizes, y=runtimes, deg=len(input_sizes))
    p = np.poly1d(z)
    plt.plot(input_sizes, p(input_sizes), color='red')
    plt.title('Runtime analysis of HVLCS')
    plt.xlabel("Input Size (n)")
    plt.ylabel("Runtime (s)")
    plt.legend()
    plt.grid(True)
    plt.show()
    
    # #converts input_generator text into dictionary, list values
    # lines = text.strip().split("\n")
    # print(lines)
    # entries = lines[0]
    # entry_vals = lines[1:int(entries)]
    # print(entries)
    # input_dict = {}
    # sequence_list = []
    # for line in entry_vals:
    #     key, val = line.split()
    #     input_dict[key] = int(val)
    # sequence_list = lines[-2:]    
    
    # print(input_dict)
    # print(sequence_list)

    # print("MAX SUBSEQUENCE CALCULATIONS:")
    
    # value, sequence = max_subsequence.max_subsequence(input_dict, sequence_list)
    # print(value)
    # print(sequence)
    
