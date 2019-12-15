__author__ = "Nantia Leonidou"
__description__ = " Reverse Complement of fasta files "

from Bio.Seq import Seq
from Bio import SeqIO

input = "assembly.fasta"
def reverse_complement(file):
    revCompls =[]
    fasta_sequences = SeqIO.parse(open(file), 'fasta')
    for fasta in fasta_sequences:
        sequence = fasta.seq
        revCompls.append(sequence.reverse_complement())
    return revCompls

# compute reverse complement of assembly
revCompl = reverse_complement("assembly.fasta")
print(revCompl)


# writes output file containing reverse complement and sequence name
f = open('assembly_revComplement.fasta', "w")
records = list(SeqIO.parse("assembly.fasta", "fasta"))
for i in range(len(records)):
    #print(records[i].id)
    f.write(">" + str(records[i].id) + "\n" + str(revCompl[i]))
f.close()
