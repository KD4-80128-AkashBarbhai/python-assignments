is_even = lambda x: x % 2 == 0
    
def main():
    Data = [1,2,4,3,5,6,7,10]
    
    FData = len(list(filter(is_even,Data)))
    print(FData)

if __name__ == "__main__":
    main()
