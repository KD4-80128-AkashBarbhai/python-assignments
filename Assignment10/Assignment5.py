def PrintEven(Value1):
    if Value1 < 1:
        return
    for i in range(1,Value1+1,2):
        print(i)


def main():

    Value1 = int(input("Enter Value : "))

    Result = PrintEven(Value1)
    
    
if __name__ == "__main__":
    main()

