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
'''
from f3 import fun
print fun()
'''
'''
import f4
print (f4.fun())
'''

'''
import sys

sys.path.insert(0,'/home/tcloudost/Desktop')
print sys.path
import f4
'''
'''
import f4
print f4.fun()
print f4.fun1()
'''
'''
import module1
print module1.file1.fun()
'''
'''
from module1 import file1,file2
print file1.fun()
print file1.fun1()
print file2.fun()
print file2.fun1()
'''
import module1
print module1.file1.fun()
print module1.file1.fun1()
print module1.file2.fun()
print module1.file2.fun1()