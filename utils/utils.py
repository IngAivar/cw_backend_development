import requests


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), "INFO: Данные получены!"
    return None, f"WARNING: Статус ответа {response.status_code}"
