#demonstrate scoping
'''
global count
count=0
def show_count():
	print('count={}'.format(count))
	print('count=',count)
	print(count)
def set_count(c):
	 
	count=c
	print(count)

show_count()
set_count(3)

#enclosed scoping

pi='global pi variable'

def outer():
	pi='outer pi variable'
	def inner():
		#pi='inner pi variable'
		nonlocal pi 
		print(pi)
	inner()

outer()
print(pi)'''

#Buily in scope
from math import pi

#pi='global pi variable'

def outer():
	'''hello'''
	#pi='outer pi variable'
	def inner():
		#pi='inner pi variable'
		#nonlocal pi 
		print(pi)
	inner()

outer()
#help(outer)
