from functools import reduce
max_number = lambda x,y: x if x > y else y
def main():
    Data = [1,2,3,4,5]
    print("Actual DAta is: ", Data)

    RData = reduce(max_number,Data)
    print(RData)

if __name__ == "__main__":
    main()
