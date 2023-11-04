from vacancies_api import HeadHunterAPI, SuperJobAPI
from class_vacancy import Vacancy
from classes_to_save import SaveToFileJSON


def main():
    # Ввод данных от пользователя
    name_vacancies = input("Введите наименование вакансии: ").lower()
    keyword = input("Введи значение(город, требования, зарплата и т.п.) по которым "
                    "будет идти сортировка вакансий: ").lower()
    top_n = int(input("Укажите кол-во выводимых в топ n вакансий: "))

    # Создание экземпляров классов для работы с апи
    hh = HeadHunterAPI()
    sj = SuperJobAPI()

    # Получение вакансий по параметру name_vacancies
    vacancies_hh = hh.get_vacancies(name_vacancies)
    vacancies_sj = sj.get_vacancies(name_vacancies)

    # Создание экземпляров вакансий
    Vacancy.init_vacancies_headhunter(vacancies_hh)
    Vacancy.init_vacancies_superjob(vacancies_sj)

    # Сортировка вакансий по зарплате и валюте
    Vacancy.sorted_vacancies_salary()

    # Получение вакансий по переданному ключу keyword
    sorted_vacancies = Vacancy.get_sorted_vacancies(keyword)

    # Получение топ вакансий по top_n
    top_vacancies = Vacancy.get_top_vacancies(sorted_vacancies, top_n)

    # Вывод конечного результата для пользователя
    if len(top_vacancies) == 0:
        print("По таким параметрам вакансий не найдено")
    else:
        for i, vacancy in enumerate(top_vacancies):
            print(f"***********************************{i+1}*****************************************")
            print(vacancy)

    # Сохранение топ вакансий в json файл
    save_vacancies = SaveToFileJSON()
    save_vacancies.save_data(top_vacancies)

    print("Топ вакансии сохранены в файл")


if __name__ == "__main__":
    main()
