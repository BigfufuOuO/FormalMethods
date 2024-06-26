from module_propagate import unit_propagate

class CDCL:
    def __init__(self, clauses, num_var):
        self.clauses = clauses
        self.num_var = num_var
        
    def solve(self):
        decision_positon = []
        M = []
        clauses, M = unit_propagate(self.clauses, M)
        if clauses == -1:
            return -1
        
        while not self.is_all_assigned(M):
            var = self.choose_var(clauses, M)
            self.assign_decision_var(decision_positon, M, var)
            
            
    def choose_var(self, clauses, M):
        pass    
        
    def is_all_assigned(self, M: list):
        if M.length >= self.num_var:
            return True
        return False
    
    def assign_decision_var(self, decision_position, M, var):
        decision_position.append(len(M))
        M.append(var)