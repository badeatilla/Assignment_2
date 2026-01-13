from Bio import SeqIO
import os

fasta_files = [f for f in os.listdir() if f.endswith(".fasta")]

print("Found FASTA files:", fasta_files)

for fasta in fasta_files:
    for record in SeqIO.parse(fasta, "fasta"):
        print("Sequence ID:", record.id)

        gb_file = fasta.replace(".fasta", ".gb")

        with open(gb_file, "w") as gb:
            gb.write("LOCUS       {}\n".format(record.id))
            gb.write("DEFINITION  Protein sequence.\n")
            gb.write("ACCESSION   {}\n".format(record.id))
            gb.write("ORIGIN\n")

            seq = str(record.seq).lower()
            for i in range(0, len(seq), 60):
                gb.write("{:9d} {}\n".format(i + 1, seq[i:i + 60]))

            gb.write("//\n")
