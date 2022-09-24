import time
def choose_word(pos,path):
    with open(path,'r')as f:
        data = f.read()
    pos %= len(data.split())
    word = data.split()[pos-1]
    total = []
    for i in data.split():
        if i not in total:
            total.append(i)
    return (len(total),word) 

def check_win(secret_word, old_letters_guessed):
    checkWin = ''
    for i in secret_word:
        if i in old_letters_guessed:
            checkWin+=i
    if checkWin == secret_word:
        return True
    return False

def show_hidden_word(secret_word, old_letters_guessed):
    truelet = ''
    for i in secret_word:
        if i in old_letters_guessed:
            truelet+=(i)
        else:
            truelet+=('_')
    return ' '.join(truelet)

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    if len(letter_guessed) == 1 and letter_guessed.isalpha() and not letter_guessed in old_letters_guessed:
        return True
    return 'X \n'+ ' -> '.join(sorted(old_letters_guessed))

def print_hangman(num_of_tries):
    p1,p2,p3,p4,p5,p6,p7='    x-------x','    x-------x\n    |\n    |\n    |\n    |\n    |','    x-------x\n    |       |\n    |       0\n    |\n    |\n    |','    x-------x\n    |       |\n    |       0\n    |       |\n    |\n    |','     x-------x\n    |       |\n    |       0\n    |      /|\\\n    |\n    |\n','     x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      /\n    |\n\n\n','      x-------x\n    |       |\n    |       0\n    |      /|\\\n    |      / \\\n    |\n\n\n'
    HANGMAN_PHOTOS={1:p1,2:p2,3:p3,4:p4,5:p5,6:p6,7:p7}
    return HANGMAN_PHOTOS[num_of_tries]


start = """   
 _    _
| |  | |
| |__| | __ _ _ __   __ _ _ __ ___   __ _ _ ___
|  __  |/ _' | '_ \\/ _' | '_ ' _ \\ / _' | '_   \\
| |  | | (_| | | | | (_| | | | | | | (_| | | | |
|_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\__,_|_| |_|
                __/ |
                |___/
                
                """

def main():
    print(start)
    time.sleep(0.4)
    counter = 1
    path = input('please enter path to list of words: ')
    index = int(input('please enter a number: '))
    _,secretWord = choose_word(index,path)
    print('Lets start!')
    print(print_hangman(counter))
    print(' _ '*len(secretWord))
    old_letters_guessed = []
    while True:
        guess = input('guess a letter: ').lower()
        check = try_update_letter_guessed(guess,old_letters_guessed)
        printH = False
        if check == True:
            old_letters_guessed.append(guess)
        else:
            print(check)
            printH = True
        if guess not in secretWord :
            printH = True
        if printH:
            print('Wrong letter')
            counter+=1
            print(print_hangman(counter))
        print(show_hidden_word(secretWord,old_letters_guessed))
        if check_win(secretWord,old_letters_guessed):
            print('You win!!!')
            break
        if counter == 7:
            print('Game over -_-')
            break
        

       
main()
while True:
    r=input('enter q to quit the game or r to reastart the game ->')
    if r == 'r':
        main()
    elif r == 'q':
        break
