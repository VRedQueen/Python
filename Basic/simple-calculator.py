def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mult(x,y):
    return x*y

def divide(x,y):
    return x/y

print("select the operation.")
print("1- Addition")
print("2- Subtract")
print("3- Multiply")
print("4- Divide\n")


while True:
    option = input("Choose a option: ")
    
    if option in ('1','2','3','4'):
        try: 
            num1=float(input("The firts number: "))
            num2=float(input("The second number: "))
        except ValueError:
            print("Invalid input. Just numbers, please.")
            continue
        
        
        if option == '1':
            print(num1,"+",num2,"=",add(num1,num2))
        elif option == '2':
            print(num1,"-",num2,"=",sub(num1,num2))
        elif option == '3':
            print(num1,"*",num2,"=",mult(num1,num2))
        elif option == '4':
            print(num1,"/",num2,"=",divide(num1,num2))
            
        next= input("Do you want to do another calculation? (yes/no)\n")
        if next=="no":
            break
        elif next=="yes":
            continue
        else:
            print("Invalid input")
