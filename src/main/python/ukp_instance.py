class ukp_instance:
	weights = []
	prices = []
	# it contains the efficiencies and its indexes
	sorted_objects = []
	

	def __init__(self, objects, capacity):
		self.objects = objects
		self.capacity = capacity
		i = 0
		for obj in objects:
			self.weights.append(obj[0])
			self.prices.append(obj[1])
			self.sorted_objects.append((
				i,
				obj[1] / obj[0]
			)) # efficiency is the ratio of the price to the weight
			i = i + 1

	def max_weight():
		return max(self.weights)

	def min_weight():
		return min(weights)	
	
	def max_prices():
		return max(prices)
	
	def min_prices():
		return min(prices)

	def sort_by_efficiency(self):
		self.sorted_objects.sort(key=lambda pair:pair[1], reverse=True)
	
	
		
