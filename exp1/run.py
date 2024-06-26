from module.read_file import read_file
from module.module_propagate import unit_propagate

if __name__ == '__main__':
    clauses, num_var, num_clause = read_file('exp1/data/simple_v3_c2.cnf')
    status, assign = unit_propagate(clauses)
    print(status, assign)