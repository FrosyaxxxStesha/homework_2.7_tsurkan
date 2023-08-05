import func


def main():
    """
    Основная программа
    :return:
    """
    # Получаем данные студентов
    data_stud = func.load_json("students.json")
    # Получаем со стандартного ввода номер студента
    pk = input("Введите номер студента:\n")
    # Получаем данные студента по номеру
    stud = func.get_student_by_pk(pk, data_stud)

    # Завершаем программу при неверном номере
    if stud == "У нас нет такого студента":
        print(stud)
        return None

    # Выводим скиллы студента
    print(f'{stud["full_name"]}\nзнает {", ".join(stud["skills"])}')
    # Получаем данные о профессиях
    data_prof = func.load_json("proffessions.json")
    # Получаем название профессии
    prof_name = input(f'Введите название профессии для студента {stud["full_name"]}:\n').capitalize()
    # получаем данные о профессии по названию
    prof = func.get_profession_by_title(prof_name, data_prof)

    # Завершаем программу при неверном названии профессии
    if prof == "У нас нет такой специальности":
        print(prof)
        return None

    # Получаем данные по соответствию
    data_dict = func.check_fitness(stud, prof)
    # Получаем строки наличия и отсутствия скиллов
    has_string = func.check_has(data_dict)
    lacks_string = func.check_lacks(data_dict)
    # Выводим данные по соответствию
    print(f'''Пригодность: {data_dict["fit_percent"]}%
{stud["full_name"]} знает {has_string}
{stud["full_name"]} {lacks_string}''')


main()
