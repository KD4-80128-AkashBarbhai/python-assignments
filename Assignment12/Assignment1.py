def check_vowel(ch):
    ch = ch.lower()
    if ch in 'aeiou':
        return True
    else: 
        return False
       


def main():

    ch = input("Enter a character : ")
    if check_vowel(ch):
        print("Vowel")
    else:
        print("Constant")
    
if __name__ == "__main__":
    main()

