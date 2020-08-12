"""
my first class
"""


class Poker:

    def __init__(self, style, point):
        self.style = style
        self.point = point

    def get_style(self):
        return self.style

    def get_value(self):
        return self.point


card1 = Poker("heart", 10)
print(card1.get_style())
print(card1.get_value())
