word_list = []

palabra_word_list = input("Ingresa la palabra principal de el juego :\n").lower()
word_list.append(palabra_word_list)
intentos = 6

def display_hangman(intentos):
    stages = [
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     / \\
    ''',
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |     /
    ''',
    '''
       --------
       |      |
       |      O
       |     \\|/
       |      |
       |
    ''',
    '''
       --------
       |      |
       |      O
       |     \\|
       |      |
       |
    ''',
    '''
       --------
       |      |
       |      O
       |      |
       |      |
       |
    ''',
    '''
       --------
       |      |
       |      O
       |
       |
       |
    ''',
    '''
       --------
       |      |
       |
       |
       |
       |
    '''
]

   
    
    return stages[intentos]

a = "_"
word_to_guess = word_list[0]  

revealed_word = a * len(word_to_guess)

while True:
    
    if intentos == 0:
        print("Ya no te quedan intentos\nYour loose")
        break

    print(f"\nTines {intentos} intentos")
    guess = input("\nIngresa una letra: ").lower()
    display = ''
    updated_revealed_word = ""
    found_match = False
    
    for index, letter in enumerate(word_to_guess):
        if letter == guess:
            updated_revealed_word += letter
            found_match = True
        else:
            updated_revealed_word += revealed_word[index]
   
    if guess in revealed_word:
            print("Ya adivinaste esa letra.")
            continue

    if not found_match:
        print("Opss! Palabra incorrecta")
        intentos-=1 
     
    revealed_word = updated_revealed_word
    print(display_hangman(6- intentos))
    print(display)

    
    print(f"Palabra actual: {revealed_word}")
    if revealed_word == word_to_guess:
        
        print("\n-----------------------------------------------------\n🥳FELICIDADES🥳\n¡Adivinaste la palabra!😎")
        break
    
