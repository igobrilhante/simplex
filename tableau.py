# Author: Igo Ramalho Brilhante
# Tableau for Simplex
# 
# 

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

		self.artificial_variable_count = 0

		self.cost_index = self.constraints_count

		self.basis = list()

		self.artificial_variable = list()

		self.columns = self.var_count + self.constraints_count + 1
		self.b_index = self.columns - 1

		self.lines = self.constraints_count + 1

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

			for i in range(self.var_count,self.columns-1):
				eq = self.constraints[j][self.var_count]
				if i - self.var_count == j:
					if eq == '<=' or eq == '<' or eq == 0:
						self.tableau[j].append(1.0)
					else:
						self.tableau[j].append(-1.0)
				else:
					self.tableau[j].append(0.0)

			# add b column
			self.tableau[j].append(float(self.constraints[j][self.var_count+1]))

		# Adding the costs
		self.tableau.append([])
		for i in range(0,self.var_count):
			self.tableau[self.constraints_count].append(float(self.cost_function[i]))
		for i in range(self.var_count,self.columns):
			self.tableau[self.constraints_count].append(0.0)

		# Add basis
		for i in range(self.var_count,self.columns-1):
			self.basis.append(i)
		print self.basis

	def __str__(self):
		s = ""
		i = 0
		for l in self.tableau:
			if i < len(self.basis):
				s += '['+str(self.basis[i])+'] ' + str(l)+"\n"
			else:
				if i == len(self.basis):
					s += '[z] ' + str(l)+"\n"
				else:
					s += '[w] ' + str(l)+"\n"
			i += 1
		s += "Basis: "+str(self.basis)
		return s

	def __getitem__(self, key):
		return self.tableau[key]

	def __setitem__(self,key,value):
		self.tableau.insert(key,value)

	def changeBasis(self,enter,leave):
		# change basis
		out = self.basis.pop(leave)
		self.basis.insert(leave,enter)
		print 'Changing basis: enter '+str(enter)+' leave '+str(out)

	def addColumn(self,key,default_value):
		for r in self.tableau:
			r.insert(key,default_value)
		self.columns += 1

	def removeColumn(self,key):
		for r in self.tableau:
			r.pop(key)
		self.columns -= 1

	def addRow(self,key,default_value):
		self.tableau.insert(key,[])
		for i in range(0,self.columns):
			self.tableau[key].append(default_value)
		self.lines += 1

	def removeRow(self,key):
		self.tableau.pop(key)
		self.lines -= 1

		