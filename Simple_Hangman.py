#Hangman game
word = input('Word: ')
l_word = list(word)
count = 0 #5 tries
new_l = list()
HANGMAN_PICS = ['''
     +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
   O   |
  /|\  |
  /    |
      ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

for char in l_word:
    char = '_'
    new_l.append(char)

print(new_l)


while True:
    guess = input('Guess the char: ')
    if guess in l_word:
        for x in range(len(l_word)):
            if l_word[x] == guess:
                for y in range(len(new_l)):
                    if y == x:
                        new_l[y] = l_word[x]
    elif guess not in l_word:
        print(HANGMAN_PICS[count])
        count += 1        
        print('you have {} tries left'.format(7-count))
        
        
        if count == 7:
            print('You lost this game! Try again....')
            print('The secret word is {}'.format(word))
            break
        
    
    print(new_l)
    
    if new_l == l_word:
        print('Congrats you found the secret word: {}'.format(word))
        break
    else:
        pass