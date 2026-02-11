import sys
import hashlib

def CalculateChecksum(FileName):
    fobj = open(FileName, "rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)
    while len(Buffer) > 0:
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()


def main():
    if len(sys.argv) != 3:
        print("Usage: python CompareFile.py <File1> <File2>")
        return

    File1 = sys.argv[1]
    File2 = sys.argv[2]

    checksum1 = CalculateChecksum(File1)
    checksum2 = CalculateChecksum(File2)

    if checksum1 == checksum2:
        print("Success")
    else:
        print("Failure")


if __name__ == "__main__":
    main()