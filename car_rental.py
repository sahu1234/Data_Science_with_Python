# car_rental.py
from datetime import datetime

#Define car rental class with constructor
class CarRental:
    def __init__(self, available_cars):
        self.available_cars = available_cars
        self.rented_cars = {}

    #define available cars function
    def display_available_cars(self):
        print("Available Cars:")
        for car, quantity in self.available_cars.items():
            print(f"{car}: {quantity}")

    #Define Rent hourly function
    def rent_hourly(self, car, num_cars, rent_time):
        if self.available_cars.get(car, 0) >= num_cars and num_cars > 0:
            self.available_cars[car] -= num_cars
            self.rented_cars[(car, rent_time)] = (num_cars, 'hourly')
            print(f"{num_cars} {car}(s) rented on hourly basis at {rent_time}.")
        else:
            print("Sorry, requested cars are not available for hourly rent.")

    #Define Rent daily function
    def rent_daily(self, car, num_cars, rent_time):
        if self.available_cars.get(car, 0) >= num_cars and num_cars > 0:
            self.available_cars[car] -= num_cars
            self.rented_cars[(car, rent_time)] = (num_cars, 'daily')
            print(f"{num_cars} {car}(s) rented on daily basis at {rent_time}.")
        else:
            print("Sorry, requested cars are not available for daily rent.")

     #Define Rent weekly function
    def rent_weekly(self, car, num_cars, rent_time):
        if self.available_cars.get(car, 0) >= num_cars and num_cars > 0:
            self.available_cars[car] -= num_cars
            self.rented_cars[(car, rent_time)] = (num_cars, 'weekly')
            print(f"{num_cars} {car}(s) rented on weekly basis at {rent_time}.")
        else:
            print("Sorry, requested cars are not available for weekly rent.")

     #Define Return cars function
    def return_cars(self, car, rent_time):
        print(f"Attempting to return {car} at {rent_time}")
        print("Rented Cars:", self.rented_cars)
        if (car, rent_time) in self.rented_cars:
            num_cars, rent_period = self.rented_cars.pop((car, rent_time))
            self.available_cars[car] += num_cars
            current_time = datetime.now()
            rental_duration = current_time - rent_time
            if rent_period == 'hourly':
                bill = rental_duration.seconds / 3600 * 10 * num_cars
            elif rent_period == 'daily':
                bill = rental_duration.days * 24 * 10 * num_cars
            else:
                bill = rental_duration.days * 7 * 10 * num_cars
            print(f"{num_cars} {car}(s) returned. Your total bill is: ${bill}.")
        else:
            print("Invalid return request.")

#creating customer class
class Customer:
    def request_rental(self, car_rental, car, num_cars, rent_time, rent_period):
        if rent_period == 'hourly':
            car_rental.rent_hourly(car, num_cars, rent_time)
        elif rent_period == 'daily':
            car_rental.rent_daily(car, num_cars, rent_time)
        elif rent_period == 'weekly':
            car_rental.rent_weekly(car, num_cars, rent_time)
        else:
            print("Invalid rental period choice.")

    def return_rental(self, car_rental, car, rent_time):
        car_rental.return_cars(car, rent_time)
