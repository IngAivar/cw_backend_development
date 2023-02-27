import requests


def get_data(url):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            return response.json(), "INFO: Данные получены!"

        return None, f"WARNING: Статус ответа {response.status_code}"

    except requests.exceptions.ConnectionError:
        return None, "ERROR: requests.exceptions.ConnectionError"


def get_filtered_data(data):
    data = [x for x in data if "state" in x and x["state"] == "EXECUTED"]

    return data, "INFO: Данные отфильтрованы!"


def get_last_data(data, count_last_values):
    data = sorted(data, key=lambda x: x["date"], reverse=True)

    return data[:count_last_values], "INFO: Данные отсортированы!"


def get_formatted_data(data):
    pass
