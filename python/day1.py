from sys import argv
script, user_name = argv
x = '>>>'

print("Hi {} , I'm the {} script.".format(user_name , script))
print("I'd like to ask you a few question.")
print("Do you like me {} ?".format(user_name))
likes = input(x)

print("where do you live {} ?".format(user_name))
lives = input(x)

print("what kind of computer do you have ?")
computer = input(x)

print("""
Alright, so you said {} about likeing me .
You live in {}, Not sure where that is.
And you have a {} computer, Nice!
""".format(likes,lives,computer))