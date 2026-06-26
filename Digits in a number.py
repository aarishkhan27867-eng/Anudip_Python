#Write a program to count the digits in the number

num=int(input("Enter the number : "))

count=0
while num>0:
    count+=1
    num//=10
print(count)
