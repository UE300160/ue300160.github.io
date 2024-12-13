#!/usr/bin/env python

# profile and consensus

from util import read_fasta

def base_frequencies(seq_dict):
    first_seq = list(seq_dict.values())[0]
    n = len(first_seq)
    counter = {
        'A': [0] * n,
        'T': [0] * n,
        'C': [0] * n,
        'G': [0] * n,
    }

    for i in range(n):
        for _, seq in seq_dict.items():
            base = seq[i]
            counter[base][i] += 1
    return counter

def consensus_at_position(frequencies, i):
    max_val = 0
    max_key = ''
    for k in frequencies:
        if frequencies[k][i] > max_val:
            max_val = frequencies[k][i]
            max_key = k
    return max_key

def find_consensus(frequencies, length):
    consensus = ''
    for i in range(length):
        consensus += consensus_at_position(frequencies, i)
    return consensus

def main():
    fasta = read_fasta('../rosalind_data/rosalind_cons.txt')
    freqs = base_frequencies(fasta)
    consensus = find_consensus(freqs, len(freqs['A']))

    print(consensus)
    for b in ['A', 'C', 'G', 'T']:
        content = " ".join([str(c) for c in freqs[b]])
        print(f'{b}: {content}')

    


if __name__ == '__main__':
    main()