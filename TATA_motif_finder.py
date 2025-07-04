# TATA motif finder

def tata_finder(dna_seq, motif1 = "TATAAA", motif2 = "TATAAT"):


    motif1_rev = ''.join(reversed(list(motif1)))
    motif2_rev = ''.join(reversed(list(motif2)))

    m1_tataaa_position = []
    m2_tataat_position = []
    m1r_aaatat_position = []
    m2r_taatat_position = []

    m1_tataaa_count = 0
    m2_tataat_count = 0
    m1r_aaatat_count = 0
    m2r_taatat_count = 0

    for base in range(
            len(dna_seq.upper())):  #can now iterate over the length of seq from 0-end. the base will be the index postion
        if dna_seq[base: base + len(motif1)] == motif1.upper():
            m1_tataaa_position.append(base)
            m1_tataaa_count += 1
        elif dna_seq[base: base + len(motif2)] == motif2.upper():
            m2_tataat_position.append(base)
            m2_tataat_count += 1
        elif dna_seq[base: base + len(motif1_rev)] == motif1_rev.upper():
            m1r_aaatat_position.append(base)
            m1r_aaatat_count += 1
        elif dna_seq[base: base + len(motif2_rev)] == motif1_rev.upper():
            m2r_taatat_position.append(base)
            m2r_taatat_count += 1
        else:
            continue
    print(f"{motif1}: positions = {m1_tataaa_position}. Count = {m1_tataaa_count}")
    print(f"{motif2}: positions = {m2_tataat_position}. Count = {m2_tataat_count}")
    print(f"{motif1_rev}: positions = {m1r_aaatat_position}. Count = {m1r_aaatat_count}")
    print(f"{motif2_rev}: positions = {m2r_taatat_position}. Count: {m2r_taatat_count}")


tata_finder("")