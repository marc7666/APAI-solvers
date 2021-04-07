#!/usr/bin/python
#######################################################################
# Code made by:
# Moises Bernaus Lechosa - 47903568L
# Marc Cervera Rosell - 47980320C
#######################################################################

# Libraries

from random import *
import sys
import numpy as np


# Classes

def cnf_parser(cnf):
    clauses = []
    vars = 0
    for line in cnf:
        line = line.split()
        if line[0] != 'c' and line[0] != 'p':
            clauses.append([int(x) for x in line[:-1]])
        elif line[0] == 'p':
            vars = line[2]
    return int(vars), clauses


def random_solution_generator(vars):
    solution = np.arange(1, vars + 1)
    for i in range(len(solution)):
        if random() < 0.5:
            solution[i] *= -1
    return solution


# This function returns the formula that results from the parameters of the function.

def data_structure(clauses, n_var):
    formula = []
    for i in range(n_var * 2):
        formula.append([])

    for c in range(len(clauses)):
        for x in clauses[c]:
            if x > 0:
                formula[x - 1].append(c)
            else:
                formula[x].append(c)
    return formula


# This function returns de number of the satisfiable literals.

def data_structure2(formula, solution):
    sat_literals = [0] * len(formula)
    count = 0
    for clauses in formula:
        for literal in clauses:
            if literal == solution[abs(literal) - 1]:
                sat_literals[count] += 1
        count += 1
    return sat_literals


def walk_sat(clauses, n_vars):
    formula = clauses
    data_structure(formula, n_vars)
    while 1:
        solution = random_solution_generator(n_vars)
        sat_literals = data_structure2(formula, solution)
        for i in range(3 * n_vars):
            zero_positions = [i for i, j in enumerate(sat_literals) if j == 0]
            print("c rober_sat")
            if len(zero_positions) == 0:
                return print("s SATISFIABLE" + "\nv " + ' '.join(str(e) for e in solution) + " 0")
            else:
                return print("s UNSATISFIABLE")
            x = zero_positions[randint(0, len(zero_positions) - 1)]
            pivote_var = pivote_var(formula[x], sat_literals, literals_in_clauses, solution)
            if pivote_var[1] > 0 and random() < 0.30:
                to_flip = abs(formula[x][randint(0, len(formula[0]) - 1)])
            else:
                to_flip = pivote_var[0]
            flip(sat_literals, literals_in_clauses, to_flip, solution)


def flip(sat_literals, lit_in_clause, to_flip, solution):
    if solution[to_flip - 1] < 0:
        for x in lit_in_clause[to_flip - 1]:
            sat_literals[x] += 1
        for x in lit_in_clause[-to_flip]:
            sat_literals[x] -= 1
    else:
        for x in lit_in_clause[to_flip - 1]:
            sat_literals[x] -= 1
        for x in lit_in_clause[-to_flip]:
            sat_literals[x] += 1
    solution[to_flip - 1] *= -1


def pivot(clause, sat_literals, lit_in_clause, solution):
    min = 999999999
    for literal in clause:
        pivot = 0
        if solution[abs(literal) - 1] < 0:
            for x in lit_in_clause[-abs(literal)]:
                if sat_literals[x] == 1:
                    pivot += 1
        else:
            for x in lit_in_clause[abs(literal) - 1]:
                if sat_literals[x] == 1:
                    pivot += 1
        if pivot < min:
            min = pivot
            to_flip = literal
    return abs(to_flip), min


if __name__ == '__main__':
    n_vars, clauses = cnf_parser(open(sys.argv[1], "r"))
    walk_sat(clauses, n_vars)
