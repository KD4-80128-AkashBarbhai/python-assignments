def count_digits(n):
    count = 0
    while n != 0:
        count += 1
        n = n // 10
    return count

def main():
    num = int(input("Enter the number : "))
    Result = count_digits(num)
    print(Result)
    
if __name__ == "__main__":
    main()