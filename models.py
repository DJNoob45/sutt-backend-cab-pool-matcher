import time

CITIES = ["Delhi", "Jaipur"]
SLOTS = ["Morning", "Afternoon", "Evening", "Night"]

class RideRequest:
    def __init__(self, name, city, slot, year):
        self.name = name
        self.city = city
        self.slot = slot
        self.year = year
        self.time = time.strftime("%Y-%m-%d %H:%M:%S")

class Cab:
    def __init__(self, driver, seats, city, slot):
        self.driver = driver
        self.seats = seats
        self.city = city
        self.slot = slot
        self.left = False
        self.students = []        