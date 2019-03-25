

iterable=['Spring','Summer','Autumn','Winter']

iterator=iter(iterable)

print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
#print(next(iterator))

def first(iterable):
	iterator=iter(iterable)
	try:
		print(next(iterator))
	except StopIteration:
		raise ValueError('iterator is Empty')


first([1,2,3,4,5])
first({1,2,3,4,5})
first(set())
