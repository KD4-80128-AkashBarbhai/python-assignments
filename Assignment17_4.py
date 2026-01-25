def factorial_Addition(num):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum = sum + i
    return sum

def main():
    num = int(input("Enter the number : "))
    result = factorial_Addition(num)
    print(result)

if __name__ == "__main__":
    main()