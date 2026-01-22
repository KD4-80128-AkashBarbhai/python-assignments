def MTable(Value1):
    
    for i in range(1,11):
        multiply = i*Value1
        print(multiply)
        i = i+1
        

    
def main():

    Value1 = int(input("Enter Value : "))

    Result = MTable(Value1)
if __name__ == "__main__":
    main()

