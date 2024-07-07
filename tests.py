from DNAToolkit import *
import random

# Creating a random DNA sequence for testing:
DNA_nucleotides = ["A", "C", "G", "T"]
RNA_nucleotides = ["A", "C", "G", "U"]
randDNASeq = ''.join([random.choice(DNA_nucleotides) for nuc in range(50)])
randRNASeq = ''.join([random.choice(RNA_nucleotides) for nuc in range(60)])

DNASeq = validateDNASeq(randDNASeq, DNA_nucleotides)
RNASeq = validateRNASeq(randRNASeq, RNA_nucleotides)
print(DNASeq)
print(countNucFreq(DNASeq))

print(RNASeq)
print(countNucFreq(RNASeq))