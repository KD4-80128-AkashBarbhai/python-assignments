largest_number = lambda a,b,c : max(max(a,b),c)     # a if(a>=b and a >= c) else (b if b >= c else c)

def main():

    Value1 = int(input("Enter first number: "))
    Value2 = int(input("Enter second number: "))
    Value3 = int(input("Enter third number: "))
    
    print("largest number is: ", largest_number(Value1,Value2,Value3))
    
if __name__ == "__main__":
    main()
