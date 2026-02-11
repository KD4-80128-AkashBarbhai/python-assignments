import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: Assignemnt_29_3.py ABC.txt")
        sys.exit()

    source_file = sys.argv[1]
    
    try:
        fobj = open(source_file,"r")
        print("File gets successfully opened")

        cobj = open("Demo.txt","w")

        for line in fobj:
            cobj.write(line)

        fobj.close()
        cobj.close()
         
    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of applicatoion")
        
    
if __name__ == "__main__":
    main()
