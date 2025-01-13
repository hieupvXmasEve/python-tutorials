class Car:
    def __init__(self, brand, model) -> None:
        self.brand = brand
        self.model = model
        pass

    def start_engine(self):
        print("Engine started")
        pass

    def stop_engine(self):
        print("Engine stopped")
        pass


# Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, battery) -> None:
        super().__init__(brand, model)
        self.battery = battery
        pass

    def start_engine(self):
        print("Engine started")
        print("Battery charged")
        pass

    def stop_engine(self):
        print("Engine stopped")
        print("Battery discharged")
        pass


class Bird:
    def fly(self):
        print("Bird flies")


class Airplane:
    def fly(self):
        print("Airplane flies")


# Tạo một hàm let_it_fly() có thể nhận cả Bird và Airplane làm đối số.
def let_it_fly(bird: Bird, airplane: Airplane):
    bird.fly()
    airplane.fly()


def main():
    car = Car("Toyota", "Corolla")
    car.start_engine()
    car.stop_engine()

    electrict_car = ElectricCar("Tesla", "Model S", "90%")
    electrict_car.start_engine()
    electrict_car.stop_engine()


if __name__ == "__main__":
    main()
