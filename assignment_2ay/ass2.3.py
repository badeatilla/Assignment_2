def parse_fasta_file(file_path):
    file_obj=open(file_path,"r")
    fastasequence={}
    for line in file_obj:
        if line.startswith(">"):
            line1=line.lstrip(">")
            name=line1.rstrip("\n")
        else:
            sequence=line.rstrip("\n")
            fastasequence[name]=sequence
    file_obj.close()
    return fastasequence   
    
fastasequence = parse_fasta_file(r"test.fasta")
print(fastasequence)
