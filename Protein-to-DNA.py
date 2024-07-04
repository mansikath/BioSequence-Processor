def read(filename):
    protein_dict={}
    with open(filename,"r")as file:
        content=file.read().split(">")
        for lines in content[1:]:
            lines=lines.split("\n")
            header=lines[0].strip()
            seq_lines = lines[1:]

            sequence = ""
            for line in seq_lines:
                if line.strip():s
                    sequence += line.strip()

                protein_dict[header] = sequence


    return protein_dict
        
def codon_table(filename):
    codon_dict={}
    with open(filename,"r")as file:
        content=file.readlines()
        for line in content[1:]:
            parts=line.split()
            if len(parts)>=4:
                codon=parts[0]
                aminoacid=parts[2]
                codon_dict[aminoacid]=codon
        return codon_dict
    
def protein_dna(protein_seq,codon_table):
    dna=""
    for aa in protein_seq:
        if aa in codon_table:
            dna+=codon_table[aa]
        else:
            pass
    return dna

#main 
protein_dict=read("human_pro.fasta")
codon_dict=codon_table("codon.txt")

for header, seq in protein_dict.items():
    dna=protein_dna(seq, codon_dict)
    print(f"Protein: {seq}")
    print(f"DNA: {dna}")
    print()


