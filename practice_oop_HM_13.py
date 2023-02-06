import random
import datetime
countries = ['Ukraine', 'Poland', 'France', 'Canada', 'Germany', 'Portugal']
time_now = datetime.datetime.now()
user_country = countries[random.randint(0, 5)]+' country.'


class Transport:
    """
      A base class representing a transport object.

      Attributes:
          year_of_manufacture: A string representing the year of manufacture.
          speed_limit_for_transport: A string representing the speed limit for transport.
      """
    year_of_manufacture = 'before 2023'
    speed_limit_for_transport = f'Actual speed limit for {time_now} is '+str(random.randint(35, 65))+f'km in hour for' \
                                f' {user_country}'

    def __init__(self, brand: str, number_of_wheels: int, speed_km: int, color: str, price: int):
        """
        Initialize a transport object.

        Args:
            brand: A string representing the brand of the transport(str).
            number_of_wheels: An integer representing the number of wheels(int).
            speed_km: An integer representing the speed in km/h(int).
            color: A string representing the color of the transport(str).
            price: An integer representing the price of the transport(int).
        """
        self.brand = brand
        self.number_of_wheels = number_of_wheels
        self.speed_km = speed_km
        self.color = color
        self.__price = price

    @property
    def price(self):
        """
        Return the price of the transport.
        """
        return self.__price

    @price.setter
    def price(self, new_price: int):
        """
        Set a new price for the transport.

        Args:
            new_price: An integer representing the new price(int).
        """
        if new_price > 0:
            self.__price = new_price
        else:
            print('incorrect value')

    def change_color(self, new_color: str):
        """
        Change the color of the transport.

        Args:
            new_color: A string representing the new color(str).
        """
        self.color = new_color

    def speed_in_miles(self):
        """
        Return the speed of the transport in miles.
        """
        return self.speed_km * 1.60


class Bike(Transport):
    """
     Class to represent a Bike. Inherits from Transport class.

    params:
        brand: brand name of the bike (str).
        number_of_wheels: number of wheels for the bike (int).
        speed_km: speed of the bike in km (int).
        color: color of the bike(str).
    """
    life_time = f'from {random.randint(3, 5)} to {20, 25} years. This statistic is current as of 2023 year.'

    def __init__(self, brand: str, number_of_wheels: int, speed_km: int, color: str, price: int, equipment: list):
        super().__init__(brand, number_of_wheels, speed_km, color, price)
        self.__equipment = equipment

    @property
    def equipment(self):
        """Getter method for the equipment attribute.

        Returns:
            Equipment value for the instance.
        """
        return self.__equipment

    @equipment.setter
    def equipment(self, new_equipment):
        """Setter method for the equipment attribute.

        Args:
            new_equipment: The new value for the equipment attribute(str). This value will be added to the list of
            equipment as new item.
        """
        self.__equipment = self.__equipment.append(new_equipment)


class Automobile(Transport):
    state = 'previously used car'

    def __init__(self, brand: str, number_of_wheels: int, speed_km: int, color: str, price: int,
                 type_car: str, accidents_in_past: bool = False):
        """
        Initializes an instance of the Automobile class.

        Args:
            brand (str): The brand of the automobile.
            number_of_wheels (int): The number of wheels of the automobile.
            speed_km (int): The speed of the automobile in km/hr.
            color (str): The color of the automobile.
            price (int): The price of the automobile.
            type_car (str): The type of car (sedan, SUV, etc.).
            accidents_in_past (bool, optional): Whether the automobile has been in any accidents in the
            past. Default is False.
        """
        super().__init__(brand, number_of_wheels, speed_km, color, price)
        self.type_car = type_car
        self.__accidents_in_past = accidents_in_past

    @property
    def accidents_in_past(self):
        """Getter for the private attribute '__accidents_in_past'.

        Returns:
            bool: The value of '__accidents_in_past'.
        """
        return self.__accidents_in_past

    @accidents_in_past.setter
    def accidents_in_past(self, accidents_in_past):
        """Setter for the private attribute '__accidents_in_past'.

         Args:
             accidents_in_past (bool): The new value for '__accidents_in_past'.
         """
        self.__accidents_in_past = accidents_in_past


class Bus(Transport):
    destination = 'transportation of passengers'

    def __init__(self, brand: str, number_of_wheels: int, speed_km: int, color: str, price: int, passengers):
        super().__init__(brand, number_of_wheels, speed_km, color, price)
        self.passengers = passengers


class Motorcycle(Bike):
    accident_statistics = 'people are 50 times more likely to be killed by motorcyclists than by car. ' \
                          'The statistics are current for 2022.'

    def __init__(self, brand: str, number_of_wheels, speed_km: int, color, price: int, equipment: list, engine_type):
        super().__init__(brand, number_of_wheels, speed_km, color, price, equipment)
        self.engine_type = engine_type


class Truck(Bus):
    def __init__(self, brand: str, number_of_wheels: int, speed_km: int, color, price: int, passengers, horse_power):
        super().__init__(brand, number_of_wheels, speed_km, color, passengers, price)
        self.horse_power = horse_power


velo_max_3000 = Bike('mazda_velo', 2, 25, 'blue', 1000, ['helmet', 'flashlight', 'elbow pads', 'knee pads'])
moto_electro_4000 = Motorcycle('Yamaha', 3, 70, 'red', 40000, ['helmet', 'elbow pads'], 'electric')
electro_bus = Bus('Suzuki', 8, 95, 'grey', 330000, 35)
cybertruck = Truck('Tesla', 4, 170, 'steel', 200000,  4, 900)
car_1992 = Automobile('Zhiguli', 4, 300, 'white', 25000, 'family car', True)

print(moto_electro_4000.engine_type)
print(moto_electro_4000.brand)
print(moto_electro_4000.speed_km)
print(cybertruck.horse_power)

# Next classes will relate to Zoo with animals


class Animal:
    Vaccination = 'Yes'

    def __init__(self, say, weight, age, health):
        self.say = say
        self.weight = weight
        self.age = age
        self.__health = health

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, health):
        self.__health = health


class Bird(Animal):
    def __init__(self, say, weight, age, health, fly_possibility: bool = True):
        super().__init__(say, weight, age, health)
        self.__fly_possibility = fly_possibility

    @property
    def fly_possibility(self):
        return self.__fly_possibility

    @fly_possibility.setter
    def fly_possibility(self, fly_possibility):
        self.__fly_possibility = fly_possibility


class Reptile(Animal):
    def __init__(self, say, weight, age, health, poisoned: bool = True):
        super().__init__(say, weight, age, health)
        self.__poisoned = poisoned

    @property
    def poisoned(self):
        return self.__poisoned

    @poisoned.setter
    def poisoned(self, poisoned):
        self.__poisoned = poisoned


class Mammal(Animal):
    pass


class Eagle(Bird):
    pass


class Colibri(Bird):
    pass


class Snake(Reptile):
    def __init__(self, say, weight, age, health, poisoned: bool = True):
        super().__init__(say, weight, age, health, poisoned)
        self.poisoned = poisoned


class Frog(Reptile):
    def __init__(self, say, weight, age, health, poisoned: bool = False):
        super().__init__(say, weight, age, health, poisoned)
        self.poisoned = poisoned


class Whale(Mammal):
    pass


class Elephant(Mammal):
    pass


frog_shrek = Frog('kva-kva', 3, 70, 'healthy', True)
eagle_bob = Eagle('OuUuUu', 3, 5, 'sick')
print(cybertruck.speed_limit_for_transport)
