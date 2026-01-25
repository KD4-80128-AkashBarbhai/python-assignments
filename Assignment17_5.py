def is_prime(num):
    if num <= 1:
        return "Not Prime"
    else:
        for i in range(2,num):
            if num % i == 0:
                return "Not Prime"
            else:
                return "Prime"


def main():
    num = int(input("Enter the number : "))
    Result = is_prime(num)
    print(Result)


if __name__ == "__main__":
    main()