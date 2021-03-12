# import termcolor
import re

HANGMAN_ASCII_ART = """Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/                      
"""
MAX_TRIES = 6


def print_pic1():
	termcolor.cprint("""
	picture 1:
	x-------x
	""", "green")


def print_pic2():
	termcolor.cprint("""
	picture 2:
	x-------x
	|
	|
	|
	|
	|
	""", "green")


def print_pic3():
	termcolor.cprint("""
	picture 3:
	x-------x
	|       |
	|       0
	|
	|
	|
	""", "green")


def print_pic4():
	termcolor.cprint("""
	picture 4:
	x------x
	|      |
	|      0
	|      |
	|
	|
	""", "green")


def print_pic5():
	termcolor.cprint("""
	picture 5:
	x-------x
	|       |
	|       0
	|      /|\\
	|
	|
	""", "green")


def print_pic6():
	termcolor.cprint("""
	picture 6:
	x-------x
	|       |
	|       0
	|      /|\\
	|      / 
	|
	""", "green")


def print_pic7():
	termcolor.cprint("""
	picture 7:
	x-------x
	|       |
	|       0
	|      /|\\
	|      / \\
	|
	""", "green")


def welcome():
	print(HANGMAN_ASCII_ART, MAX_TRIES)


def guess():
	len_flag = False
	special_char_flag = False
	string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
	user_guess = input("Please enter a word: ").lower()
	if len(user_guess) > 1:
		len_flag = True
	if not (string_check.search(user_guess) is None):
		special_char_flag = True
	if special_char_flag and len_flag:
		print("E3")
	elif special_char_flag:
		print("E2")
	elif len_flag:
		print("E1")
	else:
		print(user_guess)


if __name__ == '__main__':
	# welcome()
	guess()
