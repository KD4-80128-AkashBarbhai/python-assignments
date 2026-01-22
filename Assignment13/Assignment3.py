def is_perfect(num):
    if num <= 0:
        return False
    total = 0
    for i in range(1,num):
        if num % i == 0:
            total += i

    return total == num



def main():
    number = int(input("Enter the number: "))
    if is_perfect(number):
        print("Perfect Number")
    else:
        print("Not Perfect Number")
if __name__ == "__main__":
    main()
