class Worker:
    # атрибуты класса
    def __init__(self, name, surname, position, income={"wage": 300, "bonus": 30}):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income#{"wage": 300, "bonus": 30}

class Position(Worker):
    def get_full_name(self):#, name, surname):
        return(f"{self.name} {self.surname}")
    def get_total_income(self):#, income):
        return(self.income["wage"] + self.income["bonus"])


employee = Position("vanya", "ivanov", "doctor")
print(employee.get_full_name())
print(employee.get_total_income())
salary = {"wage": 500, "bonus": 50}
employee2 = Position("vanya", "ivanov", "doctor", salary)
print(employee2.get_full_name())
print(employee2.get_total_income())