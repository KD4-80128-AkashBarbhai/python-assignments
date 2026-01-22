def Factorial(Value1):
    sum = 1
    i = 1
    while i <= Value1:
        sum = sum * i
        i = i + 1
    return sum

def main():

    Value1 = int(input("Enter Value : "))

    Result = Factorial(Value1)
    print(Result)
    
if __name__ == "__main__":
    main()

