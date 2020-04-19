import requests


class User:
    """ A Student class """

    def __init__(self, first, last, marks):
        self.first = first
        self.last = last
        self.marks = marks

    @property
    def email(self):
        return "{}.{}@gmail.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)