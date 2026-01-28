def min_numnber(list):
    min_num = list[0]

    for i in range(len(list)):
        if list[i] < min_num:
            min_num = list[i]
    return min_num  

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
    
    Ret = min_numnber(Data)
    print("max number is : ", Ret)

if __name__ == "__main__":
    main()