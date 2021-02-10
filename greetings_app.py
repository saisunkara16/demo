from greetings import Greetings

print('what\'s your name?')
n = input()
g = Greetings(n)
print(g.say_hi())
