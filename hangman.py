my_list = ["Hello", "This", "is", "Python", "Programming", "Beginner", "Level"]
def hangman(my_list):
    import random
    n = random.randint(0, len(my_list) - 1)
    word = my_list[n]
    wrong = 0
    stages = ["                           ",
              "___________________________",
              "|                          ",
              "|           |              ",
              "|           0              ",
              "|          /|\             ",
              "|          / \             ",
              "|                          ",]
    remaining_letters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welome to Hangman.\n")
    while wrong < len(stages) - 1:
        print("\n\n\n")
        choice = input("Guess a character.\n")
        if choice in remaining_letters:
            ch_ind = remaining_letters.index(choice)
            board[ch_ind] = choice
            remaining_letters[ch_ind] = "$"
        else:
            wrong += 1
        print("Your progress: ")
        print("".join(board))
        print("\n".join(stages[0:wrong+1]))
        if "_" not in board:
            print("You win.\n")
            print("".join(board))
            win = True
            break
    if not win:
        print("You lost, word was {}.".format(word))
hangman(my_list)