# a library of utility functions for Rosalind exercises

def read_input(filepath):
    with open(filepath, 'r') as infile:
        lines = infile.readlines()
        stripped = []
        for line in lines:
            stripped.append(line.strip())
    return stripped


def read_fasta(path):
    sequences = {}
    current_id = ""
    with open(path, 'r') as fasta:
        for line in fasta:
            line = line.strip()
            if line.startswith(">"):
                header = line
                current_id = header[1:]
                sequences[current_id] = ""
            else:
                sequence = line
                sequences[current_id] = sequences[current_id] + sequence
    return sequences