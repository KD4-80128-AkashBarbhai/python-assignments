check_odd = lambda No:(No % 2 == 1)
def main():
    Data = [1,2,3,4,5]
    print("Actual DAta is: ", Data)

    FData = list(filter(check_odd,Data))
    print(FData)

if __name__ == "__main__":
    main()
