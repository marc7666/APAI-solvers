import csv


# Lleigr fitxer cnf amb les formules
def read_file(input_file):
    clauses = []
    with open(input_file) as file:
        for line in file:
            if line.startswith('c'):
                continue
            elif line.startswith('p'):
                continue
            else:
                clause = [int(x) for x in line[:-2].split()]
                clauses.append(clause)
    file.close()
    return clauses

# Propagació unitaria
# Eliminació de literals purs
# Backtracking
# Output
