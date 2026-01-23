def main():

    min_number = lambda x,y: x if x < y else y      #method2: min_number = lambda x,y: max(x,y)   --->min() is built in function
    value1 = int(input("Enter the number: "))
    value2 = int(input("Enter the number: "))
    print(min_number(value1,value2), "is minimum")
    
if __name__ == "__main__":
    main()
