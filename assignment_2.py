import Bio
print(Bio.__version__)
from Bio import SeqIO




def convert_to_genbank(seq_file_path,output_path):
    seq_handle=SeqIO.parse(seq_file_path,"fasta")
    for seq_record in seq_handle:
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))

    count=SeqIO.write(seq_handle,output_path,"genbank")
    print("Converted %i records" % count)

    
    records = []

    for record in SeqIO.parse(seq_file_path, "fasta"):
        record.annotations["molecule_type"] = "protein"  
        records.append(record)

    count = SeqIO.write(records, output_path, "genbank")
    print(f"{seq_file_path} Converted {count} records")


convert_to_genbank(r"DNA polymerase I [Escherichia coli].fasta" ,
                   r"DNA polymerase I [Escherichia coli].genbank")

convert_to_genbank(r"16S rRNA methyltransferase [Tumebacillus flagellatus].fasta" ,
                   r"16S rRNA methyltransferase [Tumebacillus flagellatus].genbank")


convert_to_genbank(r"WRN RecQ like helicase [Homo sapiens].fasta" ,
                   r"WRN RecQ like helicase [Homo sapiens].genbank")