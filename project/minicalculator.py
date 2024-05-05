no1 = input("Enter first number:")
operator = input ("+,-,%,/ :")
no2 = input("Enter second number:")

if operator == "+" :
    print(int(no1) + int(no2))
elif operator == "-" :
    print(int(no1) - int(no2))    
elif operator == "/" :
    print(int(no1 ) /int(no2))
elif operator == "%" :
    print(int(no1) % int(no2))    
else:
    print ("Invalid operator ! !") 


     
