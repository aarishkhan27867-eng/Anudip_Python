#String is a sequence of character enclosed in a single or double quote.
#String is a sequence of characters.

str1="Adolf hitler"
print(str1.lower()) #For Lower case
print(str1.upper()) #For Upper case

str2="I am learning python programming"

#Replace function
rep=str2.replace("python","Cybercrime")
print(rep)

#Split function
str3="Trump,Modi,Khamenei,Putin"
print(str3.split(",")) 

#Join function
str4=["I","am","King","of","the","world"]
str5=["Hahahah"]
joint=" ".join(str4+str5)
print(joint)

#find function is used to find the first occurance in the string
str6="Anudip Foundation"
print(str6.find("u"))

#Len function
print(len(str6))

#Count function
print(str6.count("n")) #Counts number of occurence

#startswith & endswith
str7="python"
print(str7.startswith("py"))
print(str7.endswith("on"))

#strip function
str8="  Jo bole so nihaal   "
print(str8.strip()) #For removing unnecessary spacing 
print(str8.lstrip()) #For removing left side spacing
print(str8.rstrip()) #For removing right side spacing

#isalpha function - For checking if all are characters only
str9="TataSky"
str10="ANP-D4852"
print(str9.isalpha())
print(str10.isalpha())

#isdigit function - For checking if all are Numbers only
str11="1234"
print(str11.isdigit())

#For alphanumeric
print(str10.isalnum())

#Index position
str12="python"
print(str12[3])
print(str12[-1])
print(str12[-2])

#Slicing
str13="Maharashtra"
print(str13[:3]) #or print(str13[0:3])
print(str13[4:])
print(str13[4:8]) #will take till 7th position
