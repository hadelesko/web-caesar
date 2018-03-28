from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    new_text="" ##  Initialisation of the encrypted text
    for char in text:
        new_text=new_text+rotate_character(char, rot)
    return new_text ## encrypted text

def main():
    # your main code (input and print statements)
    #def encrypt(text, rot):
    text= input("Type a message: ")
    rot= int(input("Rotate by: "))
    new_text="" ##  Initialisation of the encrypted text
    for char in text:
        new_text=new_text+rotate_character(char, rot)
    print(new_text)## encrypted text

if __name__ == "__main__":
    main()
