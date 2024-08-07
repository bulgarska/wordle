import string
import random


def game_instructions():
    print("Game Instructions:\n"
          "Enter a five letter word.\n"
          "🟩 next to a letter means the letter is in the correct position.\n"
          "🟨 next to a letter means the letter is in the incorrect position.\n"
          "⬛ next to a letter means the letter is not in the word.\n")


def get_word_lists(file_path):
    file = file_path
    words_file = open(file, "r")
    words_list = words_file.read().splitlines()
    return words_list


def get_guess():
    guesses_list = get_word_lists("valid_guesses")
    guess = ""
    while len(guess) != 5 or not guess.isalpha() or guess not in guesses_list:
        guess = str(input("Guess a five letter word:\n"))
    return guess


def get_hidden_word():
    list_hidden_words = get_word_lists("classic_answers")
    random_num = random.randrange(0, len(list_hidden_words))
    return list_hidden_words[random_num]


# game loop
def check_word():
    hidden_word = get_hidden_word().upper()
    attempts = 6
    letters_available = list(string.ascii_uppercase)
    letters_not_in_word = []
    guesses_all = []
    while attempts > 0:
        guess = get_guess().upper()
        guesses_all.append(guess)
        if guess == hidden_word:
            print(f"You guessed the word correctly! {hidden_word}\n")
            break
        else:
            attempts -= 1
            print(f"You have {attempts} attempts left.\n")
            letters_checked = []
            letters_output = []
            for guess in guesses_all:
                letter_counter = {}
                for char in hidden_word:
                    letter_counter[char] = hidden_word.count(char)
                for char_hidden, char_guess in zip(hidden_word, guess):
                    if char_guess in hidden_word and char_guess in char_hidden and letter_counter[char_hidden] > 0:
                        letter_counter[char_hidden] -= 1
                        letters_checked.append(char_guess)
                        letters_output.append("🟩")
                    elif char_guess in hidden_word and letter_counter[char_guess] > 0:
                        letter_counter[char_guess] -= 1
                        letters_checked.append(char_guess)
                        letters_output.append("🟨")
                    else:
                        letters_checked.append(char_guess)
                        letters_output.append("⬛")
                        if char_guess in letters_available or not letters_not_in_word:
                            letters_available.remove(char_guess)
                            letters_not_in_word.append(char_guess)
            for start in range(0, len(letters_checked), 5):
                print('  '.join([str(letters_checked[i]) for i in range(start, start + 5)]))
                print(' '.join([str(letters_output[i]) for i in range(start, start + 5)]))
            print("Letters available: ", ' '.join([str(letter) for letter in letters_available]))
            print("Letters not in the word: ", ' '.join([str(letter) for letter in sorted(letters_not_in_word)]))
            if attempts == 0:
                print(f"Game over !!!! The correct word is: {hidden_word}\n")


if __name__ == '__main__':
    game_instructions()
    check_word()
