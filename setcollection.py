p={1,2,45,67,89}
print(p)

print(type(p))

q=set()
print(type(q))

q=set([1,2,3,1,2])
print(q)

for x in q:
	print(x)

#membership
print(3 in q)

#adding elements
q.add(56)
print(q)

#update
q.update(p)
print(q)

#remove //remove will show error while discard will not show if element is not present
q.remove(56)
print(q)

q.discard(56)
print(q)

#copy
j=q.copy()
print(j)

m=set(j)
print(m)


blue_eyes={'mhp','chp','khp'}
blone_hair={'mhp','khp','ghp'}
smell_hcn={'chp','ghp'}
blood={1,2,3}

print(blue_eyes.union(blone_hair) == blone_hair.union(blue_eyes))#union commutative
print(blue_eyes.intersection(blone_hair)) #intersection commutative

print(blue_eyes.difference(blone_hair)) #A - A intersection B ,not commutative
print(blue_eyes.symmetric_difference(blone_hair)) #A-B U B-4A
print(blue_eyes.issubset(blone_hair))
print(blue_eyes.issuperset(blone_hair))
print(blood.isdisjoint(blue_eyes))
