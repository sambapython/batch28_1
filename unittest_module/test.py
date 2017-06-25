import app
exp=30
act=app.add(10,20)
if exp==act:
	print "test passed"
else:
	print "text not passed"
exp="str1str2"
act=app.add("str1","str2")
if exp==act:
	print "test passed"
else:
	print "text not passed"

exp=None
act=app.add("str1",123)
if exp==act:
	print "test passed"
else:
	print "text not passed"