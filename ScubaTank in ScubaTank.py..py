class ScubaTank:
    def __init__(self, label, bar):
        self.label = label
        self.bar = bar

    def get_bar(self):
        return self.bar

    def set_bar(self, bar):
        if 0 <= bar <= 300:
            self.bar = bar
        else:
            print("Invalid pressure.")

    def fill(self, amount):
        if amount > 0:
            self.__bar += amount
        else:
            print("Invalid amount.")

    def release(self, amount):
        if amount <= 0:
            print("Invalid amount.")
        elif amount > self.__bar:
            print("Not enough air.")
        else:
            self.bar -= amount

    def __str__(self):
        return "Tank " + str(self.label) + ": " + str(self.bar) + " bar"

