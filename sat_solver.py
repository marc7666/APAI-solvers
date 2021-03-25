import csv


# Lleigr fitxer cnf amb les formules
def read_file(input_file):
    clauses = []
    with open(input_file) as file:
        for line in file:
            if line.startswith('c'):  # Comment line
                continue
            elif line.startswith('p'):  # Statement line
                continue
            else:
                clause = [int(x) for x in line[:-2].split()]
                # line[:-2] omits the two last characters. In this case, we are omitting the last character "\n" and the penultimate character "0"
                '''Each clause is going to be formed by literals. In this case, '+/-x' will denote a literal (a 
                variable with either positive or negative sign). '-/+x' is therefore the same variable with its sign 
                flipped '''
                clauses.append(clause)  # Appending each clause to the list of clauses
    file.close()  # Closing the document
    return clauses  # Returning all of the clauses

# Propagació unitaria
# Eliminació de literals purs
# Backtracking
# Output
