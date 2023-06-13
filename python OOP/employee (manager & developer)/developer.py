from employee import Employee


class Developer(Employee):
    def __init__(self, name: str, salary: int, programming_languages: list) -> None:
        super().__init__(name, salary)
        self.programming_languages = programming_languages

    def __str__(self) -> str:
        return f'{super().__str__()}, Programming Language: {self.programming_languages}'

    def get_technologies(self) -> list:
        return self.programming_languages
