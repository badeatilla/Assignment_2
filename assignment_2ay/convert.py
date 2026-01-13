from Bio import SeqIO
import os

fasta_files = [f for f in os.listdir() if f.endswith(".fasta")]

print("Found FASTA files:", fasta_files)

for fasta in fasta_files:
    print("\nProcessing:", fasta)

    records = list(SeqIO.parse(fasta, "fasta"))
    for record in records:
        print("Sequence ID:", record.id)

    output_file = fasta.replace(".fasta", ".gb")

    try:
        SeqIO.convert(fasta, "fasta", output_file, "genbank")
        print("Created:", output_file)
    except ValueError as e:
        print("GenBank conversion failed:", e)
        print("Continuing with next file...")
