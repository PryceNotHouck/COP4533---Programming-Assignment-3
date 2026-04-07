from input_generator import *
from max_subsequence import *
from parse_input import *
import time
from matplotlib import pyplot as plt
import numpy as np


if __name__ == "__main__":
    
    #adjust input sizes here
    input_sizes = [25, 50, 75, 100, 125, 150, 175, 200, 225, 250]
    char_num = 5
    #generate 10 inputs of length n, dictated by the input_size list (10 total inputs/files)
    for i in range(1,11):
        input_size = input_sizes[i-1]
        text = generate_input(char_num, input_size)
        filename = f"input{i}.txt"
        with open(filename, "w") as f:
            f.write(text)
            
    #recoreds runtime for each nth input HVLCS
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