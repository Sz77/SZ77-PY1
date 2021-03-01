import random
import termcolor

def print_pic1():
	print("""
	x-------x
	""")


def print_pic2():
	print("""
	x-------x
	|
	|
	|
	|
	|
	""")


def print_pic3():
	print("""
	x-------x
	|       |
	|       0
	|
	|
	|
	""")


def print_pic4():
	print("""
	x------x
	|      |
	|      0
	|      |
	|
	|
	""")


def print_pic5():
	print("""
	x-------x
	|       |
	|       0
	|      /|\\
	|
	|
	""")


def print_pic6():
	print("""
	x-------x
	|       |
	|       0
	|      /|
	|      / 
	|
	""")


def print_pic7():
	print("""
	x-------x
	|       |
	|       0
	|      /|\\
	|      / \\
	|
	""")


def welcome():
	print("""
	 _    _                                     
	| |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                         __/ |                      
                        |___/
	""")
	print(random.randint(5, 10))


if __name__ == '__main__':
	welcome()
	print_pic1()
	print_pic2()
	print_pic3()
	print_pic4()
	print_pic5()
	print_pic6()
	print_pic7()
