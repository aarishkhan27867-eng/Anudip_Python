'''
Tuple
1)Immutable (Cannot be modified after creation)
2)Ordered (Elements maintain their order)
3)Allows duplicate values
4)Can store different data types
5)Defined using parentheses ()
'''

tuple1 = ()  # Empty tuple

tuple1 = (10,)  # Singleton tuple
tuple2 = (1, 2, 3, 4, 5)
print(tuple2)

tuple3 = (1, 2, 3, 4, 5)  # Creating a tuple
print(tuple3[1]) #To retrieve the second element

#print(tuple3[4])
print(tuple3[-1])
print(tuple3[2:4]) #Retrieve tuple using slicing

#Concate tuples
tuple4=(4,5,6)
tuple5=(8,7,6)
concate=tuple4+tuple5
print(concate)

#Check membership of tuple
tuple6=(4,3,2,1,67,55,9)
print(5 in tuple6)
print(5 not in tuple6)

#Repetition of same tuples using multiplication
tuple7=(3,4,5,6,7,5)
print(tuple7*4) #prints 4 times
size=len(tuple7) #counts length ie number of elements
print(size)
print(tuple7.count(5)) #counts occurences of the element 5

tuple8=(9,8,2,1)
print(min(tuple8)) #For minimun value
print(max(tuple8)) #For maximun value

#Sorting in tuple
tuple9=(33,78,66,456,90,23,11,56)
result=sorted(tuple9)
print(result)
print(sorted(tuple9, reverse=True)) #Reverse sorting

#Unpacking the tuples
p,q,r,s=tuple8
print(p,q,r,s) #Result: 9 8 2 1

tuple10=(4,5,66,88,76,67)
total=sum(tuple10) #Summation of the tuple
print(total)

for i in tuple10 :
    print(i)
