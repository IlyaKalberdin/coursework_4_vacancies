class Vacancy:
    """Класс для работы с вакансиями"""
    all_vacancies = []

    def __init__(self, name, url, salary_from, salary_to, currency, description, requirements, area):
        """Инициализация экземпляра класса"""
        self.name = name
        self.url = url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.currency = currency
        self.description = description
        self.requirements = requirements
        self.area = area

        self.all_vacancies.append(self)

    def __str__(self):
        """Метод возвращает информацию о вакансии для пользователя"""
        if self.salary_from != 0 and self.salary_to != 0:
            salary = f"{self.salary_from}-{self.salary_to}"
        elif self.salary_from != 0:
            salary = f"{self.salary_from}"
        elif self.salary_to != 0:
            salary = f"{self.salary_to}"
        else:
            salary = "Не указана"

        if self.currency != "-":
            salary += self.currency

        return ("--------------------------------------------------------------------------------------\n"
                f"{self.name}\n"
                f"{salary}\n"
                f"{self.area}\n"
                f"{self.url}\n"
                f"{self.description}\n"
                f"{self.requirements}\n"
                "--------------------------------------------------------------------------------------")

    def __repr__(self):
        """Метод возвращает все свойства экземпляра класса"""
        return (f"{self.name}\n{self.salary_from}-{self.salary_to}{self.currency}\n"
                f"{self.area}\n{self.url}\n{self.requirements}\n{self.description}")

    @classmethod
    def init_vacancies_headhunter(cls, vacancies):
        """Метод класса для инициализации экземпляров на основе полученных
           вакансий с сайта hh.ru"""
        for vacancy in vacancies:
            name = vacancy["name"].lower()
            url = vacancy["alternate_url"]
            description = vacancy["snippet"]["responsibility"]

            if description is not None:
                description = description.lower()
            else:
                description = ""

            requirements = vacancy["snippet"]["requirement"]

            if requirements is not None:
                requirements = requirements.lower()
            else:
                requirements = ""

            area = vacancy["area"]["name"].lower()

            salary = vacancy["salary"]

            if salary is None:
                salary_from = 0
                salary_to = 0
                currency = "-"
            elif salary["from"] is not None and salary["to"] is not None:
                salary_from = salary["from"]
                salary_to = salary["to"]
                currency = salary["currency"].lower()
            elif salary["from"] is not None:
                salary_from = salary["from"]
                salary_to = 0
                currency = salary["currency"].lower()
            else:
                salary_from = 0
                salary_to = salary["to"]
                currency = salary["currency"].lower()

            if currency == "rur":
                currency = "rub"

            cls(name, url, salary_from, salary_to, currency, description, requirements, area)

    @classmethod
    def init_vacancies_superjob(cls, vacancies):
        """Метод класса для инициализации экземпляров на основе полученных
           вакансий с сайта superjob.ru"""
        for vacancy in vacancies:
            name = vacancy["profession"].lower()
            url = vacancy["link"]
            description = vacancy["candidat"].lower()
            requirements = ""
            area = vacancy["town"]["title"].lower()
            currency = vacancy["currency"].lower()

            if vacancy["payment_from"] != 0 and vacancy["payment_to"] != 0:
                salary_from = vacancy["payment_from"]
                salary_to = vacancy["payment_to"]
            elif vacancy["payment_from"] != 0:
                salary_from = vacancy["payment_from"]
                salary_to = 0
            elif vacancy["payment_to"] != 0:
                salary_from = 0
                salary_to = vacancy["payment_to"]
            else:
                salary_from = 0
                salary_to = 0

            cls(name, url, salary_from, salary_to, currency, description, requirements, area)

    @classmethod
    def sorted_vacancies_salary(cls):
        """Метод класса для сортировки по зарплате.
           Сначала идут вакансии с самой высокой минимальной оплатой в долларах.
           Потом в рублях и потом в остальных валютах"""
        cls.all_vacancies.sort(key=lambda vacancy: vacancy.salary_to, reverse=True)
        cls.all_vacancies.sort(key=lambda vacancy: vacancy.salary_from, reverse=True)
        cls.all_vacancies.sort(key=lambda vacancy: vacancy.currency, reverse=True)

    @classmethod
    def get_sorted_vacancies(cls, keyword):
        """Метод класса, который возвращает список вакансий по ключевому слову"""
        sorted_vacancies = []

        for vacancy in cls.all_vacancies:
            if keyword in vacancy.__repr__():
                sorted_vacancies.append(vacancy)

        return sorted_vacancies

    @staticmethod
    def get_top_vacancies(vacancies, top_n):
        """Метод, который возвращает топ n вакансий из списка"""
        return vacancies[:top_n]
