#Write a python program to accept alphabet from the user and check if the alphabet is vowel or consonant.

#Method 1
Alphabet=input("Enter any aphabet: ")
if Alphabet in 'aeiouAEIOU':
    print("Vowel")
elif Alphabet in '~!@#$%^&*()_+{}:"<>?/-/`-=[];.,/\|':
    print("Yeh kya bak rahe ho m*d*rchod !")
else:
    print("Consonant")

#Method 2
