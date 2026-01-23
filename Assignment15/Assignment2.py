check_even = lambda No : (No % 2 == 0)
def main():
    Data = [1,2,3,4,5]
    print("Actual DAta is: ", Data)

    FData = list(filter(check_even,Data))
    print(FData)

if __name__ == "__main__":
    main()
