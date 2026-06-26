#Write a program to print Fibonacci series.

num=(int(input("Enter the number : ")))

a=1
b=1

for i in range(1,num+1) :
    print(a)
    c=a+b  #c=1+1, c=2+1=3
    a=b      #a=1,  a=2
    b=c      #b=2, b=3
