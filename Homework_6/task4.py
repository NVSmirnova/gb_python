class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return(f"{self.name}, is going.")
    def stop(self):
        return(f"{self.name} stopped")
    def turn_right(self):
        return(f"{self.name} turned right")
    def show_speed(self):
        return(f"{self.name} speed is {self.speed} mlh.")

class TownCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return(f"{self.name} speed is {self.speed} mlh that is higher then limits.")
        else:
            return (f"{self.name} speed is {self.speed} mlh.")

class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return (f"{self.name} speed is {self.speed} mlh that is higher then limits.")
        else:
            return (f"{self.name} speed is {self.speed} mlh.")


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)


mashinka = Car(60, "red", "Volga", False)
print(mashinka.go())
print(mashinka.show_speed())

townCar = TownCar(80, "green", "iVolga")
print(townCar.stop())
print(townCar.show_speed())

police = PoliceCar(110, "blue", "merce")
print(police.turn_right())
print(police.show_speed())

workcar = WorkCar(50, "black", "lada")
print(workcar.go())
print(workcar.stop())
print(workcar.show_speed())