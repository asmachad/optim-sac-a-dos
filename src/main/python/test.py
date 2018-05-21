from Knapsack import Knapsack
from KnapsackSolver import KnapsackSolver
from Benchmark_reader import BenchmarkReader
import sys
from timeit import default_timer as timer
from ukp_solving_method import ukp_solving_method
from ukp_instance import ukp_instance
from ukp_solver import ukp_solver
sys.setrecursionlimit(10000)

#weights_and_prices = [[33,4],[49,5],[60,6],[32,2]]
#capacity = 130
#kp = Knapsack(capacity,weights_and_prices)

br = BenchmarkReader("../../../assets/upk/exnsd16.ukp")

# kp = Knapsack(br.capacity,br.problem_values)
kp = ukp_instance(br.problem_values, br.capacity)
start = timer()
#kp.sort_by_utility()
#end = timer()
#print("Sorting time: ",end-start)
#Solver = KnapsackSolver(kp)
solver = ukp_solver(kp, ukp_solving_method.DENSITY_ORDERED_UGREEDY)
#start = timer()
#Solver.BB_solver1(0,0,0)
#Solver.BB_solver2()
solver.solve()
end = timer()
print("Solving time: ",end-start)

print('index nb weight price')
cap = 0
final_taken = []
for i in range(len(solver.how_much_taken)):
    if solver.how_much_taken[i] > 0:
        if cap + solver.how_much_taken[i]*kp.weights[i] <= kp.capacity:
            cap += solver.how_much_taken[i]*kp.weights[i]
            final_taken.append(i)
            print(kp.sorted_objects[i][0],solver.how_much_taken[i], kp.weights[i],kp.prices[i])
print('found: ',cap,'for max capacity: ',kp.capacity)
print("Solution: ",br.Solution)
