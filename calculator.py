class Addition:
    def add(self, *args):
        return sum(args)

class Substraction:
    def sub(self, a, b):
        self.a = a
        self.b = b
        return a -b

class Div:
    def div(self, a, b):
        self.a = a
        self.b = b
        return a / b


class Mult:
    def mult(self, a, b):
        self.a = a
        self.b = b
        return a * b
