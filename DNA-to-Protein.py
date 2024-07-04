def read(filename):
    sequence_dict = {}  
    try:
        with open(filename, "r") as file:
            content = file.read().split(">")

            for data in content[1:]:
                lines = data.split("\n")
                header = lines[0].strip()
                seq_lines = lines[1:]

                sequence = ""
                for line in seq_lines:
                    if line.strip():
                        sequence += line.strip()

                sequence_dict[header] = sequence
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return sequence_dict

def codon_table(filename):
    codon_dict = {}
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            for line in lines[1:]:
                parts = line.split()
                if len(parts) >= 4:
                    codon = parts[0]
                    amino_acid = parts[2]
                    codon_dict[codon] = amino_acid
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return codon_dict

def dna_protein(seq, codon_dict):
    protein_list = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) == 3:
            if codon in codon_dict:
                amino_acid = codon_dict[codon]
                if amino_acid == "O":  # Stop codon
                    break
                protein_list.append(amino_acid)
            else:
                pass
    return "".join(protein_list)

def dna_rna(seq):
    rna = ""
    dna = seq.upper()
    for base in dna:
        if base not in "AGCT":
            raise ValueError("Invalid DNA sequence.")
        else:
            if base == "A":
                rna += "U"
            elif base == "T":
                rna += "A"
            elif base == "C":
                rna += "G"
            elif base == "G":
                rna += "C"
    return rna

# Main code
sequence_dict = read("C:\\python_learning\\human_nucl.fasta")
codon_dict = codon_table("C:\\python_learning\\codon.txt")
for header, seq in sequence_dict.items():
    print(f"Header: {header}")
    print(f"DNA: {seq}")
    rna = dna_rna(seq)
    print(f"RNA: {rna}")
    protein_seq = dna_protein(seq, codon_dict)
    print(f"Protein sequences: {protein_seq}")
    print()
