check_even = lambda No : (No % 2 == 0)

def main():

    Data = int(input("Enter the number: "))
    
    print("True if Even else false: ", check_even(Data))
    
if __name__ == "__main__":
    main()
