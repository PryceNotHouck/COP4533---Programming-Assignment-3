from collections import deque

ex_characters = {'a': 2, 'b': 4, 'c': 5}
ex_sequences = ['aacab', 'caab']
#expected output:
# 13
# caab


# MAXIMUM SUBSTRING INTERPRETATION OF THE QUESTION:
# def max_subsequence(characters: dict, sequences: list):
#     common = {}
#     A = sequences[0]
#     B = sequences[1]
#     longest = A if len(A) > len(B) else B
#
#     subsequences = set()
#     for i in range(len(longest)):
#         j = i + 1
#         while j <= len(longest):
#             subsequences.add(longest[i:j])
#             j += 1
#
#     for sub in subsequences:
#         value = 0
#         for i in sub:
#             value += characters[i]
#
#         if longest == A:
#             if sub in B:
#                 common[sub] = value
#         else:
#             if sub in A:
#                 common[sub] = value
#
#     max_value = max(common.values())
#     max_sequence = [key for key, value in common.items() if value == max_value][0]
#
#     return max_value, max_sequence

def is_common(deq, sequence):
    subsequence = sequence
    while len(deq) != 0:
        curr = deq.popleft()
        found = subsequence.find(curr)
        if found != -1:
            subsequence = subsequence[found:]
        else:
            return False
    return True

def max_subsequence(characters: dict, sequences: list):
    common = {}
    A = sequences[0]
    B = sequences[1]
    A_subsequences = set()
    B_subsequences = set()

    for i in range(len(A)):
        j = i + 1
        while j <= len(A):
            A_subsequences.add(A[i:j])
            j += 1

    for i in range(len(B)):
        j = i + 1
        while j <= len(B):
            B_subsequences.add(B[i:j])
            j += 1
    A_subsequences = sorted(list(A_subsequences))
    B_subsequences = sorted(list(B_subsequences))

    for sub in A_subsequences:
        value = 0
        for i in sub:
            value += characters[i]

        if sub in B_subsequences:
            common[sub] = value
            continue

        sub_split = deque(sub)
        if is_common(sub_split, B):
            common[sub] = value

    for sub in B_subsequences:
        value = 0
        for i in sub:
            value += characters[i]

        if sub in A_subsequences:
            common[sub] = value
            continue

        sub_split = deque(sub)
        if is_common(sub_split, A):
            common[sub] = value

    max_value = max(common.values())
    max_sequence = [key for key, value in common.items() if value == max_value][0]

    return max_value, max_sequence

if __name__ == '__main__':
    print(ex_characters)
    print(ex_sequences)
    value, sequence = max_subsequence(ex_characters, ex_sequences)
    print(value)
    print(sequence)