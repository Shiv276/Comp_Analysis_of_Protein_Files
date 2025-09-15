masses = {
    "A": 71.03711,  "R": 156.10111, "N": 114.04293, "D": 115.02694,
    "C": 103.00919, "E": 129.04259, "Q": 128.05858, "G": 57.02146,
    "H": 137.05891, "I": 113.08406, "L": 113.08406, "K": 128.09496,
    "M": 131.04049, "F": 147.06841, "P": 97.05276,  "S": 87.03203,
    "T": 101.04768, "W": 186.07931, "Y": 163.06333, "V": 99.06841
}

mass_H2O = 18
mass_proton = 1


def digest_aspN(sequence):
    peptides = []
    start = 0
    for i in range(len(sequence)):
        if sequence[i] == "D" and i != 0:  
            peptides.append(sequence[start:i])
            start = i
    peptides.append(sequence[start:])
    return peptides
def mass_calculator(peptide):
    MW = 0
    for aa in peptide:
        MW += masses[aa]
    MW += mass_H2O + mass_proton
    return MW

sequence = "MSVIKMTDLDLAGKRVFIRADLNVPVKDGKVTSDARIRASLPTIELALKQGAKVMVTSHLGRPTEGEYNEEFSLLPVVNYLKDKLSNPVRLVKDYLDGVDVAEGELVVLENVRFNKGEKKDDETLSKKYAALCDVFVMDAFGTAHRAQASTHGIGKFADVACAGPLLAAELDALGKALKEPARPMVAIVGGSKVSTKLTVLDSLSKIADQLIVGGGIANTFIAAQGHDVGKSLYEADLVDEAKRLLTTCNIPVPSDVRVATEFSETAPATLKSVNDVKADEQILDIGDASAQELAEILKNAKTILWNGPVGVFEFPNFRKGTEIVANAIADSEAFSIAGGGDTLAAIDLFGIADKISYISTGGGAFLEFVEGKVLPAVAMLEERAKK"


aspN_peptides = digest_aspN(sequence)

pep_masses = [ ]
for pep in aspN_peptides:
    mass = mass_calculator(pep)
    pep_masses.append(mass)

with open("AspN_digest_peptides.txt", "w") as f:
    for fragments in aspN_peptides:
        f.write(str(fragments) + "\n")

with open("AspN_digest_masses.txt", "w") as f:
    for fragments in pep_masses:
        f.write(str(fragments) + "\n")