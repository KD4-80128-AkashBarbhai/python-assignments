def print_binary(num):
    if num <= 0:
        return "0"
    
    binary = ""
    num = abs(num)

    while num > 0:
        binary = str(num % 2) + binary
        num //= 2
    return binary

def main():
    number = int(input("Enter the number : "))
    result = print_binary(number)
    print(result)

if __name__ == "__main__":
    main()
