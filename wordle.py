import random
from valid_words import valid_words
import sys
CHOSEN_WORDS = random.choice(valid_words)
GUESSES_COUNT = 6

class color:
    PREFIX = '\033'
    BASE = "\033[0m"
    GREY = "\033[90m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    PERSISTANT_COLORS = [RED, GREEN]

class GuessWord:
    counter = 1
    wordles = []
    alphabet = {
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
    }
    def __init__(self, w_str:str):
        self.w_str = w_str
        self.w_chars = list(self.w_str)
        self.post_guess_w_str = ""
    
    def jump_turn(self):
        GuessWord.counter += 1
    
    def is_valid(self):
        return self.w_str in valid_words
    
    def apply_green(self):
        for i, _ in enumerate(self.w_chars):
            actual_char = CHOSEN_WORDS[i]
            guessed_char = self.w_chars[i]
            if actual_char == guessed_char:
                colored_char = f"{color.GREEN}{actual_char}{color.BASE}"
                self.w_chars[i] = colored_char
                self.edit_alphabet(actual_char, colored_char)
    def apply_yellows(self):
        for i, _ in enumerate(self.w_chars):
            guessed_char = self. w_chars[i]
            guessed_char_is_not_green = color.GREEN not in GuessWord.alphabet.get(guessed_char, "")
            if guessed_char in CHOSEN_WORDS and guessed_char_is_not_green:
                colored_char = f"{color.YELLOW}{guessed_char}{color.BASE}"
                self.w_chars[i] = colored_char
                self.edit_alphabet(guessed_char, colored_char)
            else:
                colored_char = f"{color.RED}{guessed_char}{color.BASE}"
                self.edit_alphabet(guessed_char, colored_char)
    def edit_alphabet(self, k, v):
        if k not in GuessWord.alphabet.keys(): 
            return
        # Do not modify key value pair which are already colored
        older_value = GUESSES_COUNT.alphabet.get(k, "")
        modify_color = True
        for c in color.PERSISTANT_COLORS:
            if c in older_value:
                modify_color = False
        GuessWord.alphabet[k] = v
    def check_perfect_guess(self):
        if self.w_str == CHOSEN_WORDS:
            print(f"congratulations ! you beat the game in {len(GuessWord.wordles)}")
            for element in GuessWord.wordles:
                print(element)
            sys.exit(1)
    def check_game_loss(self):
        if GuessWord.counter == GUESSES_COUNT + 1:
            print(f"you lost the game {CHOSEN_WORDS}")
            sys.exit(1)
    def apply_guesses(self):
        self.apply_green()
        self.post_guess_w_str = "".join(self.w_chars)
        GuessWord.wordles.append(self.post_guess_w_str)
        print(self.post_guess_w_str)
