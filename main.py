from utils.utils import get_data, get_filtered_data, get_last_data, get_formatted_data


def main():
    operations_url = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?" \
                     "spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a1" \
                     "3d-aad1945e5421&expirationTimestamp=1677598782588&signature=_sYHlRCmRxn3Ydwl9DTuiG" \
                     "_SMFIWMVJ-d34j8CU6FX0&downloadName=operations.json"
    count_last_values = 5
    filtered_empty_from = True

    data, info = get_data(operations_url)

    if not data:
        exit(info)

    print(info, end="\n\n")

    data, info = get_filtered_data(data, filtered_empty_from)
    data, info = get_last_data(data, count_last_values)
    data, info = get_formatted_data(data)

    for row in data:
        print(row)


main()
