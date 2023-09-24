class sequnce_class():
    def __init__(self,s="..."):
              self.seq=s

    def translate(self):
            com=''
            for i in self.seq.upper():
                if i not in "ATGC":
                    print("invalid input!Enter:>>ATGC")
                    break
            else: 
                for i in self.seq.upper():
                    if i == 'A':
                        com+='T'
                    if i == 'T':
                        com+='A'
                    if i == 'G':
                        com+='C'
                    if i == 'G':
                        com+='G'
                print(f'>>Complement: {com}')
                rna=com.replace('T','U')
                print(f'>>RNA: {rna}')
                if rna.startswith("AUG"):
                    print('>>ORF: {rna}')
                else:
                    print('>>ORF not found!')
def read_seq(input_seq):
    dna_seq = sequnce_class(input_seq)
    dna_seq.translate()
    
input_file="rat.fasta"
with open (input_file,'r')as obj:
    header=None
    seq=''
    sequence_list=[]

    for line in obj:
        line=line.strip()
        if line.startswith('>'):
            if header is not None:
                sequence_list.append((header,seq))
            header=line
            seq=''
        else:
            seq+=line
    if header is not None:
        sequence_list.append((header,seq))

    for i ,(header,seq) in enumerate(sequence_list):
            print(f'Sequence: {i+1}\n>>Header: {header}')
            print(f'>>DNA: {seq}')
            read_seq(seq)
            print('\n')
                
o1=sequnce_class("ATGCATGC")
o1.translate()


