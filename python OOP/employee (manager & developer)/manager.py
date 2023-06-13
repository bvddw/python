from employee import Employee


class Manager(Employee):
    def __init__(self, name: str, salary: int, bonus: int) -> None:
        super().__init__(name, salary)
        self.bonus = bonus

    def __str__(self) -> str:
        return f'{super().__str__()}, Bonus: {self.bonus}'

    def set_bonus(self, bonus):
        self.bonus = bonus

    def get_bonus(self):
        return self.bonus

    @property
    def total_salary(self) -> int:
        return self.salary + self.bonus
