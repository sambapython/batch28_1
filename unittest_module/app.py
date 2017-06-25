class c1:
	def add(self,a,b):
		"""
		a,b: int: a+b
		a,b: str: concate
		a: int, b:str: None
		"""
		try:
			return a+b
		except:
			return None

def mul(a,b):
	return a*b