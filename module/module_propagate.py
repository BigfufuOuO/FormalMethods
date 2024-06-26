def bcp(clauses, unit_var):
    clause_set = [c[:] for c in clauses]
    for c in reversed(clause_set):
        if unit_var in c:       # 如果单子句中有unit_var，可满足，删除该子句
            clause_set.remove(c)
        elif -unit_var in c:    # 如果单子句中有-unit_var，删除-unit_var
            c.remove(-unit_var)
            if len(c) == 0:
                return -1       # 不可满足
    return clause_set

def unit_propagate(clauses):
    assign = []
    flag = True
    while flag:
        flag = False
        for clause in clauses:
            if len(clause) == 1:
                clauses = bcp(clauses, clause[0])
                assign.append(clause[0])
                flag = True
            if clauses == -1:
                return -1, []
    return clauses, assign