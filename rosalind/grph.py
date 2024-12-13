#!/usr/bin/env python

from util import read_fasta

# intro to graph theory

def overlaps(seq1, seq2, k=3):
    return seq1[-k:] == seq2[:k]

def main():
    fasta = read_fasta('../rosalind_data/rosalind_grph.txt')
    for seq_i in fasta:
        for seq_j in fasta:
            if seq_i == seq_j:
                continue
            if overlaps(fasta[seq_i], fasta[seq_j]):
                print(seq_i, seq_j)

if __name__ == '__main__':
    main()