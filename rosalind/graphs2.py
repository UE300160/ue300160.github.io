#!/usr/bin/env python

# overlap graphs

def read_fasta(file):
    sequences = {}
    current_id = ""
    with open(file, 'r') as fasta:
        for line in fasta:
            line = line.strip()
            if line.startswith(">"): # could also be: line[0] == ">":
                # print("This line is a header:")
                header = line
                # print(header)
                # this is a header
                # we only care about this header from now on
                current_id = header[1:]
                sequences[current_id] = ""
            else:
                # print("this is a sequence:")
                sequence = line
                # print("we currently belong to sequence", current_id)
                # print(sequence)
                # it is a sequence
                sequences[current_id] = sequences[current_id] + sequence
    return sequences

def overlaps(seq1, seq2):
    if seq1[-3:] == seq2[:3]:
        return True
    return False
    # return seq1[-3:] == seq2[:3]


def main():
    fasta = read_fasta('../rosalind_data/rosalind_grph.txt')
    for h1, seq1 in fasta.items():
        for h2, seq2 in fasta.items():
            if h1 == h2:
                continue
            if overlaps(seq1, seq2):
                print(h1, h2)


if __name__ == '__main__':
    main()