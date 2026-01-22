def print_factors(value):
    value = abs(value)
    for i in range (1,value+1):
        if value % i == 0:
            print(i)        

def main():

    value = int(input("Enter a number : "))
    
    Result = print_factors(value)
    
    

    
if __name__ == "__main__":
    main()

