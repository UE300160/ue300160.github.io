#!/usr/bin/env python

from util import read_fasta
from prot import translate

# easy splicing

def read_first_sequence(path):
    with open(path, 'r') as fasta:
        return fasta.readline().strip()[1:]

def splice(dna, introns):
    for intron in introns:
        dna = dna.replace(intron, '')
    return dna



def main():
    sequences = read_fasta('../rosalind_data/rosalind_splc.txt')
    first = read_first_sequence('../rosalind_data/rosalind_splc.txt')
    
    dna = sequences[first]
    introns = [sequences[intron] for intron in sequences if intron != first]

    cdna = splice(dna, introns)
    mrna = cdna.replace('T', 'U')
    peptide = translate(mrna)
    print(peptide)
    

if __name__ == '__main__':
    main()