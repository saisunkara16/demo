class Greetings:
    def __int__(self, my_name):
        self.name = my_name
    def say_hai(self):
        return 'Hello {}!'.format(self.name)
