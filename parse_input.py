# 3
# a 2
# b 4
# c 5
# aacb
# caab
example = "3\na 2\nb 4\nc 5\naacb\ncaab"

def parse_input(text: str):
    characters = {}
    sequences = []
    alphabet_size_i = text.find('\n')
    cc = alphabet_size_i

    for i in range(int(text[alphabet_size_i - 1])):
        #characters.append((text[cc + 1], int(text[cc + 3])))
        characters[text[cc + 1]] = int(text[cc + 3])
        cc += 4
    cc += 1

    sequences.append(text[cc:text.find('\n', cc)])
    cc += len(sequences[0]) + 1
    sequences.append(text[cc:])

    return characters, sequences

if __name__ == "__main__":
    characters, sequences = parse_input(example)
    print(characters)
    print(sequences)