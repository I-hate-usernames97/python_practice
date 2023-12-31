old_point_structure = {
    1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
    2: ['D', 'G'],
    3: ['B', 'C', 'M', 'P'],
    4: ['F', 'H', 'V', 'W', 'Y'],
    5: ['K'],
    8: ['J', 'X'],
    10: ['Q', 'Z']
}


def old_scrabble_scorer(word):
    word = word.upper()
    letter_points = ""

    for letter in word:
        for point_value, letters in old_point_structure.items():
            if letter in letters:
                letter_points += f"Points for '{letter}': {point_value}\n"

    return letter_points


def initial_prompt(i):
    while True:
        if i >= 1:
            word = input("Enter a word: ")
            if word.isalpha():  # Check if the input consists only of letters
                return word
            else:
                print("Invalid input. Please enter a word with letters only.")

        word = input("Let's play some scrabble!\nEnter a word: ")
        if word.isalpha():  # Check if the input consists only of letters
            return word
        else:
            print("Invalid input. Please enter a word with letters only.")


def simple_score(word):
    return len(word)


def vowel_bonus_score(word):
    word = word.upper()
    vowel = ['A', 'E', 'I', 'O', 'U']
    point = 0

    for letter in word:
        if letter in vowel:
            point += 3
        else:
            point += 1

    return point


def scrabble_score(word):
    word = word.lower()
    letter_points = 0

    for letter in word:
        if letter in new_point_structure:
            letter_points += new_point_structure[letter]

    return letter_points


scoring_algorithms = [simple_score, vowel_bonus_score, scrabble_score]


def scorer_prompt(word):
    while True:
        choice = input(
            "Which scoring algorithm would you like to use?\n"
            "0 for Simple, Each letter is worth 1 point.\n"
            "1 for Vowel Bonus, Vowels are 3 pts, consonants are 1 pt\n"
            "or 2 for The traditional scoring for Scrabble.\nEnter 0, 1, or 2: "
        )
        if choice.isdigit() and int(choice) in [0, 1, 2]:
            choice = int(choice)
            print(f'Score for "{word}": {scoring_algorithms[choice](word)}')
            break
        else:
            print("Invalid input. Please enter 0, 1, or 2.")


def transform():
    new_point = {}

    for point_value, letters in old_point_structure.items():
        for letter in letters:
            new_point[letter.lower()] = point_value

    return new_point


new_point_structure = transform()


def run_program():
    repeat = True

    i = 0
    while repeat:
        user_input = initial_prompt(i)
        scorer_prompt(user_input)
        stop = input("Do you want to play again? \n (Y) or (N) ")
        if stop.upper() == "N":
            repeat = False
            print("Ok goodbye")
        i += 1



run_program()
