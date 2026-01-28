def count_frequency(list,num):
    count = 0

    for i in range(len(list)):
        if list[i] == num:
            count += 1
    return count  

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

    search = int(input("Enter the element you want to search"))
    
    Ret = count_frequency(Data,search)
    print("Frequency of ", search, "is :", Ret)

if __name__ == "__main__":
    main()