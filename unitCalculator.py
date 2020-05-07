def gettingValues(self):
    print("\nWhich", self.className, "unit would you like to convert?")
    for key in self.options:
        print(int(key), ":", self.options[key])

    self.choice = checking(self.options)

    print("To which unit? Choose number from same options")
    self.choice2 = checking(self.options)

    print("Give me your", self.className, "value: ")
    self.userValue = checking()

    return self.choice, self.choice2, self.userValue


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
        self.className = "temperature"
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
        self.choice, self.choice2, self.userValue = gettingValues(self)

        self.inCelsius = self.toCelsius()

        print(self.userValue, "in", self.options[self.choice], "is",
              self.toTarget(), "in", self.options[self.choice2])

    def toCelsius(self):
        converter = {
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

    def toTarget(self):
        converter = {
            'Celsius': self.inCelsius,
            'Fahrenheit': 32 + (9 / 5 * self.inCelsius),
            'Kelvin': self.inCelsius + 273.15,
            'Rankine': (self.inCelsius + 273.15) * 9 / 5,
            'Delisle': (100 - self.inCelsius) * 3 / 2,
            'Newton': self.inCelsius * 33 / 100,
            'Réaumur': self.inCelsius * 4 / 5,
            'Rømer': (self.inCelsius * 21 / 40) + 7.5
        }

        return round(converter[self.options[self.choice2]], 3)


class Speed:
    def __init__(self):
        self.className = "speed"
        self.options = {
            1.: 'Kilometers per hour',
            2.: 'Miles per hour',
            3.: 'Meters per second'
        }

        self.choice, self.choice2, self.userValue = gettingValues(self)

        self.inKmH = self.toKmH()

        print(self.userValue, "in", self.options[self.choice], "is",
              self.toTarget(), "in", self.options[self.choice2])

    def toKmH(self):
        converter = {  # From : To Km/H
            'Kilometers per hour': self.userValue,
            'Miles per hour': self.userValue / 0.62137,
            'Meters per second': self.userValue * 3.6
        }

        return converter[self.options[self.choice]]

    def toTarget(self):
        converter = {  # To :
            'Kilometers per hour': self.inKmH,
            'Miles per hour': self.inKmH * 0.62137,
            'Meters per second': self.inKmH / 3.6
        }

        return round(converter[self.options[self.choice2]], 2)


class Distance:
    def __init__(self):
        self.className = "Distance"
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

        self.choice, self.choice2, self.userValue = gettingValues(self)

        self.inMeters = self.toMeters()

        print(self.userValue, "in", self.options[self.choice], "is",
              self.toTarget(), "in", self.options[self.choice2])

    def toMeters(self):
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

    def toTarget(self):
        converter = {  # To :
            'Metre': self.inMeters,
            'Angstrom': self.inMeters / (10**-10),
            'Micron': self.inMeters / (10**-6),
            'Inch': self.inMeters / 0.0254,
            'Foot': self.inMeters / 0.3048,
            'Yard': self.inMeters / 0.9144,
            'Mile (brit.)': self.inMeters / 1609.344,
            'Mile (nautical)': self.inMeters / 1852,
            'Light-year': self.inMeters / (9.46 * (10**15))
        }

        return round(converter[self.options[self.choice2]], 2)


class Capacity:
    def __init__(self):
        print("Currency")
        pass


class Area:
    def __init__(self):
        print("Currency")
        pass


class Weight:
    def __init__(self):
        print("Currency")
        pass


class Currency:
    def __init__(self):
        print("Currency")
        pass


options = {
    1.: 'Temperature',
    2.: 'Speed',
    3.: 'Distance',
    4.: 'Currency',
}

print("\nWhat would you like to convert?\nChoose number from below:")
for key in options:
    print(int(key), ":", options[key])

choice = checking(options)

eval(options[choice])()
