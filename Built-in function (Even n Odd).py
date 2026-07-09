#Write a python function to check the number is even or odd.

num = int(input("Enter a number: "))

def check_even_odd(num):
    if num % 2 == 0:
        print("Number is Even")
    else:
        print("Number is Odd")
        
check_even_odd(num)
