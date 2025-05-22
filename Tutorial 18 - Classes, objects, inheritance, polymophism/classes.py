class Vehicle:
    # Constructor
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # Refers to itself
    def moves(self):
        print('Moves along...')

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


# Create an object of class Vehicle, fill the required parameter with
# Cadillac and XT5
my_car = Vehicle('Cadillac', 'XT5')
my_car.get_make_model()
my_car.moves()

# Can create multiple objects from said class.
your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()


# Override moves function, and constructs using the
# Original make and model init, but a new faa_id parameters.
class Airplane(Vehicle):
    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print('Flies along...')


# Override moves function
class Truck(Vehicle):
    def moves(self):
        print('Rumbles along...')


# Inherit everything
class GolfCart(Vehicle):
    pass


# Build objects from each child class.
cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golfwagon = GolfCart('Yamaha', 'GC100')


cessna.get_make_model()
cessna.moves()

mack.get_make_model()
mack.moves()

golfwagon.get_make_model()
golfwagon.moves()

print('\n\n')

# simply go through each vehicle and give the make, model, and move message.
for x in (my_car, your_car, cessna, mack, golfwagon):
    x.get_make_model()
    x.moves()
