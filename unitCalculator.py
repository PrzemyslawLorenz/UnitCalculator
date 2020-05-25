def getting_values(self):
    print("\nWhich", type(self).__name__, "unit would you like to convert?")
    for key in self.options:
        print(int(key), ":", self.options[key])

    self.choice = checking(self.options)

    print("To which unit? Choose number from same options")
    self.choice2 = checking(self.options)

    print("Give me your", type(self).__name__, "value: ")
    self.userValue = checking()

    self.inDefault = self.to_default()

    print(self.userValue, "in", self.options[self.choice], "is",
          self.to_target(), "in", self.options[self.choice2])


def checking(options=False):
    while True:
        try:
            value = float(input())
            if options:
                while value not in options:
                    value = float(
                        input("Wrong number. Choose number from available options\n"))
            break
        except ValueError:
            print("Your value must be integer or float type")

    return value


class Temperature:
    def __init__(self):
        self.choice, self.choice2, self.userValue, self.inDefault = 0, 0, 0, 0
        self.options = {
            1.: 'Celsius',
            2.: 'Fahrenheit',
            3.: 'Kelvin',
            4.: 'Rankine',
            5.: 'Delisle',
            6.: 'Newton',
            7.: 'Réaumur',
            8.: 'Rømer'
        }

        getting_values(self)

    def to_default(self):
        converter = {  # From : To Celsius
            'Celsius': self.userValue,
            'Fahrenheit': 5 / 9 * (self.userValue - 32),
            'Kelvin': self.userValue - 273.15,
            'Rankine': (self.userValue * 5 / 9) - 273.15,
            'Delisle': 100 - (self.userValue * 2 / 3),
            'Newton': self.userValue * 100 / 33,
            'Réaumur': self.userValue * 5 / 4,
            'Rømer': (self.userValue - 7.5) * 40 / 21
        }

        return converter[self.options[self.choice]]

    def to_target(self):
        converter = {  # To :
            'Celsius': self.inDefault,
            'Fahrenheit': 32 + (9 / 5 * self.inDefault),
            'Kelvin': self.inDefault + 273.15,
            'Rankine': (self.inDefault + 273.15) * 9 / 5,
            'Delisle': (100 - self.inDefault) * 3 / 2,
            'Newton': self.inDefault * 33 / 100,
            'Réaumur': self.inDefault * 4 / 5,
            'Rømer': (self.inDefault * 21 / 40) + 7.5
        }

        return round(converter[self.options[self.choice2]], 3)


class Speed:
    def __init__(self):
        self.choice, self.choice2, self.userValue, self.inDefault = 0, 0, 0, 0
        self.options = {
            1.: 'Kilometers per hour',
            2.: 'Miles per hour',
            3.: 'Meters per second'
        }

        getting_values(self)

    def to_default(self):
        converter = {  # From : To Km/H
            'Kilometers per hour': self.userValue,
            'Miles per hour': self.userValue / 0.62137,
            'Meters per second': self.userValue * 3.6
        }

        return converter[self.options[self.choice]]

    def to_target(self):
        converter = {  # To :
            'Kilometers per hour': self.inDefault,
            'Miles per hour': self.inDefault * 0.62137,
            'Meters per second': self.inDefault / 3.6
        }

        return round(converter[self.options[self.choice2]], 2)


class Distance:
    def __init__(self):
        self.choice, self.choice2, self.userValue, self.inDefault = 0, 0, 0, 0
        self.options = {
            1.: 'Metre',
            2.: 'Angstrom',
            3.: 'Micron',
            4.: 'Inch',
            5.: 'Foot',
            6.: 'Yard',
            7.: 'Mile (brit.)',
            8.: 'Mile (nautical)',
            9.: 'Light-year'
        }

        getting_values(self)

    def to_default(self):
        converter = {  # From : To Meters
            'Metre': self.userValue,
            'Angstrom': self.userValue * (10**-10),
            'Micron': self.userValue * (10**-6),
            'Inch': self.userValue * 0.0254,
            'Foot': self.userValue * 0.3048,
            'Yard': self.userValue * 0.9144,
            'Mile (brit.)': self.userValue * 1609.344,
            'Mile (nautical)': self.userValue * 1852,
            'Light-year': self.userValue * 9.46 * (10**15)
        }

        return converter[self.options[self.choice]]

    def to_target(self):
        converter = {  # To :
            'Metre': self.inDefault,
            'Angstrom': self.inDefault / (10**-10),
            'Micron': self.inDefault / (10**-6),
            'Inch': self.inDefault / 0.0254,
            'Foot': self.inDefault / 0.3048,
            'Yard': self.inDefault / 0.9144,
            'Mile (brit.)': self.inDefault / 1609.344,
            'Mile (nautical)': self.inDefault / 1852,
            'Light-year': self.inDefault / (9.46 * (10**15))
        }

        return round(converter[self.options[self.choice2]], 2)


class Volume:
    def __init__(self):
        self.choice, self.choice2, self.userValue, self.inDefault = 0, 0, 0, 0
        self.options = {
            1.: 'Litre',
            2.: 'Cubic metre',
            3.: 'Barrel',
            4.: 'Cubic foot',
            5.: 'Cubic decimetre',
            6.: 'Gallon (US)',
            7.: 'Pint (US)',
            8.: 'Cubic inch'
        }

        getting_values(self)

    def to_default(self):
        converter = {  # From : To Liters
            'Litre': self.userValue,
            'Cubic metre': self.userValue * 1000,
            'Barrel': self.userValue * 158.987294928,
            'Cubic foot': self.userValue * 28.316864592,
            'Cubic decimetre': self.userValue * 1,
            'Gallon (US)': self.userValue * 3.785411784,
            'Pint (US)': self.userValue * 0.473176473,
            'Cubic inch': self.userValue * 0.016387064
        }

        return converter[self.options[self.choice]]

    def to_target(self):
        converter = {  # To :
            'Litre': self.inDefault,
            'Cubic metre': self.inDefault / 1000,
            'Barrel': self.inDefault / 158.987294928,
            'Cubic foot': self.inDefault / 28.316864592,
            'Cubic decimetre': self.inDefault / 1,
            'Gallon (US)': self.inDefault / 3.785411784,
            'Pint (US)': self.inDefault / 0.473176473,
            'Cubic inch': self.inDefault / 0.016387064
        }

        return round(converter[self.options[self.choice2]], 2)


options = {
    1.: 'Temperature',
    2.: 'Speed',
    3.: 'Distance',
    4.: 'Volume'
}

print("\nWhat would you like to convert?\nChoose number from below:")
for key in options:
    print(int(key), ":", options[key])

choice = checking(options)

eval(options[choice])()
