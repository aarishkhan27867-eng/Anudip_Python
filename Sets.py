#Sets
"""
Set is enclosed in curly braces
sets are mutable
no duplicate values allowed
no indexing available
Sets doesnt maintain any order (displays values randomly)
"""
"""
set1={10,90,70,34,25} #Creating set using curly braces
print(set1)

#Creating the set using the set constructor
set2=[2,34,32,5556,33,45,89,67,2,2] #Doesnt take duplicate values
myset2=set(set2)
print(myset2)

#Creating an empty set
set3=[]

#For adding new element
set4={34,55,64,87}
set4.add(50)
print(set4)

#For removing
set4={34,55,64,87}
set4.remove(34)
print(set4)
#If value not available in the set
set4.remove(69)
print(set4)
"""
"""
Result: error
Traceback (most recent call last):
  File "C:/Users/AARISH KHAN/Desktop/STUDY/Anudip/Domain/Notes/Python/Sets.py", line 30, in <module>
    set4.remove(69)
KeyError: 69

#Discard function doesnt give error message like remove()
set4.discard(69)
print(set4)


#Clear function is used to remove all the elements
set5={44,56432,2446,654,2,53,4}
set5.clear()
print(set5)
"""
#Union operation : returns all the elements from both sets
set6={445456,5432,54,21}
set7={21,456,32,3}
result1=set6.union(set7)
print(result1)

#Intersection operation : returns common element from both sets
result2=set6.intersection(set7)
print(result2)

#Difference opretion : Returns only first set elements which are not in the second set
result2=set6.difference(set7)
print(result2)

#Symmetric difference : Elements that are in either set, but not both
result2=set6.symmetric_difference(set7)
print(result2)

#Subset operation
set8={10,20,30,40,50,60,70}
subset1={20,40}
is_subset=subset1.issubset(set8) #Checks if values of subset1 is present in set8 or not.
print(is_subset)
