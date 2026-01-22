def Palindrome(Value):
    orignal = Value
    reverse = 0
    Value = abs(Value)        # Handel negative number
    while Value > 0:
        reverse = reverse * 10 + (Value % 10)
        Value //= 10        

    return orignal == reverse


def main():

    Value = int(input("Enter Value : "))

    if Palindrome(Value):
        print("Palindrome")
    else:
        print("Not Palindrome")

if __name__ == "__main__":
    main()
