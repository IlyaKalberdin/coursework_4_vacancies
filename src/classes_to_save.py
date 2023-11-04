from abc import ABC, abstractmethod
import os.path
import json


class SaveToFile(ABC):
    """Абстрактный класс для работы с файлом"""
    @abstractmethod
    def save_data(self, data):
        """Метод для сохранения данных в файл"""
        pass

    @abstractmethod
    def get_data(self, param):
        """Метод для получения данных из файла по параметрам"""
        pass

    @abstractmethod
    def delete_data(self):
        """Метод для удаления данных из файла"""
        pass


class SaveToFileJSON(SaveToFile):
    """Класс для работы с json файлом """
    def save_data(self, data):
        """Метод для сохранения данных в json файл"""
        with open(os.path.join("../", "data", "data.json"), "w", encoding="utf-8") as file:
            all_data = []

            for d in data:
                all_data.append({"name": d.name,
                                 "salary_from": d.salary_from,
                                 "salary_to": d.salary_to,
                                 "currency": d.currency,
                                 "area": d.area,
                                 "url": d.url,
                                 "description": d.description,
                                 "requirements": d.requirements})

            json.dump(all_data, file, ensure_ascii=False)

    def get_data(self, param):
        """Метод для получения данных из json файла по параметрам"""
        sorted_data = []

        with open(os.path.join("../", "data", "data.json"), "r", encoding="utf-8") as file:
            data = json.load(file)

            for vacancy in data:
                for element in vacancy.values():
                    if param in str(element):
                        sorted_data.append(vacancy)

        return sorted_data

    def delete_data(self):
        """Метод для удаления данных из json файла"""
        with open(os.path.join("../", "data", "data.json"), "w", encoding="utf-8") as file:
            file.write("")
