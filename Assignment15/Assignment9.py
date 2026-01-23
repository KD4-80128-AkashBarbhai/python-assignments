from functools import reduce
product = lambda a,b : a*b
    
def main():
    Data = [1,2,5,2,1]
    
    RData = reduce(product,Data)
    print(RData)

if __name__ == "__main__":
    main()
