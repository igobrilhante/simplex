### Author
### Igo Ramalho Brilhante
###
### Simplex: Implementation of Simplex for two dimension

class Simplex2D(object):
	"""docstring for Simplex2D"""
	def __init__(self, cost_function,constraints):
		super(Simplex2D, self).__init__()
		self.cost_function = cost_function
		self.constraints = constraints

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

		# print 'Final Tableau',self.tableau

	# Check if there is positive values on the cost line
	def canContinue(self):
		cost_index = len(self.tableau)-1
		for i in range (0,self.var_count+self.constraints_count):
			if self.tableau[cost_index][i] > 0:
				return True

		return False

	# Get the pivot, which is the column with the highest value in cost line
	def getPivot(self):
		cost_index = len(self.tableau)-1
		pivot = 0
		for i in range (0,self.var_count+self.constraints_count):
			if self.tableau[cost_index][i] > pivot:
				pivot = self.tableau[cost_index][i]

		return self.tableau[cost_index].index(pivot)

	# Look for the minimum limit for the variable
	# pivot: pivot index
	def getConstraintLimit(self,pivot):
		b_index = self.var_count + self.constraints_count

		limit = float("inf")
		line_index = -1
		for i in range(0,self.constraints_count):
			if self.tableau[i][b_index]/self.tableau[i][pivot] < limit and self.tableau[i][pivot] > 0 :
				limit = self.tableau[i][b_index]/self.tableau[i][pivot]
				line_index = i
		print 'Limit %f in %d' %(limit,line_index)
		return line_index

	# Scaling matrix in order to obtain 0 in position 'pivot'
	# i: constraint index
	# pivot: pivot index
	def scalingMatrix(self,i,pivot):
		for j in range(0,self.constraints_count+1):
			if i != j:
				# print self.tableau[j]
				pivot_value = self.tableau[j][pivot]
				for k in range(0,self.var_count+self.constraints_count+1):
					# print '%f - (%f * %f)' % (self.tableau[j][k],self.tableau[i][k],pivot_value)
					self.tableau[j][k] = self.tableau[j][k] - (self.tableau[i][k]*pivot_value)

	# Perfomr iteration for Simplex Method
	def iteration(self):
		pivot_index  = self.getPivot()
		constaint_index = self.getConstraintLimit(pivot_index)
		if constaint_index == -1:
			return
		pivot_value = self.tableau[constaint_index][pivot_index]

		print 'Pivot Index',pivot_index
		print 'Pivot Value',pivot_value
		print 'Constraint Index',constaint_index
		for i in range(0,self.var_count+self.constraints_count+1):
			self.tableau[constaint_index][i] = self.tableau[constaint_index][i] / pivot_value
		
		# print 'Constraint',self.tableau[constaint_index]
		self.scalingMatrix(constaint_index,pivot_index)







if __name__ == '__main__':

	print 'Simplex Method'
	r1 = [0,2,3,1,5]
	r2 = [1,1,2,3,3]
	r = list()
	r.append(r1)
	r.append(r2)

	f = [5,6,9,8]

	simplex = Simplex2D(f,r)
	simplex.initTableau()
	print simplex.tableau
	i = 1
	while simplex.canContinue():
		print '###### Iteration',i
		simplex.iteration()
		print simplex.tableau
		i += 1
	print simplex.tableau




		