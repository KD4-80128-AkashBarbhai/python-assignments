square = lambda x: x**2
    
def main():
    Data = [1,2,3,4,5]
    print("Actual DAta is: ", Data)

    MData = list(map(square,Data))
    print(MData)

if __name__ == "__main__":
    main()
