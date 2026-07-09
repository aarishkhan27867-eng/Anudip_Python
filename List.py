#List

#Example1
list1=[23,"Whatever",4.5,True]
print(list1)
print(list1[2])
print(list1[1:3])

#Mutation in List
list1[2]=10
print(list1)

#Append example
list2=["Ghanta",10,5.6,00.09]
list3=list2.append("Car") #Adds the item in the end of the list
print(list2)

print(len(list2)) #Length check

#Insert function is used to insert the item at a specified position
list4=[34,22,4.5,0.9,"Suraj","Weds","Sandeep"]
list4.insert(2,44) #2 determines the position and 44 is the value
print(list4)

#Remove : removes the first occurance of the specified value
list5=[1,2,3,4,5,4,3,2,1]
list5.remove(5) #Removes 5 or will remove 1 only first occured if removing 1
print(list5)

#pop removes the item at particular specified index
list6=[3,1,24,235,35,356,35,3]
list6.pop(3) #Removes item at 3rd index
print(list6)

#index() returns the index of first occurence of the element
print(list6.index(35))

#Count returns the number of times the element occured
list7=["Vikas","Suraj",55,23425,3.4,00.000000003,55]
print(list7.count(55))

#sort() used to sort elements in ascending order
list8=[1,2,3,4,5,3,6,7,8,93,5,3,6,3,6,3,6,2]
list8.sort()
print(list8)
list8.reverse() #used for reverse order
print(list8)
#Ex:
list9=[1,2,3,4,5,6,6,7,7,7,64,34,5,7,5]
list9.reverse()
print(list9)

#copy() creates the copy of a list
list10=[3,4,5]
list11=list10.copy()
print(list11)

#Descending order using sort()
list12=[4,33,5.4]
list12.sort()
print(list12[::-1])

#Descending order using sorted and reverse
list13=[5,3,8,9,2,3,33,6.7]
a=sorted(list13,reverse=True)
print(a)

#Traversing a list using for loop
list14=[4,5,6,88,6.7,0.9,132]
for i in list14:
    print(i)

#Traversing using while loop
i=0
while i<len(list14) :
    print(list14[i])
    i+=1

#enumerate function used for print values with their corresponding indexes
list15=[3,5,46,3456,5,343,66,0.7,0.4]
for index,value in enumerate(list15):
    print(index,value)

#Practice question:
"""
1.Write a python program to find even n odd number from the list ex: [1,2,3,4,5,6,7,8,9]
2.Find the largest number or element from the list.
3.Find the 2nd largest element from the list. [20,25,45,22,68]
4.Check whether the element exists in the list or not after taking elements from the user
"""
