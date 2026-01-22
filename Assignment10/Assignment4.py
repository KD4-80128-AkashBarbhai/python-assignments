def PrintEven(Value1):
    if Value1 < 2:
        return
    for i in range(2,Value1+1,2):
        print(i)


def main():

    Value1 = int(input("Enter Value : "))

    Result = PrintEven(Value1)
    
    
if __name__ == "__main__":
    main()

