import random
import termcolor


def print_pic1():
	termcolor.cprint("""
	picture 1:
	x-------x
	""","green")


def print_pic2():
	termcolor.cprint("""
	picture 2:
	x-------x
	|
	|
	|
	|
	|
	""","green")


def print_pic3():
	termcolor.cprint("""
	picture 3:
	x-------x
	|       |
	|       0
	|
	|
	|
	""","green")


def print_pic4():
	termcolor.cprint("""
	picture 4:
	x------x
	|      |
	|      0
	|      |
	|
	|
	""","green")


def print_pic5():
	termcolor.cprint("""
	picture 5:
	x-------x
	|       |
	|       0
	|      /|\\
	|
	|
	""","green")


def print_pic6():
	termcolor.cprint("""
	picture 6:
	x-------x
	|       |
	|       0
	|      /|\\
	|      / 
	|
	""","green")


def print_pic7():
	termcolor.cprint("""
	picture 7:
	x-------x
	|       |
	|       0
	|      /|\\
	|      / \\
	|
	""","green")


def welcome():
	termcolor.cprint("""
	 _    _                                     
	| |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/
	""","blue")
	termcolor.cprint(random.randint(5, 10),"red")


if __name__ == '__main__':
	welcome()
	print_pic1()
	print_pic2()
	print_pic3()
	print_pic4()
	print_pic5()
	print_pic6()
	print_pic7()
