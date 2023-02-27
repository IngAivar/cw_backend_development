import requests
from datetime import datetime


def get_data(url):
    """
    Функция берет JSON список переходя по URL ссылке и приводит его в читабельный формат для python
    :param url:
    :return:
    """

    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json(), "INFO: Данные получены!"

        return None, f"WARNING: Статус ответа {response.status_code}"

    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"


def get_filtered_data(data, filtered_empty_from=False):
    """
    Функция фильтрует данные и оставляет только выполненные операции
    :param data:
    :return:
    """

    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]

    if filtered_empty_from:
        data = [x for x in data if "from" in x]

    return data, "INFO: Данные отфильтрованы!"


def get_last_data(data, count_last_values):
    """
    Функция сортирует и упорядочивает данные по дате
    :param data:
    :param count_last_values:
    :return:
    """

    data = sorted(data, key=lambda x: x["date"], reverse=True)

    return data[:count_last_values], "INFO: Данные отсортированы!"


def get_formatted_data(data):
    """
    Функция приводит данные к нужному формату
    :param data:
    :return:
    """

    formatted_data = []

    print(data[0])
    for row in data:

        # Приведение даты к правильному формату
        date = datetime.strptime(row['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        print("data = ", date)
        print("row = ", row)

        return data, "INFO: Данные отформатированы!"
