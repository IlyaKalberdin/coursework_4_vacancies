from abc import ABC, abstractmethod
import requests
import os


class VacanciesApi(ABC):
    """Абстрактный класс для работы с API"""
    @abstractmethod
    def get_vacancies(self, name_vacancies):
        pass


class HeadHunterAPI(VacanciesApi):
    """Класс для получения вакансий с hh.ru"""
    def get_vacancies(self, name_vacancies):
        """Метод для получения вакансий.
           Возвращает вакансии в которых указано ключевое слово name_vacancies.
           Возвращает максимум 100 вакансий"""
        vacancies = requests.get(f"https://api.hh.ru/vacancies?"
                                 f"per_page=100&text={name_vacancies}")

        return vacancies.json()["items"]


class SuperJobAPI(VacanciesApi):
    """Класс для получения вакансий с superjob.ru"""
    def get_vacancies(self, name_vacancies):
        """Метод для получения вакансий.
           Возвращает вакансии в которых указано ключевое слово name_vacancies.
           Возвращает максимум 100 вакансий"""
        api_key = os.getenv('Superjob_API')

        vacancies = requests.get(f"https://api.superjob.ru/2.0/{api_key}/vacancies?"
                                 f"count=100&keyword={name_vacancies}")

        return vacancies.json()["objects"]
