import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

def generate_input(k: int, n: int):
    if k > 26:
        raise ValueError('There are only 26 characters in the English alphabet.')

    text = f"{k}\n"
    used_values = []
    for i in range(k):
        val = random.randint(1, k)
        while val in used_values:
            val = random.randint(1, k)
        used_values.append(val)
        text += f"{alphabet[i]} {val}\n"

    for i in range(n):
        text += random.choice(alphabet[:k])
    text += "\n"
    for i in range(n):
        text += random.choice(alphabet[:k])

    return text

if __name__ == "__main__":
    text = generate_input(5, 10)
    print(text)