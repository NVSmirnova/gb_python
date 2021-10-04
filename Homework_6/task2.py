class Road:
    # атрибуты класса
    def __init__(self, width, length):
        self._width = width
        self._length = length

    # методы класса
    def asfalt(self, kg_4_1_m=0.025, sloj_asfalta=0.05):
        return self._width * self._length * kg_4_1_m * sloj_asfalta

doroga = Road(20, 5000)
print(doroga.asfalt())
print(doroga.asfalt(25, 0.05))
