from helpers import alphabet_position, rotate_character
from flask import Flask, request
app=Flask(__name__)
app.confi
def encrypt(text, encryption_key):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    u_alphabet=alphabet.upper()
    #encryption_key=input("Type your encryption key:  ")
    #text= input("Type the text that wil be encrypted:  ")
    num_char=0
    encrypted_text=""
    
    for j in range(len(text)):     ## for lowercase
        if text[j] in alphabet: #or text[j] in alphabet.upper():
            char= text[j]
            charposition=alphabet_position(char)
            num_char+=1
            
            corchar=encryption_key[(num_char-1)%len(encryption_key)]
            retvalue=(num_char-1, char, charposition, corchar, alphabet_position(corchar), alphabet[(charposition+alphabet_position(corchar))%len(alphabet)]  )
            encrypted_text= encrypted_text + alphabet[(charposition+alphabet_position(corchar))%len(alphabet)]
            #return retvalue
            #print(retvalue)
           
        else:                       ## for uppercases     
            if text[j] in alphabet.upper(): #or text[j] in alphabet.upper():
                char= text[j]
                charposition=alphabet_position(char)
                num_char+=1
                corchar = encryption_key[(num_char-1)%len(encryption_key)] ## corresponding character in the in the encrcyption key
                
                ### built here the for each character from a text a sixtuplet: retvalue = ( a, b, c,d,  e, f ); where
                ## a: position of the character in the given text, b caharacter of the text referenced by "a";
                ## c: position in the alphabet; d: correspoding character from the given encryption key
                ## e: position of "d" in the alphabet
                ## f: the resulted encrypted character
                retvalue=(num_char-1, char, charposition, corchar, alphabet_position(corchar), u_alphabet[(charposition+alphabet_position(corchar))%len(alphabet)])
                ## Update encrypted text
                encrypted_text= encrypted_text + u_alphabet[(charposition+alphabet_position(corchar))%len(u_alphabet)]
            
            else:                 ## character not in alphabet: number, %$&*())_"::><?@#!~|}][\=-)'/ ...etc
                char= text[j]
                charposition=alphabet_position(char)
                num_char= num_char
                corchar="n/a" ## corresponding character in the in the encrcyption key
                retvalue=(num_char-1, char, charposition, corchar, alphabet_position(corchar), char)
                ## Update encrypted text
                encrypted_text= encrypted_text + char
                #print(retvalue)
                #return retvalue
                
    return encrypted_text # return the text  enclosed in '': 'text'
    #print(encrypted_text) # print the text  without ''


def main():
    #from helpers import alphabet_position, rotate_character
    alphabet="abcdefghijklmnopqrstuvwxyz"
    u_alphabet=alphabet.upper()
    encryption_key=input("Type your encryption key:  ")
    text= input("Type the text that wil be encrypted:  ")
    num_char=0
    encrypted_text=""
    
    for j in range(len(text)):     ## for lowercase
        if text[j] in alphabet: #or text[j] in alphabet.upper():
            char= text[j]
            charposition=alphabet_position(char)
            num_char+=1
            corchar=encryption_key[(num_char-1)%len(encryption_key)]
            retvalue=(num_char-1, char, charposition, corchar, alphabet_position(corchar), alphabet[(charposition+alphabet_position(corchar))%len(alphabet)]  )
            encrypted_text= encrypted_text + alphabet[(charposition+alphabet_position(corchar))%len(alphabet)]
            #return retvalue
            #print(retvalue)
           
        else:                       ## for uppercases     
            if text[j] in alphabet.upper(): #or text[j] in alphabet.upper():
                char= text[j]
                charposition=alphabet_position(char)
                num_char+=1
                corchar = encryption_key[(num_char-1)%len(encryption_key)] ## corresponding character in the in the encrcyption key
                
                ### built here the for each character from a text a sixtuplet: retvalue = ( a, b, c,d,  e, f ); where
                ## a: position of the character in the given text, b caharacter of the text referenced by "a";
                ## c: position in the alphabet; d: correspoding character from the given encryption key
                ## e: position of "d" in the alphabet
                ## f: the resulted encrypted character
                retvalue=(num_char-1, char, charposition, corchar, alphabet_position(corchar), u_alphabet[(charposition+alphabet_position(corchar))%len(alphabet)])
                ## Update encrypted text
                encrypted_text= encrypted_text + u_alphabet[(charposition+alphabet_position(corchar))%len(u_alphabet)]
            
            else:                 ## character not in alphabet: number, %$&*())_"::><?@#!~|}][\=-)'/ ...etc
                char= text[j]
                charposition=alphabet_position(char)
                num_char= num_char
                corchar="n/a" ## corresponding character in the in the encrcyption key
                retvalue=(num_char-1, char, charposition, corchar, alphabet_position(corchar), char)
                ## Update encrypted text
                encrypted_text= encrypted_text + char
                #print(retvalue)
                #return retvalue
                
    #return encrypted_text # return the text  enclosed in '': 'text'
    print(encrypted_text) # print the text  without ''


if __name__ == "__main__":
    main()
    

