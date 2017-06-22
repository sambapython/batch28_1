import pdb
a=10
b=20
c=30
def fun(a,b):
	print "a=%s, b=%s"%(a,b)
	return a+b
pdb.set_trace()
print fun(a,b)
for i,j in zip(range(10),range(10,20)):
	print fun(i,j)
