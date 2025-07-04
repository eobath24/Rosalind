
def motif_finder(sequence, motif):
    reversed_motif = ''.join(reversed(list(motif)))

    motif_position = []
    motif_count = 0

    rev_motif_position = []
    rev_motif_count = 0

    if motif == "":
        print("Please input a motif")
    else:
        for base in range(len(sequence)):
            if sequence[base: base + len(motif)] == motif:
                motif_position.append(base +1) # index 0 will now be 1. every index now has +1
                motif_count += 1
            elif sequence[base: base + len(reversed_motif)] == reversed_motif:
                rev_motif_position.append(base +1)
                rev_motif_count += 1
            else:
                continue

        print(f"{motif}: count = {motif_count}, positions = {motif_position}")
        print(f"{reversed_motif}: count = {rev_motif_count}, positions = {rev_motif_position}")



#Function only takes one motif
# going to create a seprate function to take an unknown number of motifs, seoartae each one, then pass it theough this function

import os

with open(os.path.expanduser(r"C:\Users\Ella\Downloads\rosalind_subs(1).txt")) as f:
    sequence = f.read().replace("\n", "n")

motif_finder(sequence, "A")



print()

# Motif seperator #

import os

with open(os.path.expanduser(r"C:\Users\Ella\Downloads\rosalind_subs(1).txt")) as f:
    sequence = f.read().replace("\n", "")
with open(os.path.expanduser(r"C:\Users\Ella\Downloads\motifs.txt")) as f:
    motifs = f.read()
    motifs_list = (motifs.split(", "))
    for motif in motifs_list:
        motif_finder(sequence, motif)














