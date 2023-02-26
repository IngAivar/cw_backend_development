from utils.utils import get_data, get_filtered_data, get_last_data


def main():
    operations_url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=" \
                     "0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&" \
                     "expirationTimestamp=1677506820563&signature=xUtvHAi7R26qkBWkadhtR3dolbZS6XtaQyXCVbsY2mM&do" \
                     "wnloadName=operations.json"
    count_last_values = 5

    data, info = get_data(operations_url)

    if not data:
        exit(info)

    print(info)

    data, info = get_filtered_data(data)

    print(info)

    data, info = get_last_data(data, count_last_values)

    print(info)
    print(data)


main()
