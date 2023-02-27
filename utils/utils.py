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
    :param filtered_empty_from:
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

    for row in data:

        # Приведение даты к правильному формату
        date = datetime.strptime(row['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

        description = row["description"]

        sender = row["from"].split()
        sender_bill = sender.pop(-1)
        sender_bill = f"{sender_bill[:4]} {sender_bill[4:6]}** **** {sender_bill[-4:]}"
        sender_info = " ".join(sender)

        recipient = f"**{row['to'][-4:]}"

        amount = f"{row['operationAmount']['amount']} {row['operationAmount']['currency']['name']}"

        formatted_data.append(f"""\
{date} {description}
{sender_info} {sender_bill} -> {recipient}
{amount}
""")

    return formatted_data, "INFO: Данные отформатированы!"
