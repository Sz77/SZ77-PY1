def main():
    """
    this is the main function of the program
    it has the main game loop and calling all the other functions
    :return: none
    """
    welcome()
    # input and setup
    path, index = input("Enter file path: "), int(input("Enter index: "))
    secret_word = choose_word(path, index)
    is_over = False
    hangman_state = 1
    old_guessed_letters = []
    # main loop
    print("Lets start!")
    while not is_over:
        print_hangman(hangman_state)
        hangman_state += 1

        print(show_hidden_word(secret_word, old_guessed_letters))

        guess = input("Guess a letter: ")

        if try_update_letter_guessed(guess, old_guessed_letters):
            if guess in secret_word:
                hangman_state -= 1
            else:
                print("OOF")
        else:
            hangman_state -= 1

        if check_win(secret_word, old_guessed_letters):
            print(show_hidden_word(secret_word, old_guessed_letters))
            print("WIN GG")
            break

        if hangman_state == 7:
            print_hangman(7)
            print(show_hidden_word(secret_word, old_guessed_letters))
            print("LOSE OOF")
            break


def choose_word(file_path, index):
    """
    this function returns the number of unique_words and the chosen words
    :param file_path:all of the words
    :param index: the index of the chosen words
    :type file_path: file
    :type index: int
    :return: unique_words, word
    :rtype: str
    """
    words = open(file_path, "r").read().split(' ')
    index = (index % len(words) - 1)
    word = words[index]
    return word


def welcome():
    """
    This function prints the starting picture
    :return:
    """
    print("""
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/""")


def print_hangman(num_of_tries):
    """
    prints the hangman by the number of tries
    :param num_of_tries: number of tries
    :type num_of_tries: int
    :return: none
    """
    hangman_dict = {1: """x-------x""", 2: """x-------x
    |
    |
    |
    |
    |""", 3: """x-------x
    |       |
    |       0
    |
    |
    |""", 4: """x-------x
    |       |
    |       0
    |       |
    |
    |""", 5: """x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 6: """x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |
""", 7: """x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}
    print(hangman_dict[num_of_tries])


def show_hidden_word(secret_word, old_letters_guessed):
    """
    this function return string from _ and letters based on
    :param secret_word:the word we guessing
    :param old_letters_guessed:the guessed letters
    :type secret_word: str
    :type old_letters_guessed:list
    :return:the word
    :rtype str:
    """
    word = ""
    i = 0
    for letter in secret_word:
        if letter in old_letters_guessed:
            word = word + secret_word[i]
            if i < len(secret_word) - 1:
                word = word + " "
            i += 1
            continue
        else:
            word = word + "_"
            if i < len(secret_word) - 1:
                word = word + " "
            i += 1
    return word


def check_win(secret_word, old_letters_guessed):
    """
    this function is used to check whether the user won
    :param secret_word: the word we trying to guess
    :param old_letters_guessed: all letters that already been guessed
    :type secret_word: str
    :type old_letters_guessed :list
    :return: False if the user hasn't won, True if he did
    :rtype bool
    """
    for letter in secret_word:
        if letter in old_letters_guessed:

            continue
        else:
            return False
    return True


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    this func checks if its possible to add the letter to the old_letters_guessed list by calling check_valid_input
    :param letter_guessed:  the guess
    :param old_letters_guessed: the list of old letters
    :type letter_guessed str
    :type old_letters_guessed list
    :return: True if possible
    :rtype bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed += [letter_guessed]
        return True
    else:
        print("X")
        old_letters_guessed = ' -> '.join(sorted(old_letters_guessed))
        print(old_letters_guessed)
        return False


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    this func checks if the guess is longer then 1 and if it has something that isn't letters and if it been guessed
    before :param letter_guessed:the guess to check :param old_letters_guessed:the old guess :type letter_guessed:str
    :param letter_guessed:
    :type old_letters_guessed: list :return:True if the guess is valid False is not :rtype bool
    """
    len_flag = False
    already_guessed = False
    special_char_flag = not (letter_guessed.lower().isalpha())
    if len(letter_guessed) > 1:
        len_flag = True
    if letter_guessed.lower() in old_letters_guessed:
        already_guessed = True
    if (not special_char_flag) and (not len_flag) and (not already_guessed):
        return True
    else:
        return False


if __name__ == '__main__':
    main()
