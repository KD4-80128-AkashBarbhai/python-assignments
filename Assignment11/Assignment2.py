def countDigits(Value):
    count = 0
    Value = abs(Value)        # Handel negative number
    while Value > 0:
        count = count + 1
        Value //= 10        # Divide the number by 10 and floor the value
                            # example 123/10 = 12.3 = 12 (floor of 12.3)
    return count


def main():

    Value = int(input("Enter Value : "))

    Result = countDigits(Value)
    print("Count of digit is :", Result)

if __name__ == "__main__":
    main()

