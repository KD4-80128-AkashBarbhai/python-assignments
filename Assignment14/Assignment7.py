check_divisiblity_5 = lambda No : (No % 5 == 0)

def main():

    Data = int(input("Enter the number: "))
    
    print("True if divisible by 5 else false: ", check_divisiblity_5(Data))
    
if __name__ == "__main__":
    main()
