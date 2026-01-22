def isPrime(Value1):
    if Value1 <= 1:
        return False
    for i in range(2,int(Value1 ** 0.5) + 1):
        if Value1 % i == 0:
            return False
    return True


def main():

    Value1 = int(input("Enter Value : "))

    if isPrime(Value1):
        print("Prime Number")
    else:
        print("Not a prime number")
    
if __name__ == "__main__":
    main()

