replacements = {"Al":("ThF","ThRnFAr"),
                "e":("HF", "NAl","OMg"),
                "Ti":("TiTi","BP"),
                "Th":("ThCa"),
				"Si":("CaSi"),
                "P":("SiRnFAr","PTi","CaP"),
                "O":("OTi","NRnFAr","HP","CRnMgAr","CRnFYFAr"),
				"N":("HSi","CRnFAr"),
                "Mg":("TiMg","BF"),
                "H":("ORnFAr","OB","NTh","NRnMgAr","NRnFYFAr","HCa","CRnMgYFAr","CRnFYMgAr","CRnFYFYFAr","CRnAlAr"),
				"F":("SiAl","PMg","CaF"),
                "Ca":("SiTh","SiRnMgAr","SiRnFYFAr","PRnFAr","PB","CaCa"),
                "B":("TiRnFAr","TiB","BCa")}

molecule = "CRnCaCaCaSiRnBPTiMgArSiRnSiRnMgArSiRnCaFArTiTiBSiThFYCaFArCaCaSiThCaPBSiThSiThCaCaPTiRnPBSiThRnFArArCaCaSiThCaSiThSiRnMgArCaPTiBPRnFArSiThCaSiRnFArBCaSiRnCaPRnFArPMgYCaFArCaPTiTiTiBPBSiThCaPTiBPBSiRnFArBPBSiRnCaFArBPRnSiRnFArRnSiRnBFArCaFArCaCaCaSiThSiThCaCaPBPTiTiRnFArCaPTiBSiAlArPBCaCaCaCaCaSiRnMgArCaSiThFArThCaSiThCaSiRnCaFYCaSiRnFYFArFArCaSiRnFYFArCaSiRnBPMgArSiThPRnFArCaSiRnFArTiRnSiRnFYFArCaSiRnBFArCaSiRnTiMgArSiThCaSiThCaFArPRnFArSiRnFArTiTiTiTiBCaCaSiRnCaCaFYFArSiThCaPTiBPTiBCaSiThSiRnMgArCaF"

distinct_molecules = set()

# Loop through the keys in the replacements dictionary
for key in replacements:
    # Find all positions of the key in the molecule string
    start = 0
    while start < len(molecule):
        # Look for the next occurrence of the key
        start = molecule.find(key, start)
        if start == -1:
            break
        
        # For each occurrence, try all possible replacements
        for replacement in replacements[key]:
            # Generate a new molecule with the replacement
            new_molecule = molecule[:start] + replacement + molecule[start + len(key):]
            # Add the new molecule to the set of distinct molecules
            distinct_molecules.add(new_molecule)
        
        # Move past this occurrence for the next iteration
        start += 1

# Output the number of distinct molecules
print(f"Number of distinct molecules: {len(distinct_molecules)}")