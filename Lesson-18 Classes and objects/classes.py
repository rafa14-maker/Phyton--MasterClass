class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along..")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}.")


my_car = Vehicle("tesla", "model 3")

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle("cadillac", "Escalade")
your_car.get_make_model()
your_car.moves()


class Airplae(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("files along...")


class Truck(Vehicle):
    def moves(self):
        print("Rumbles along..")


class GolfCart(Vehicle):
    pass


cassna = Airplae("Cessna", "SkyHawk", "N-123445")
mack = Truck("Mack", "Pinnacle")
golfwagon = GolfCart("Yamaga", "GC1000")

cassna.get_make_model()
cassna.moves()
mack.get_make_model()
mack.moves()
golfwagon.get_make_model()
golfwagon.moves()


print("\n\n")

for v in (my_car, your_car, cassna, mack, golfwagon):
    v.get_make_model()
    v.moves()
