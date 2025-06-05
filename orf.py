import helpers 

def solution(input: str):
    
    dna = '''GTAAGGACTGGCGCGCGAAGCAGTAAAAGATAGTTGTCTCCTGTGAACTGGATAGGCGGCTCGGGATAGGAAGTATCCATTTTTATGACGGGCGCGGTGACAAATGATCCATCACAACCAGATGCCGGTAACCAAGTCCAATGTGTAGCAGAGGCACGACAGACCCTGGAATTCAGAGTGTATATGCACATGATGCCAGCGACTCATTCGCGTGGGGCGATGGTTGCCGCCTGCCCGGGGACAACCGCAAATCCAGTGAGCCGAATACCGTAAAGTTCTATCGCCAACCCGTCCGCGTTTGCGGCCCTGTTCCGCAAACGGGTCCCTTTATCGACTTCTGAAGAGTTCGTACTAAGGGCGTGACTCAATGGTCGTACCAATCAGAACGGGGTAGGGTCAATAACGCCGTGCAGAGTACATGCTGCACTCGCGCTACACCGCCTAGCTAGGCGGTGTAGCGCGAGTGCAGCATCTCTTCTTGGTAACTGTTAATCAGTCCATTGTTAATGCAATCTAACCAATGCTAGTCGACATCGAGCGCGTCTCACTTAGCGACACCTATGCCCTTGTGGACACGGGGTAAATGACATAGACTGTAACGGACGTGCGACATGTGTTACCGGTTATGAGCAGTACAGATAAATAAAGTCGGGGCAAACGCGATAACGAGTCATGCTGCCAGCTGTGGAGGGTCCCTGCTAGGTCGGGATGTGACATCGAGAAGGCTCGTGCGCAGCGTCAAGGAAAACGTACTCAAAATGGACTCGAAACTTAGCAAATTTTTCTGCCAAAGCGAATGCACGGGATCAACCTCCAGGATATCAGTATTGGATTTTTTTGAAGCTGCAGCTCCACTGTATCCGGTAATCTGTGGTGAAACAAGGACCTCC'''
    complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
    dnaComp = ''.join(complement[base] for base in reversed(dna))
    rna = dna.replace("T", "U")
    rnaComp = dnaComp.replace("T", "U")
    # print(rna)
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

    result = set()

    def solve(rna: str):
        def translate(rna: str) -> str:
            # print(rna)
            currCodon = ""
            result = ""
            for base in rna:
                currCodon += base
                if len(currCodon) == 3:
                    if geneticCode[currCodon] == "Stop":
                        return result
                    result += geneticCode[currCodon]
                    currCodon = ""
        
        currCodon = ""
        for i, base in enumerate(rna):
            currCodon += base
            if currCodon == "AUG":
                res = translate(rna[i - 2:])
                if res:
                    result.add(res)
            if len(currCodon) == 3:
                currCodon = ""
    for i in range(3):                
        solve(rna[i:])
        solve(rnaComp[i:])
    for rez in result:
        print(rez)

    

solution('''>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG''')


