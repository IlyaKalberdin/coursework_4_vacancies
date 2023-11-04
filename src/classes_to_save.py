from abc import ABC, abstractmethod
import os.path
import json


class SaveToFile(ABC):
    """Абстрактный класс для работы с файлом"""
    @abstractmethod
    def save_vacancies(self, vacancies: list) -> None:
        """Метод для сохранения данных в файл"""
        pass

    @abstractmethod
    def get_vacancy(self, name_vacancy: str) -> list:
        """Метод для получения данных из файла по параметрам"""
        pass

    @abstractmethod
    def delete_vacancies(self) -> None:
        """Метод для удаления данных из файла"""
        pass


class SaveToFileJSON(SaveToFile):
    """Класс для работы с json файлом """
    def save_vacancies(self, vacancies: list) -> None:
        """Метод для сохранения данных в json файл"""
        with open(os.path.join("../", "data", "data.json"), "w", encoding="utf-8") as file:
            all_data = []

            for vacancy in vacancies:
                all_data.append({"name": vacancy.name,
                                 "salary_from": vacancy.salary_from,
                                 "salary_to": vacancy.salary_to,
                                 "currency": vacancy.currency,
                                 "area": vacancy.area,
                                 "url": vacancy.url,
                                 "description": vacancy.description,
                                 "requirements": vacancy.requirements})

            json.dump(all_data, file, ensure_ascii=False)

    def get_vacancy(self, name_vacancy: str) -> dict:
        """Метод для получения данных из json файла по параметрам"""
        with open(os.path.join("../", "data", "data.json"), "r", encoding="utf-8") as file:
            vacancies = json.load(file)

            for vacancy in vacancies:
                if name_vacancy in vacancy["name"]:
                    return vacancy

    def delete_vacancies(self) -> None:
        """Метод для удаления данных из json файла"""
        with open(os.path.join("../", "data", "data.json"), "w", encoding="utf-8") as file:
            file.write("")
