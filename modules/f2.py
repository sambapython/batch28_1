'''
import f1
#print "fun calling in f2:", f1.fun()
'''
'''
import f3
print "*"*20
print "calling fun in f2: ", f3.fun()
print "calling fun1 in f2: ", f3.fun1()
'''
from f3 import fun
print fun()