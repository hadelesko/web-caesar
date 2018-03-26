def alphabet_position(letter):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    return alphabet.find(letter.lower())
def rotate_character(char, rot):
    alphabet="abcdefghijklmnopqrstuvwxyz" ## Latin alphabet in the right order
    if char in alphabet: ## check if the char is in the alphabet
            ## Return the rotate lowercase character corresponding to the char
            ## using modulo operation
        return alphabet[(alphabet_position(char)+rot)%(len(alphabet))]
    else:
        if char in alphabet.upper():
            alphabet=alphabet.upper() ## get the uppercase of the "alphabet" 
                ## Return the rotate uppercase character corresponding to the "char"
                ## using modulo operation
            return alphabet[(alphabet_position(char)+rot)%(len(alphabet))]
        else:
            return char ## return the charachter if the char is not found in the alhabet
