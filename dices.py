from random import randint


class SixSidedDice:
    def __init__(self):
        self.sides = 6

    def roll_dice_x10(self):
        for i in range(10):
            number = randint(1, 6)
            print(number)


class TenSidedDice:
    def __init__(self):
        self.sides = 10

    def roll_dice_x10(self):
        for i in range(10):
            number = randint(1, 10)
            print(number)


class TwentySidedDice:
    def __init__(self):
        self.sides = 20

    def roll_dice_x10(self):
        for i in range(10):
            number = randint(1, 20)
            print(number)


dice_6 = SixSidedDice()
dice_10 = TenSidedDice()
dice_20 = TwentySidedDice()

dice_6.roll_dice_x10()
print('\n')
dice_10.roll_dice_x10()
print('\n')
dice_20.roll_dice_x10()
