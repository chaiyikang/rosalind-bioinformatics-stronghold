import requests

# Step 1: Input string of IDs
input_string = '''P01046_KNL1_BOVIN
P09136
P10493_NIDO_MOUSE
P47002
P01047_KNL2_BOVIN
P19823_ITH2_HUMAN
A1UR66
P00748_FA12_HUMAN
P20840_SAG1_YEAST
P06870_KLK1_HUMAN
Q9D9T0
P28653_PGS1_MOUSE
P08709_FA7_HUMAN
A2Z669'''
ids = input_string.split('\n')

def solution(ids):
    result = []

    # Step 2: Query API and parse FASTA
    for rawId in ids:
        uniprot_id = rawId.split("_")[0]
        url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
        response = requests.get(url)

        if response.status_code != 200:
            print(f"Failed to fetch {uniprot_id}: {response.status_code}")
            continue

        fasta_lines = response.text.splitlines()
        sequence = ''.join(line for line in fasta_lines if not line.startswith('>'))
        matches = findMotifs(sequence)
        if not matches:
            continue
        result.append([rawId, matches])
    return result



def findMotifs(seq):
    result = []
    for start in range(0, len(seq) - 4 + 1):
        ss = seq[start: start + 4]
        if checkMotif(ss):
            result.append(start + 1)
    return result


def checkMotif(str):
    if str[0] == "N" and str[1] != "P" and (str[2] == "S" or str[2] == "T") and str[3] != "P":
        return True
    return False

sol = solution(ids)
for s in sol:
    print(s[0])
    print(" ".join(str(x) for x in s[1]))