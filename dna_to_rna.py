
def transcribe_dna_to_rna(dna_sequence):
    rna_sequence = []
    for base in dna_sequence.upper():
        if base == "T":
            rna_sequence.append("U")
        else:
            rna_sequence.append(base)
    print(''.join(rna_sequence))



