def parse_fasta(fasta_str):
    ids = []
    sequences = []
    current_seq = []

    for line in fasta_str.strip().splitlines():
        line = line.strip()
        if line.startswith(">"):
            if current_seq:
                sequences.append(''.join(current_seq))
                current_seq = []
            ids.append(line[1:])  # remove '>'
        else:
            current_seq.append(line)
    
    if current_seq:
        sequences.append(''.join(current_seq))

    return ids, sequences

def translate(rna):
    geneticCode = {
    "UUU": "F", "CUU": "L", "AUU": "I", "GUU": "V",
    "UUC": "F", "CUC": "L", "AUC": "I", "GUC": "V",
    "UUA": "L", "CUA": "L", "AUA": "I", "GUA": "V",
    "UUG": "L", "CUG": "L", "AUG": "M", "GUG": "V",
    "UCU": "S", "CCU": "P", "ACU": "T", "GCU": "A",
    "UCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
    "UCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
    "UCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
    "UAU": "Y", "CAU": "H", "AAU": "N", "GAU": "D",
    "UAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
    "UAA": "Stop", "CAA": "Q", "AAA": "K", "GAA": "E",
    "UAG": "Stop", "CAG": "Q", "AAG": "K", "GAG": "E",
    "UGU": "C", "CGU": "R", "AGU": "S", "GGU": "G",
    "UGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
    "UGA": "Stop", "CGA": "R", "AGA": "R", "GGA": "G",
    "UGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"
    }
    currCodon = ""
    result = ""
    for base in rna:
        currCodon += base
        if len(currCodon) == 3:
            if geneticCode[currCodon] == "Stop":
                return result
            result += geneticCode[currCodon]
            currCodon = ""
    return ""

