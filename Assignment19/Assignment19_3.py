
from functools import reduce


def main():
    
    Size = int(input("Enter the size of list"))
    Data = list()

    print("Enter the elements: ")
    for i in range(Size):
        value = int(input())
        Data.append(value)
    
    FData = list(filter(lambda No : No >= 70 and No <= 90, Data))
    print("Data after filter : ", FData)

    MData = list(map(lambda No : No + 10 , FData))
    print("Data after map : ", MData)

    RData = reduce(lambda A,B : A*B , FData)
    print("Data after reduce : ", RData)

if __name__ == "__main__":
    main()