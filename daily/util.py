codons = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": None, "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": None, "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": None, "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
}

def parse_fasta(lines_list):
    current_sequence = ''
    current_id = ''
    sequences = {}

    for line in lines_list:
        # if line.startswith('>'):
        if line[0] == '>':
            sequences[current_id] = current_sequence
            current_id = line[1:]
            current_sequence = ''
        else:
            current_sequence = current_sequence + line

    sequences[current_id] = current_sequence
    del sequences['']
    return sequences

def read_file_into_lines(file_path):
    """
    A simple function to read a file into
    a list of lines, removing the newline
    character at the end.

    Arguments:
    ==========
    file_path: str
        The location of a text file to read.

    Returns:
    ========
    list[str]
        A list that contains all stripped lines
        of the input text file.
    """
    lines = []
    with open(file_path, 'r') as infile:
        for line in infile.readlines():
            cleaned = line.rstrip()
            lines.append(cleaned)
    return lines

def read_fasta(fasta_file):
    lines = read_file_into_lines(fasta_file)
    fasta = parse_fasta(lines)
    return fasta

def reverse_complement(rna):
    # the reverse complement:
    revc = rna[::-1]
    revc = revc.replace('A', 'u')
    revc = revc.replace('U', 'a')
    revc = revc.replace('G', 'c')
    revc = revc.replace('C', 'g')
    revc = revc.upper()
    return revc