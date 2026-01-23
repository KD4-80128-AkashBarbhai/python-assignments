from functools import reduce
Add = lambda a,b: a+b
def main():
    Data = [1,2,3,4,5]
    print("Actual Data is: ", Data)

    RData = reduce(Add,Data)
    print(RData)

if __name__ == "__main__":
    main()
