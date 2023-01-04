class Calculator(object):
    """
    Calculator class containing basic math operations.
    """

    def __init__(self, first_term=0, second_term=0):
        self.first_term = first_term
        self.second_term = second_term

    def add(self):
        return self.first_term + self.second_term

    def subtract(self):
        return self.first_term - self.second_term

    def multiply(self):
        return self.first_term * self.second_term

    def divide(self):
        if self.second_term == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.first_term / self.second_term

    def square(self):
        return self.first_term ** 2

    def square_root(self):
        return self.first_term ** .5
