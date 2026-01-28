import MarvellousNum
def listPrime(list):
    sum_prime = 0

    for i in range(len(list)):
        if MarvellousNum.CheckPrime(list[i]):
            sum_prime += list[i]
    return sum_prime 

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
    
    Ret = listPrime(Data)
    print("Addition of all prime numbers is : ", Ret)

if __name__ == "__main__":
    main()