def point_mutation_counter(sequence1, sequence2):
    point_mutation_count = 0

    for base in range(len(sequence1)): # since sequneces are of equal length the len() function will give same answer
        if sequence1[base] != sequence2[base]: #base is a number for indexing
            point_mutation_count +=1
        else:
            continue

    return(point_mutation_count)


point_mutation_counter(sequence1, sequence2)
