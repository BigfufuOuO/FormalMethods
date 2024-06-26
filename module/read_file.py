def read_file(filename):
    with open(filename, 'r') as f:
        line_count = 0
        clauses = []
        for line in f:
            line = line.split()
            if not line[0] == 'c':
                if line[0] == 'p':
                    num_var = int(line[2])
                    num_clause = int(line[3])
                else:
                    new_clause = []
                    for var in line:
                        if var == '0':
                            line_count += 1
                            clauses.append(new_clause)
                        elif - int(var) in new_clause:
                            line_count += 1
                            break
                        else:
                            new_clause.append(int(var))
                        
                        if int(var) > num_var or int(var) < -num_var:
                            raise ValueError('Illegal variable {}'.format(var))
                            
    if len(clauses) != num_clause:
        raise ValueError('Clauses number not match with {} and {}'.format(len(clauses), num_clause))
    return clauses, num_var, num_clause
                            