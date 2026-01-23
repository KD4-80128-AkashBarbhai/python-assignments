check_length = lambda s : len(s) > 5
    
def main():
    Data = ["Aakash","Raahul","Om","Jay"]
    print("Actual DAta is: ", Data)

    FData = list(filter(check_length,Data))
    print(FData)

if __name__ == "__main__":
    main()
