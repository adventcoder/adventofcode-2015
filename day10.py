from utils import get_input
from itertools import groupby
import numpy as np
import re

def looksay(seq):
    return ''.join(str(len(list(v))) + k for k, v in groupby(seq))

def split(seq):
    # We can split where the start of a subsequence never again interacts with the end of the previous subsequence.
    #
    # Ultimately this is a result of the following cycle (which never starts with a 2):
    # 
    # 12[^2] -> 111
    # 13[^3] -> 111
    # 111 -> 31
    # 31 -> 131
    # 32[^2] -> 131
    # 322[^2] -> 132
    #
    # Or of the cycle (which always starts with a 2):
    #
    # 22 -> 22 (provided that the sequence following doesn't interact with it, as above)
    #
    split_pattern = r'12[^2]|13[^3]|111|31|32[^2]|322[^2]'
    chunks = []
    start = 0
    for i in range(1, len(seq)-2):
        if ((seq[i-1] == '2' and re.match(split_pattern, seq[i:i+4])) or
            (seq[i-1] != '2' and seq[i:i+2] == '22' and re.match(split_pattern, seq[i+2:i+6]))):
            chunks.append(seq[start:i])
            start = i
    chunks.append(seq[start:])
    return chunks

stack = ['3']
elements = { '3': 0 }
while stack:
    seq = stack.pop()
    for subseq in split(looksay(seq)):
        if subseq not in elements:
            elements[subseq] = len(elements)
            stack.append(subseq)

def count_elements(seq):
    counts = np.zeros(len(elements), dtype=int)
    for subseq in split(seq):
        counts[elements[subseq]] += 1
    return counts

lengths = np.zeros(len(elements), dtype=int)
for subseq in elements:
    lengths[elements[subseq]] = len(subseq)

matrix = np.column_stack([count_elements(looksay(seq)) for seq in elements])
counts = count_elements(get_input(10).strip())

counts = np.dot(np.linalg.matrix_power(matrix, 40), counts)
print('1.', np.dot(counts, lengths))

counts = np.dot(np.linalg.matrix_power(matrix, 10), counts)
print('2.', np.dot(counts, lengths))
