
def fasta_file_sorter(fasta_file):
    f_dict = {}
    for line in fasta_file:
        # Adding lines to a dictionary
        if ">" in line:
            f_label = line.strip("\n")  # setting line as the key if it has >
            f_dict[f_label] = ""  # setting the value of the key to empty string  e.g >rosalind_xxxx : "",
        else:
            f_dict[f_label] += line.strip("\n")
    return f_dict




