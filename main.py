import input_generator
import max_subsequence
import parse_input

if __name__ == "__main__":
    ex_characters = {'a': 2, 'b': 4, 'c': 5}
    ex_sequences = ['aacab', 'caab']

    text = input_generator.generate_input(5, 10)
    print("SOI")
    print(text)
    print("EOI")
    
    
    #converts input_generator text into dictionary, sequence values
    lines = text.strip().split("\n")
    print(lines)
    entries = lines[0]
    entry_vals = lines[1:int(entries)]
    print(entries)
    input_dict = {}
    sequence_list = []
    for line in entry_vals:
        key, val = line.split()
        input_dict[key] = int(val)
    sequence_list = lines[-2:]    
    
    print(input_dict)
    print(sequence_list)


    # value, sequence = max_subsequence.max_subsequence(ex_characters, ex_sequences)
    # print(value)
    # print(sequence)
    
    # for i in range(1,11):
    #     text = input_generator.generate_input(5, 25)
    #     filename = f"input{i}.txt"
        
    #     with open(filename, "w") as f:
    #         f.write(text)