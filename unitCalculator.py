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

        print("\nWhich temperature unit would you like to convert?")
        for key in self.options:
            print(int(key), ":", self.options[key])

        self.choice = checking(self.options)

        print("To which unit? Choose number from same options")
        self.choice2 = checking(self.options)

        print("Give me your temperature value: ")
        self.userTemperature = checking()

        self.inCelsius = self.toCelsius()

        print(self.userTemperature, "in", self.options[self.choice], "is",
              self.toTarget(), "in", self.options[self.choice2])

    def toCelsius(self):
        converter = {
            'Celsius': self.userTemperature,
            'Fahrenheit': 5 / 9 * (self.userTemperature - 32),
            'Kelvin': self.userTemperature - 273.15,
            'Rankine': (self.userTemperature * 5 / 9) - 273.15,
            'Delisle': 100 - (self.userTemperature * 2 / 3),
            'Newton': self.userTemperature * 100 / 33,
            'Réaumur': self.userTemperature * 5 / 4,
            'Rømer': (self.userTemperature - 7.5) * 40 / 21
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

        self.options = {
            1.: 'Kilometers per hour',
            2.: 'Miles per hour',
            3.: 'Meters per second'
        }

        print("\nWhich speed unit would you like to convert?")
        for key in self.options:
            print(int(key), ":", self.options[key])

        self.choice = checking(self.options)

        print("To which unit? Choose number from same options")

        self.choice2 = checking(self.options)

        print("Give me your speed value: ")
        self.userSpeed = checking()

        self.inKmH = self.toKmH()

        print(self.userSpeed, "in", self.options[self.choice], "is",
              self.toTarget(), "in", self.options[self.choice2])

    def toKmH(self):
        converter = {  # From : To Km/H
            'Kilometers per hour': self.userSpeed,
            'Miles per hour': self.userSpeed / 0.62137,
            'Meters per second': self.userSpeed * 3.6
        }

        return converter[self.options[self.choice]]

    def toTarget(self):
        converter = {  # To :
            'Kilometers per hour': self.inKmH,
            'Miles per hour': self.inKmH * 0.62137,
            'Meters per second': self.inKmH / 3.6
        }

        return round(converter[self.options[self.choice2]], 2)


class Currency:
    def __init__(self):
        print("Currency")
        pass


options = {
    1.: 'Temperature',
    2.: 'Speed',
    3.: 'Currency'
}

print("\nWhat would you like to convert?\nChoose number from below:")
for key in options:
    print(int(key), ":", options[key])

choice = checking(options)

eval(options[choice])()
