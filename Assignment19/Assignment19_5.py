from functools import reduce

def CheckPrime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def main():
    
    Size = int(input("Enter the size of list"))
    Data = list()

    print("Enter the elements: ")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    
    FData = list(filter(CheckPrime, Data))
    print("Data after filter : ", FData)

    MData = list(map(lambda No : No*2 , FData))
    print("Data after map : ", MData)

    RData = reduce(lambda A,B : A if A > B else B, MData)
    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()