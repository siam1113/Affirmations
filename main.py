from greetings import greet
from affirmations import  affirm

name = input("What's your name ? _")
happy = input("Are you happy Y(yes)/N(no)? _")
sad = input("Are you sad Y(yes)/N(no)? _")

print("\n\n")
greet(name)
affirm(happy, sad)


