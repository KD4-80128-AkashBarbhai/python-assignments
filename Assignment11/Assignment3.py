def SumOfDigits(Value):
    total = 0
    Value = abs(Value)        # Handel negative number
    while Value > 0:
        total = total + (Value % 10)
        Value //= 10        

    return total


def main():

    Value = int(input("Enter Value : "))

    Result = SumOfDigits(Value)
    print("Sum of the digit is :", Result)

if __name__ == "__main__":
    main()

