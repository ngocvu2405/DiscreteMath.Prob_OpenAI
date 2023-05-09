from ortools.sat.python import cp_model

def solve(n_size):
    m = cp_model.CpModel()

    class SolutionPrinter(cp_model.CpSolverSolutionCallback):
        """Print intermediate solutions."""

        def __init__(self):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self.__solution_count = 0

        def solution_count(self):
            return self.__solution_count

        def check(self):
            return LastCheck(self)

        #print solution
        def PrintCase(self):
            for i in range(N):
                print(int(self.Value(x[i])),end = " ")
            print()

        # calculate solution here
        def on_solution_callback(self):
            if SolutionPrinter.check(self):
                self.__solution_count += 1
                # SolutionPrinter.PrintCase(self) # Nếu muốn in tất cả solution, bật dòng này lên
            

    def A(name, left,right):
        global m
        m.NewBoolVar(left,right,name)

    #declare variables and constraints here

    N = n_size
    x = [0 for i in range(N)]

    for i in range(N):
        x[i] = m.NewIntVar(0, 6, f"x_{i}")

    for i in range(1, N - 1):
        m.Add(x[i] >= 2)

    m.Add(sum(x) + N - 1 == 10)

    #only declare function, no call
    def LastCheck(self):
        if self.Value(x[0]) == 1:
            return False
        if self.Value(x[N - 1]) == 1:
            return False
        return True

    #end create variables and constraints

    solver = cp_model.CpSolver()

    solver.parameters.enumerate_all_solutions = True
    callback = SolutionPrinter()
    status = solver.Solve(m,callback)
    # print(callback.solution_count())    
    return callback.solution_count()

    if status in [cp_model.UNKNOWN]:
        status =  "Time out."

    if status not in [cp_model.OPTIMAL, cp_model.FEASIBLE]:
        status =  "No solution."

N_size = 10
result = 0

for i in range(1, N_size):
    result += solve(i)

print(result)