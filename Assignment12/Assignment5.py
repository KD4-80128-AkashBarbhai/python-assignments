def print_numbers(value1):
    for i in range(value1,0,-1):
        print(i)

def main():

    value1 = int(input("Enter a number : "))
    print_numbers(value1)

if __name__ == "__main__":
    main()