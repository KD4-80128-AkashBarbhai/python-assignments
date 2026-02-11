import sys
import hashlib

def CountFrequency(word, FileName):
    try:
        fobj = open(FileName, "r")
        data = fobj.read()
        fobj.close()

        count = data.count(word)
        return count
    except FileNotFoundError:
        print("File not found.")
        return

def main():
    if len(sys.argv) != 3:
        print("Usage: python CompareFile.py <String> <FileName>")
        return

    searchString = sys.argv[1]
    File_name = sys.argv[2]

    result = CountFrequency(searchString,File_name)
    print("String",searchString,"is repeated", result, "time/times in the",File_name)


if __name__ == "__main__":
    main()