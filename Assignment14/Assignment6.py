check_odd = lambda No : (No % 2 == 1)

def main():

    Data = int(input("Enter the number: "))
    
    print("True if odd else false: ", check_odd(Data))
    
if __name__ == "__main__":
    main()
