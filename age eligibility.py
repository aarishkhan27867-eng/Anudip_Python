#Write a python program to accept the age from the user and check whether the candidate is eligible for voting or not?

Name=input("Enter the Name: ")
Age=int(input("Enter the age: "))
if Age>18 and Age<80:
    print("User is eligible for voting")
elif Age>80:
    print("Marja buddhe!")
else:
    print("User is not eligible for voting!")
