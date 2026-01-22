def ChkGreater(Value1,Value2):
    if Value1 > Value2:
        return Value1
    else:
        return Value2
    
    
def main():

    Value1 = int(input("Enter Value 1: "))
    Value2 = int(input("Enter Value 2: "))

    Result = ChkGreater(Value1, Value2)
    print(Result, "is greater")
if __name__ == "__main__":
    main()
