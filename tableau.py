
class Tableau(object):
	"""docstring for Tableau"""
	def __init__(self, cost_function,constraints):
		super(Tableau, self).__init__()
		self.cost_function = cost_function
		self.constraints = constraints

		self.initTableau()

		# Initialize the tableau model
	def initTableau(self):
		self.constraints_count = len(self.constraints)
		self.var_count = len(self.cost_function)

		columns = self.var_count + self.constraints_count
		lines = self.constraints_count + 1

		self.tableau = []

		# Adding the constraints into the tableau
		for j in range(0,self.constraints_count):
			self.tableau.append([]) # insert line
			for i in range(0,self.var_count):
				# print 'tableau',self.tableau
				# print i,j
				# print 'constain',self.constraints[j]
				# print self.constraints[j][i]
				self.tableau[j].append(float(self.constraints[j][i]))

			for i in range(self.var_count,columns):
				if i - self.var_count == j:
					self.tableau[j].append(1.0)
				else:
					self.tableau[j].append(0.0)

			self.tableau[j].append(float(self.constraints[j][self.var_count]))
		# Adding the costs
		self.tableau.append([])
		for i in range(0,self.var_count):
			self.tableau[self.constraints_count].append(float(self.cost_function[i]))
		for i in range(self.var_count,columns+1):
			self.tableau[self.constraints_count].append(0.0)

		