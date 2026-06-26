#Write a program to display student result in grade.
# A=80+ B=60-80 C=50-60 D=40-50 E=35-40 F=<35

Name = input("Enter the name: ")
Marks = float(input("Enter the Marks: "))

if Marks < 35:
    print("F")
elif Marks <= 40:
    print("E")
elif Marks <= 50:
    print("D")
elif Marks <= 60:
    print("C")
elif Marks <= 80:
    print("B")
elif Marks <= 100:
    print("A")
else:
    print(f"{Name} Tere baap ko mila tha kya itna?")
