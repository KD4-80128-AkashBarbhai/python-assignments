def Operations(a,b):
    print("Addition: ", a+b)
    print("Substraction: ", a-b)
    print("Multiplication: ", a*b)
    if b != 0:
        print("Division: ", a/b)
    else:
        print("Division is not possible")

def main():

    value1 = int(input("Enter a number : "))
    value2 = int(input("Enter a number : "))
    Operations(value1,value2)


    
    

    
if __name__ == "__main__":
    main()

