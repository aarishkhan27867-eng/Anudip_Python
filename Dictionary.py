#dictionary
"""
1)It is mutable
2)It has key value pair
3)It stores data in unordered form
4)keys Must be a unique
5)It defines by using curly braces
"""
dict={}#empty dictionary

student={"name":"John","course":"BSC IT","Id":101}
print(student)

copy_student=student.copy()#create a shadow of your dictionary
print(copy_student)

copy_student.clear() #remove all the key value pair
print(copy_student)

student1={"name":"Arthur","Course":"Bcom","Id":102}
student_items=student1.items() #shows items of dictionary in list
print(student_items)

print(student1.get("Course")) #particular key's value
print(student1.keys()) # Only keys
print(student1.values()) #Only values

value=student1.pop("Id")
print(value,student1)

dict1={"Emp_Id":101,"Salary":30000,"Name":"Dutch"}
item=dict1.popitem() #Remove and return the key value pair from the last position
print(item,dict1)

#Traversing the dictionary
dict2={"Emp_Id":101,"Salary":30000,"Name":"Micah"}

#for key in dict2.keys():
#    print(key)

#for value in dict2.values():
#    print(value)

for key, value in dict2.items() :
    print(key, value)

#Updating the values
dict3={"Name":"Hosea"} 
dict3["Name"]="Abigail"
print(dict3)

dict4={"Name":"Mary","Age":30,"Name":"Angela"} #Duplicate keys are not allowed
print(dict4)

dict5={"Michael":45,"Trevor":44,"Franklin":30}# Duplicate values are allowed
print(dict5)

#Nested dictionary
students={
    "101": {"Name":"Nico","Number":"778865754756"},
    "102": {"Name":"Roman","Number":"43647537868924"}
    }
print(students["102"]["Name"])

dict6={"Michael":45,"Trevor":44,"Franklin":30}
if  "Trevor" in dict6:
    print("Key exists")
else:
    print("It doesn't exist")
