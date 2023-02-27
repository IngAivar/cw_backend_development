from utils.utils import get_data


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


def test_get_last_data():
    pass
