class car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour
        self.for_sale = for_sale

    def drive(self):
        print("vroom vroom")
    def stop(self):
        print("brakeeeee")
    def honk(self):
        print("beep beep")
    def park(self):
        print("parking the car")
    def sell(self):
        if self.for_sale:
            print(f"sold the {self.model}")
        else:
            print(f"{self.model} is not for sale")