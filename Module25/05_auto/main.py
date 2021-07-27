from auto import *


car_1 = Auto(0, 0, 45)
bus_1 = Bus(0, 0, 225)

car_1.move(2.82843)
car_1.set_angel(60)
print(car_1)

bus_1.come_in(5)
bus_1.move(2.82843)
bus_1.come_out(1)
print(bus_1)

