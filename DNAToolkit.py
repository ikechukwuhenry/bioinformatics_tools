import collections


# Check the sequence to make sure it is a DNA string
def validateSeq(seq, Nucleotides):
    tempSeq = seq.upper()
    for nuc in tempSeq:
        if nuc not in Nucleotides:
            return False
    return tempSeq

def validateDNASeq(dna_seq, dna_nucleotides):
    return validateSeq(dna_seq, dna_nucleotides)

def validateRNASeq(rna_seq, rna_nucleotides):
    return validateSeq(rna_seq, rna_nucleotides)

def countNucFreq(seq):
    # tempFreqDict = {"A": 0, "C": 0, "G": 0, "T": 0 }
    # for nuc in seq:
    #     tempFreqDict[nuc] += 1
    # return tempFreqDict
    return dict(collections.Counter(seq))