
def complementary_reversed_strand(dna_sequence):
    complementary_sequence = []
    uppercase_sequence = dna_sequence.upper()


    for base in uppercase_sequence:
        if base == "G":
            complementary_sequence.append("C")
        elif base == "C":
            complementary_sequence.append("G")
        elif base == "A":
            complementary_sequence.append("T")
        elif base == "T":
            complementary_sequence.append("A")
        elif base != ("A", "G", "C", "T"):
            print(f"Base unknown: {base}, position: {uppercase_sequence.find(base)}")
            break
        else:
            continue

    reversed_complement = ''.join(reversed(complementary_sequence))
    return reversed_complement


complentary_strand("ATCGATCNGATCGGTA")