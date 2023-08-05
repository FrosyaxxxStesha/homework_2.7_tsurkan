from json import load
from os.path import join


def load_json(file_name):
    """
    Получает файл json,
    возвращает объект python
    :param file_name:
    :return:
    """
    direct = join("..", "data", file_name)
    with open(direct) as file:
        data_json = load(file)
    return data_json


def get_student_by_pk(pk, struct):
    """
    получает номер и структуру данных,
    возвращает словарь с данными студента или
    соответствующее уведомление, если такого студента
    нет
    :param pk:
    :param struct:
    :return:
    """
    try:
        student = struct[int(pk) - 1]
        return student
    except IndexError:
        return "У нас нет такого студента"


def get_profession_by_title(title, struct):
    """
    Получает название профессии, список профессий,
    возвращает словарь с данными профессии или уведомление в
    случае отсутствия специальности
    :param title:
    :param struct:
    :return:
    """
    for i in struct:
        if i["title"] == title:
            return i
    return "У нас нет такой специальности"


def check_fitness(stud, prof):
    """
    проверяет соответствие студента и
    профессии, выводит соответствующие данные
    :param stud:
    :param prof:
    :return:
    """
    std_skills = set(stud["skills"])
    need_skills = set(prof["skills"])
    has_skills = std_skills.intersection(need_skills)
    lacks_skills = need_skills.difference(std_skills)
    per_of_coin = len(has_skills) * 100 // len(need_skills)
    output_dict = {
        "has": list(has_skills),
        "lacks": list(lacks_skills),
        "fit_percent": per_of_coin
    }
    return output_dict


def check_has(data_dict):
    """
    Проверка наличие скиллов,
    соответствующих профессии
    :param data_dict:
    :return:
    """
    if len(data_dict["has"]) > 0:
        return ", ".join(data_dict["has"])
    return "ничего"


def check_lacks(data_dict):
    """
    Проверка наличия недостающих скиллов
    для профессии
    :param data_dict:
    :return:
    """
    if len(data_dict["lacks"]) > 0:
        return f'не знает {", ".join(data_dict["lacks"])}'
    return "знает всё"
