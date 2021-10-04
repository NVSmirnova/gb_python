class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return(f"Запуск отрисовки для {self.title}.")

class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return(f"Ручкой на полях рисует {self.title}.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f"Крутой скетч готов с {self.title}.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        return (f"Перманентным {self.title} нарисованы усы у Рейчел.")

kanz = Stationery("Comus")
print(kanz.title)
print(kanz.draw())

ru4ka = Pen("pilot")
print(ru4ka.title)
print(ru4ka.draw())

karandash = Pencil("coh-i-noor")
print(karandash.title)
print(karandash.draw())

marker = Handle("light-green")
print(marker.title)
print(marker.draw())