#add space in every 3rd place of the string

#get string from user
str=input("enter the sentance : ") 

#declare a variable
addSpace="" 

#use for loop for getting single character from str
for i in range(0,len(str)):
    #use % for calculate 3rd place and add space
    if i % 2==0: #
        addSpace+=" "+str[i] 

    #if it is not a 3rd place ,then add next character in a str
    else:
        addSpace+=str[i]

#finally , display the output
print(addSpace)
