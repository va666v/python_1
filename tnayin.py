#product - season - brand -contry
class Country():
    def __init__(self, name, continent):
        self.name = name
        self.continent = continent

    def present(self):
        print(f"{self.name} in {self.continent}")

class Brand(Country):
    def __init__(self, brand_name, business_s_date, name, continent):
        self.brand_name = brand_name
        self.business_s_date = business_s_date
        super().__init__(name, continent)


    def present_brand(self):
        print(f"{self.brand_name} started at {self.business_s_date}")

class Season(Brand):
    def __init__(self, season_name, avg_temp, brand_name, business_s_date, name, continent):
        self.season_name = season_name
        self.avg_temp = avg_temp
        super().__init__(brand_name, business_s_date, name, continent)


    def present_season_temp(self):
        print(f"In the {self.season_name} the temperature is {self.avg_temp}")

class Product(Season, Brand, Country):
    def __init__(self, prod_name, prod_type, prod_price, prod_quantity,
                 season_name, avg_temp, brand_name, business_s_date, name, continent):
        self.prod_name = prod_name
        self.prod_type = prod_type
        self.prod_price = prod_price
        self.prod_quantity = prod_quantity
        super().__init__(season_name, avg_temp, brand_name, business_s_date, name, continent)

    def present_prod(self):
        print(f"{self.prod_name} is the {self.prod_type} type\n"
              f"The price is {self.prod_price}.\n"
              f"For this product we have {self.prod_quantity} pcs")

    def discount(self, a):
        self.prod_price = self.prod_price - (self.prod_price * (a/100))

    def increase_quantity(self, pcs):
        self.prod_quantity = self.prod_quantity - pcs

    def decrease_quantity(self, pcs):
        self.prod_quantity = self.prod_quantity - pcs

iphone = Product('Iphone 14', 'smartphone', '1500$', '35', "Spring", 38, "Malatya-bazar", "15.12.2022", "Yerevan", "Armenia")
iphone.present_prod()

# Hotel - Taxi - Tour
class Hotel():
    def __init__(self, hotel_name, place):
        self.hotel_name = hotel_name
        self.place = place
        self.mid_room = {
            "room1": 10000,
            "room2": 10000,
            "room3": 10000
        }
        self.lux_room = {
            "room1": 30000,
            "room2": 30000,
            "room3": 30000
        }

    def present_hotel(self):
        print(f'Welcome {self.hotel_name} hotel in {self.place}.\n'
              'We have rooms mid and luxe.\n')

    def booking(self):
        user_answer = input("We have rooms for 2 type. \n"
                            "mid for price 10000 and lux for 30000)\n"
                            "What you want mid or lux?\n")

        user_answer = user_answer.lower()
        if user_answer == 'mid':
            for i, j in self.mid_room.items():
                type_room = self.mid_room
                print(f'{i} - price {j}')
        elif user_answer == 'lux':
            type_room = self.lux_room
            for i, j in self.lux_room.items():
                print(f'{i} - price {j}')
        else:
            print("Pleas tell mid or lux")

        user_answer2 = input("Please input which room you want!\n"
                             "Input room1, room2 or room3\n")
        user_answer2 = user_answer2.lower()
        if user_answer2 == 'room1':
            print(f'You reserved room1 and have to pay {type_room[user_answer2]}.')
            type_room[user_answer2] = 'close'
        elif user_answer2 == 'room2':
            print(f'You reserved room1 and have to pay {type_room[user_answer2]}.')
            type_room[user_answer2] = 'close'
        elif user_answer2 == 'room3':
            print(f'You reserved room1 and have to pay {type_room[user_answer2]}.')
            type_room[user_answer2] = 'close'

    def aveilable_room_check(self):
        user_answer = input("We have rooms for 2 type. \n"
                            "mid for price 100$-150$ and lux for 250$-350$)\n"
                            "What you want mid or lux?\n")

        user_answer = user_answer.lower()
        if user_answer == 'mid':
            for i, j in self.mid_room.items():
                if j == 'close':
                    print(f"{i} is busy")
                    continue
                else:
                    print(f'{i} is free')
        elif user_answer == 'lux':
            for i, j in self.lux_room.items():
                if j == 'close':
                    print(f"{i} is busy")
                    continue
                else:
                    print(f'{i} is free')
        else:
            print("Pleas tell mid or lux")

class Taxi(Hotel):
    def __init__(self, taxi_name, car_types, hotel_name, place):
        self.taxi_name = taxi_name
        self.car_types = car_types
        self.price_for_tour = 5000
        super().__init__(hotel_name, place)


    def present_taxi(self):
        print(f"Name of taxi - {self.taxi_name}\n"
              f"Type of cars - {self.car_types}\n"
              f"Price of tour is {self.price_for_tour}\n")

    def discount(self, x):
        discount_price = self.price_for_tour - (self.price_for_tour * (x / 100))
        print(f"The price is disconted {x}%, now is {discount_price}")

class Tour(Taxi, Hotel):
    def __init__(self, tour_name, taxi_name, car_types, hotel_name, place):
        self.tour_name = tour_name
        self.price_luxe = 35000
        self.price_mid = 15000
        super().__init__(taxi_name, car_types, hotel_name, place)

    def present_tour(self):
         print(f"We have {self.tour_name} tour.\n"
              f"If you live in hotel mid room is price become {self.price_mid}(with taxi).\n"
              f"If you live in hotel lux room is price become {self.price_luxe}(with taxi).\n")

    def gl_present(self):
        super().present_hotel()
        super().present_taxi()
        self.present_tour()


tour = Tour("Geghard", 'Dalay Lama', 'Luxe', 'Holiday Inn', 'Yerevan')
tour.gl_present()