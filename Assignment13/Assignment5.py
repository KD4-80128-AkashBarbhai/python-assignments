def print_grade(num):
    if  75<= num <=100:
        return "Distinction"
    elif 60<= num <75:
        return "First Class"
    elif 50<= num <60:
        return "Second Class"
    elif 0 <= num <50:
        return "Fail"
    else:
        return "Wrong input"

def main():
    number = int(input("Enter the marks : "))
    result = print_grade(number)
    print(result)

if __name__ == "__main__":
    main()
