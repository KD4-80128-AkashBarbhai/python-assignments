def count_factorial(num):
    total = 1
    for i in range(1,num+1):
        total = total * i
    return total

def main():
    num = int(input("Enter the number : "))
    print(count_factorial(num))

if __name__ == "__main__":
    main()