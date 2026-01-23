def chk_div_5(num):
    if num%5==0:
        print(True)
    else:
        print(False)
def main():
    num = int(input("Enter the number: "))
    chk_div_5(num)

if __name__ == "__main__":
    main()
