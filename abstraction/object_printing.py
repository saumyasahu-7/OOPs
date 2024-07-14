class Test: 
	def __init__(self, a, b): 
		self.a = a 
		self.b = b 

	def __repr__(self): 
		return "Test a:%s b:%s" % (self.a, self.b) 

	def __str__(self): 
		return "From str method of Test: a is %s, b is %s" % (self.a, self.b) 

# Driver Code		 
t = Test(1,2) 
print(t) # This calls __str__() 
print([t]) # This calls __repr__() 

#From str method of Test: a is 1,b is 2
#[Test a:1 b:2]