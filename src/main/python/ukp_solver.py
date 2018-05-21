from timeit import default_timer as timer
from ukp_solving_method import ukp_solving_method
from ukp_instance import ukp_instance

class ukp_solver:
	sorting_time = 0
	resolving_time = 0
	sorting_time = 0
	total_time = 0
	how_much_taken = []

	def __init__(self, ukp_instance, solving_method):
		self.ukp_instance = ukp_instance
		self.solving_method = solving_method
		self.how_much_taken = [0] * len(self.ukp_instance.sorted_objects)

	def solve(self):
		if self.solving_method == ukp_solving_method.DENSITY_ORDERED_UGREEDY:
			start = timer() # start the sorting of objects according to the decreasing of efficiencies
			self.ukp_instance.sort_by_efficiency()
			end = timer()
			self.sorting_time = end - start
			
			
			start = timer() # start the solving procedure
			self.density_ordered_ugreedy()
			end = timer()
			self.resolving_time = end - start
			self.total_time = self.sorting_time + self.resolving_time

	def density_ordered_ugreedy(self):
		remaining_capacity = self.ukp_instance.capacity
		for i in range(len(self.ukp_instance.weights)):
			print(self.ukp_instance.sorted_objects[i][1])
			self.how_much_taken[i] = int(remaining_capacity / self.ukp_instance.weights[self.ukp_instance.sorted_objects[i][0]])
			remaining_capacity = remaining_capacity - self.how_much_taken[i] * self.ukp_instance.weights[i]

	def ugreedy_solver(self):
		pass
'''
    def density_ordered_ugreedy(self):
		remaining_capacity = self.ukp_instance.capacity
		for i in self.ukp_instance.sorted_objects:
            self.how_much_taken[i] = int(remaining_capacity / self.ukp_instance.weights[self.ukp_instance.sorted_objects[i][0])
            remaining_capacity = remaining_capacity - self.taken[i] * self.knapsack.weights[i]

'''
    