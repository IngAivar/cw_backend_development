from utils.utils import get_data, get_last_data, get_formatted_data, get_filtered_data


def test_get_data():
    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?" \
          "spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a1" \
          "3d-aad1945e5421&expirationTimestamp=1677598782588&signature=_sYHlRCmRxn3Ydwl9DTuiG" \
          "_SMFIWMVJ-d34j8CU6FX0&downloadName=operations.json"
    assert get_data(url) is not None

    url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?" \
          "spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a1" \
          "3d-aad1945e5421&expirationTimestamp=1677598782588&signature=_sYHlCmRxn3Ydwl9DTuiG" \
          "_SMFIWMVJ-d34j8CU6FX0&downloadName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "WARNING: Статус ответа 400"

    url = "https://file.noton.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?" \
          "spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a1" \
          "3d-aad1945e5421&expirationTimestamp=1677598782588&signature=_sYHlRCmRxn3Ydwl9DTuiG" \
          "_SMFIWMVJ-d34j8CU6FX0&downloadName=operations.json"
    data, info = get_data(url)
    assert data is None
    assert info == "ERROR: requests.exceptions.ConnectionError"


def test_get_last_data(test_data):
    data = get_last_data(test_data, count_last_values=2)
    assert data[0]['date'] == '2019-12-07T06:17:14.634890'
    assert len(data) == 2


def test_get_formatted_data(test_data):
    data = get_formatted_data(test_data[:1])

    assert data == ["07.12.2019 Перевод организации\nVisa Classic 2842 87** **** 9012 -> **3655\n48150.39 USD\n"]

    data = get_formatted_data(test_data[1:2])

    assert data == ["19.11.2019 Перевод организации\n[СКРЫТО]  -> **2869\n30153.72 руб.\n"]
