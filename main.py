import random


def play_wordle():
    word_bank=["apple"]
    red="\033[31m"
    green="\033[32m"
    yellow="\033[33m"
    reset="\033[0m"
    while True:
        secret_word=random.choice(word_bank)
        max_attempts=6
        attempts=0
        while attempts<max_attempts:
            guess=input(f"Enter your guess number {attempts} here : ").strip()
            
            lenght=len(guess)
            
            if lenght !=5:
                print(f"the word you pick should be composed of 5 letters")  
           
            if lenght ==5:
                attempts +=1
                if any(char.isdigit() for char in guess):
                    print("the guess can't contain numbers !!")
                else:
                    valid=True
                    output=""
                    list_guess=list(guess)
                    list_ans=list(secret_word)
                    print(list_ans)
                    print(list_guess)
                    for char_2 ,char_1 in zip(list_ans,list_guess):
                        if char_1 == char_2:
                            output += f'{green} {char_1} {reset}'
                        if char_1 not in list_ans:
                            output+=f'{red} {char_1} {reset}'
                        if char_1 in list_ans and char_1 != char_2:
                            output+=f'{yellow} {char_1} {reset}'
                   
                        
                    print(output)
                    if guess==secret_word:
                        print(f'congrats you won!!')
                        break

  
play_wordle()

