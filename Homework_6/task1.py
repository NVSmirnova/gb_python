from time import sleep
class TrafficLight:
    # атрибуты класса
    __TrafficLight_color = "red"

    # методы класса
    def running(self, num_of_circuls=3):
        for i in range(1, num_of_circuls):
            print("red")
            sleep(7)
            print("yellow")
            sleep(2)
            print("green")
            sleep(3)
svetofor_1 = TrafficLight()
print(svetofor_1)
svetofor_1.running()

