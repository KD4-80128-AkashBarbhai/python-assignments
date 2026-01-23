check_divisiblity = lambda No : (No % 3 == 0 and No % 5 == 0)
    
def main():
    Data = [10,12,15,20,30]
    
    FData = list(filter(check_divisiblity,Data))
    print(FData)

if __name__ == "__main__":
    main()
