import os

def main():
    FileName = input("Enter the name of file : ")

    try:
        fobj = open(FileName, "r")
        Data = fobj.read()
        print(Data)
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")

    finally:
        print("End of application")
if __name__ == "__main__":
    main()
