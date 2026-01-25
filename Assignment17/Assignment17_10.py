def sum_of_digits(n):
    total = 0
    while n != 0:
        total += n % 10
        n = n // 10
    return total

def main():
    num = int(input("Enter the number : "))
    Result = sum_of_digits(num)
    print(Result)
    
if __name__ == "__main__":
    main()