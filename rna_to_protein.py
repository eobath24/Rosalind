
def rna_to_protein(rna_sequence: str):
    rna_sequence = rna_sequence.upper()
    """ Translates RNA sequences into protein. Input: single RNA sequence. Output: protein string in single
    amino acid code"""

    codons = {
        'UUU': 'F', 'CUU': 'L', 'AUU': 'I', 'GUU': 'V', 'UUC': 'F', 'CUC': 'L', 'AUC': 'I', 'GUC': 'V',
        'UUA': 'L', 'CUA': 'L', 'AUA': 'I', 'GUA': 'V', 'UUG': 'L', 'CUG': 'L', 'AUG': 'M', 'GUG': 'V',
        'UCU': 'S', 'CCU': 'P', 'ACU': 'T', 'GCU': 'A', 'UCC': 'S', 'CCC': 'P', 'ACC': 'T', 'GCC': 'A',
        'UCA': 'S', 'CCA': 'P', 'ACA': 'T', 'GCA': 'A', 'UCG': 'S', 'CCG': 'P', 'ACG': 'T', 'GCG': 'A',
        'UAU': 'Y', 'CAU': 'H', 'AAU': 'N', 'GAU': 'D', 'UAC': 'Y', 'CAC': 'H', 'AAC': 'N', 'GAC': 'D',
        'UAA': '', 'CAA': 'Q', 'AAA': 'K', 'GAA': 'E', 'UAG': '', 'CAG': 'Q', 'AAG': 'K', 'GAG': 'E',
        'UGU': 'C', 'CGU': 'R', 'AGU': 'S', 'GGU': 'G', 'UGC': 'C', 'CGC': 'R', 'AGC': 'S', 'GGC': 'G',
        'UGA': '', 'CGA': 'R', 'AGA': 'R', 'GGA': 'G', 'UGG': 'W', 'CGG': 'R', 'AGG': 'R', 'GGG': 'G'
    }

    proteins = []
    for codon in range(0, len(rna_sequence), 3): #will read sequence 3 at a time now
        triplet = rna_sequence[codon:codon + 3]
        proteins.append(codons[triplet])
    print(''.join(proteins))


# Executing function #
import os

with open(os.path.expanduser(r"C:\Users\Ella\Downloads\rosalind_prot.txt")) as f:
    rna_sequence = f.read().replace("\n", "")

rna_to_protein(rna_sequence)








