def solution(input_str: str):
    dna = input_str.strip().splitlines()[1]
    
    # Genetic code table
    genetic_code = {
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
    
    def reverse_complement(dna_seq):
        complement = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
        return ''.join(complement[base] for base in reversed(dna_seq))
    
    def find_orfs_in_frame(rna_seq):
        orfs = []
        i = 0
        while i < len(rna_seq) - 2:
            # Look for start codon AUG
            if rna_seq[i:i+3] == "AUG":
                # Found start codon, now translate until stop codon
                protein = "M"  # Start with methionine
                j = i + 3
                
                while j < len(rna_seq) - 2:
                    codon = rna_seq[j:j+3]
                    if len(codon) < 3:
                        break
                    
                    if genetic_code[codon] == "Stop":
                        # Found complete ORF
                        orfs.append(protein)
                        break
                    else:
                        protein += genetic_code[codon]
                    j += 3
            i += 1
        return orfs
    
    def get_all_orfs(dna_seq):
        all_orfs = []
        
        # Convert to RNA
        rna = dna_seq.replace("T", "U")
        
        # Get ORFs from forward strand (3 reading frames)
        for frame in range(3):
            frame_rna = rna[frame:]
            all_orfs.extend(find_orfs_in_frame(frame_rna))
        
        # Get reverse complement and convert to RNA
        rev_comp = reverse_complement(dna_seq)
        rev_rna = rev_comp.replace("T", "U")
        
        # Get ORFs from reverse strand (3 reading frames)
        for frame in range(3):
            frame_rna = rev_rna[frame:]
            all_orfs.extend(find_orfs_in_frame(frame_rna))
        
        return all_orfs
    
    # Find all ORFs
    orfs = get_all_orfs(dna)
    
    # Remove duplicates and return
    unique_orfs = list(set(orfs))
    return unique_orfs

# Test with the sample
test_input = """>Rosalind_99
AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACTTGGATTAGAGTCTCTTTTGGAATAAGCCTGAATGATCCGAGTAGCATCTCAG"""

result = solution(test_input)
for orf in result:
    print(orf)