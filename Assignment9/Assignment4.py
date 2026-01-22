import math
def Square(Value1):
    return pow(Value1,3)
    
    
def main():

    Value1 = int(input("Enter Value : "))

    Result = Square(Value1)
    print(Result)
if __name__ == "__main__":
    main()

