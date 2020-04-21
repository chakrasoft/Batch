##########################set and frozen set
a={}
print(type(a))

b=set()
print(type(b))


s1={1,2,3,5,4,1,6}
s1
type(s1)
s1.add(7)
s1

###########3frozenset cannot addd or update###################
s2=frozenset({6,7,8,9,5,6})
s2
type(s2)
s2.add(1)
s2

#set operations
#add
s1.add(6)
s1

#insert does not work
s1.insert(66)
s1
s1.insert(66,77)
s1
####################################
s1.remove(6)
s1

s1.remove(5)
s1

s1.remove(5)
s1

s1.discard(4)
s1

# update

s1={1,2,3,4,5}
s1.update({6,7,8})
s1

# add list and set
s1={1,2,3,4}
s1.update([4,5],[1,6,8])
s1

###########################
s1={1,2,3,4,5,7}
s2={4,5,6,7,8,9}
 
4 not in s1

#union
s1.union(s2)  #s2.union(s1)
s1 | s2
s3=s1.union(s2)
s3


#intersection
s1={1,2,3,4,5}
s2={4,5,6,7,8,9}

s1 & s2
s1.intersection(s2)
s3=s1.intersection(s2)
s3


# difference
s1={1,2,3,4,5}
s2={4,5,6,7,8,9}

s1.difference(s2)
s3=s1.difference(s2)
s3=s1-s2
s3

s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
s4=s1.difference(s2,s3)
s4=s2.difference(s1,s3)
print(s4)

s1={1,2,3}
s2={2,3,4}
s3={3,4,5}
s4=s1.symmetric_difference(s2,s3)
print(s4)

###################ERROR#################################
s4=s1.symmetric_difference(s2,s3)
print(s4)

#clear
s1
s1.clear()
s1
      
##################Boolen##########################
s1={1,2,3}
s2={2,3,4}
s1<s2  


s={"hello world","hello King"}
s
s={"ab","cd","ef","gh"}
s
s={"A","B","C"}
s
s={"a","b","c"}
s
print(s.pop())

s4={1,2,3,1,2,4,5}
s4
print(s4.pop())

