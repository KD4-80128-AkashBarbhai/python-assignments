def CheckDiv(Value1):
    if Value1 % 3 == 0 and Value1 % 5 == 0:
        return True
        

    
    
def main():

    Value1 = int(input("Enter Value : "))

    Result = CheckDiv(Value1)
    if Result == True:
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")
        
if __name__ == "__main__":
    main()

