from random import *


def select_word():

    seeds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    seed(choice(seeds))

    word_list = list()
    print("Selecting word now...\n")
    with open("ospd.txt", "r") as file:
        # each line is only one word; append the word to the list
        # and strip it just in case of whitespace
        for line in file:
            word_list.append(line.strip())
    shuffle(word_list)
    hangman_word = choice(word_list)
    # can initialize a list like this out of a string, tuple, etc.
    return hangman_word


def verify_user_input(user_input):
    return len(user_input) == 1 and user_input.isalpha()


def guess_info(guess_limit, guess_count, wrong_chars, test_base):
    print("Guesses made: " + str(guess_count) + "\n")
    print("You have: " + str(round(guess_limit - guess_count)) + " guesses left.\n")
    print("This is what you've already entered: " + wrong_chars)
    print("Here's what the word looks like: ")
    str_base = ""
    for i in range(len(test_base)):
        str_base += test_base[i]
    print(str_base + "\n\n")


def run_game():
    print("Welcome to Hangman!\n")
    word = select_word()
    wrong_chars = test_word = test_base_str = ""
    word_list = list(word)
    for el in word_list:
        test_base_str += "_"
    test_base = list(test_base_str)
    guess_count = 0
    start_len: int = len(word)
    # setting limit on guesses to 1.5 times the length of the string
    guess_limit: int = start_len * 2
    user_input: str = input("Pick a character: ")
    while guess_count < guess_limit and test_word != word:
        if verify_user_input(user_input):
            if word_list.count(user_input) > 0:
                for i in range(len(word)):
                    if word_list[i] == user_input:
                        test_base[i] = word_list[i]
                        word_list[i] = "_"
            else:
                wrong_chars += user_input
        else:
            print("That guess doesn't work - try again!")
        guess_count += 1
        guess_info(guess_limit, guess_count, wrong_chars, test_base)
        test_word = ""
        for i in range(len(test_base)):
            test_word += str(test_base[i])
        if test_word != word:
            user_input = input("Enter in another guess:\n")

    if test_word == word:
        print("Congrats, you won the game!\n")
    else:
        print("Sorry, you lost the game :(\n")

    print("The correct word was " + word + ".")


def main():
    run_game()


if __name__ == "__main__":
    main()
