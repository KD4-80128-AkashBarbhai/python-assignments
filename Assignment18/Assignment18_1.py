def Summation(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    return Sum

def main():
    Size = 0
    value = 0
    Ret = 0

    print("Enter the number of elements: ")
    Size = int(input())
    
    Data = list()
    
    print("Enter the elements: ")
    
    for i in range(Size):
        value = int(input())
        Data.append(value)
    
    Ret = Summation(Data)
    print("Summation is : ", Ret)

if __name__ == "__main__":
    main()