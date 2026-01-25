def main():
    num = int(input("Enter the number : "))
    while num > 0:
        for i in range(1,6):
            print(i,end="  ")
        print()
        num = num - 1


if __name__ == "__main__":
    main()