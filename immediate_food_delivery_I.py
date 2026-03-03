import pandas as pd

delivery = pd.DataFrame({"delivery_id": [1, 2, 3, 4, 5, 6],
    "customer_id": [1, 5, 1, 3, 4, 2],
    "order_date": [
        "2019-08-01",
        "2019-08-02",
        "2019-08-11",
        "2019-08-24",
        "2019-08-21",
        "2019-08-11"
    ],
    "customer_pref_delivery_date": [
        "2019-08-02",
        "2019-08-02",
        "2019-08-11",
        "2019-08-26",
        "2019-08-22",
        "2019-08-13"
    ]})


def food_delivery(delivery: pd.DataFrame):
    # find the valid delivery
    is_valid = delivery['order_date'] == delivery['customer_pref_delivery_date']
    valid_count = is_valid.sum()
    total_count = len(delivery)
    percentage = round(valid_count * 100/ total_count, 2)
    df = pd.DataFrame({'immediate_percentage': [percentage]})
    return df


result = food_delivery(delivery)
print(result)