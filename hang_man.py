# Hang - man game
import random
import time


def exit_game():
    accept_exit = input('Czy na pewno chcesz opuścić grę? ')
    if accept_exit.lower() == 'tak':
        return False
    elif accept_exit.lower() == 'nie':
        return True
    else:
        print('Proszę wpisać tak lub nie.\n')
        exit_game()


def blank_space(number_of_blank_spaces):
    letter_list = ['_' for _ in range(number_of_blank_spaces)]
    print(' '.join(letter_list))
    return letter_list


def filling_spaces(word_to_guess, list_of_blank_spaces, guessed_letter):
    i = 0
    for letter in word_to_guess:
        if letter == guessed_letter:
            index = word_to_guess.index(guessed_letter, i)
            list_of_blank_spaces[index] = guessed_letter
            i = index + 1
        else:
            continue
    print(' '.join(list_of_blank_spaces))
    return list_of_blank_spaces


list_of_words = []
with open('hang_man_words.txt', 'r', encoding='UTF-8') as slowa:
    for word in slowa:
        list_of_words.append(word.rstrip())
running = True
while running:
    print('\n------------------------')
    print('Witaj w grze Hang-man!')
    print('------------------------')
    print('1. Rozpocznij grę')
    print('2. Wybierz poziom trudności (w toku)')
    print('3. Wyświetl ranking (w toku)')
    print('4. Wyjdź z programu')
    try:
        choice = int(input('\nProszę wybrać jedną z dostępnych opcji: '))
        if choice == 1:
            life = 5
            bad_letters = []
            used_letters = []
            count = 0
            time.sleep(1)
            word = random.choice(list_of_words)
            letters = len(word)
            print(f'Szukane słowo ma {letters} liter')
            puste_miejsca = blank_space(letters)
            game_over = False
            while not game_over:
                guess = (input('Wpisz swoją literę: ')).lower()

                if guess in puste_miejsca or guess in bad_letters:
                    print('Już wcześniej wpisałeś tę literę!')
                elif len(guess) > 1:
                    print('Proszę wpisywać pojedynczo!\n')
                else:
                    used_letters.append(guess)
                    used_letters_updated = ', '.join(used_letters)
                    print(f'Wykorzystane litery: {used_letters_updated}')
                    if guess in word:
                        print('Trafiłeś!')
                        letters -= word.count(guess)
                        print(f'Pozostało do odgadnięcia: {letters}')

                        puste_miejsca = filling_spaces(word, puste_miejsca, guess)
                        if '_' not in puste_miejsca:
                            print('Wygrałeś! Gratulacje!')
                            game_over = True
                    else:
                        bad_letters.append(guess)
                        print('Nie trafiłeś!')
                        print(f'Pozostało do odgadnięcia: {letters}\n')
                        life = life - 1
                        if life == 4:
                            print('-----\n'
                                  '    |\n')
                            print(f'Pozostały Ci {life} próby\n')
                        elif life == 3:
                            print('-----\n'
                                  '    |\n'
                                  '    o\n')
                            print(f'Pozostały Ci {life} próby\n')
                        elif life == 2:
                            print('-----\n'
                                  '    |\n'
                                  '    o\n'
                                  '    |\n')
                            print(f'Pozostały Ci {life} próby\n')
                        elif life == 1:
                            print('-----\n'
                                  '    |\n'
                                  '    o\n'
                                  '   /|l\n')
                            print(f'Pozostała Ci {life} próba\n')
                        elif life == 0:
                            print('-----\n'
                                  '    |\n'
                                  '    o\n'
                                  '   /|l\n'
                                  '   ( )\n')
                            print(f'Skończyły Ci się próby!\nPrzegrywasz!\nSzukanym słowem było: {word}')
                            time.sleep(5)

                            game_over = True

        elif choice == 4:
            running = exit_game()
    except:
        print('Proszę wprowadzić poprawnie!')

print('Życzymy miłego dnia!')
