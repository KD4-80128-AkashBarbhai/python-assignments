def main():

    max_number = lambda x,y: x if x > y else y      #method2: max_number = lambda x,y: max(x,y)   --->max() is built in function
    value1 = int(input("Enter the number: "))
    value2 = int(input("Enter the number: "))
    print(max_number(value1,value2), "is maximum")
    
if __name__ == "__main__":
    main()
