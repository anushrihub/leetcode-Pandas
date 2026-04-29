import pandas as pd

activities = pd.DataFrame(
    {
           "sell_date": [
        "2020-05-30",
        "2020-06-01",
        "2020-06-02",
        "2020-05-30",
        "2020-06-01",
        "2020-06-02",
        "2020-05-30"
    ],
    "product": [
        "Headphone",
        "Pencil",
        "Mask",
        "Basketball",
        "Bible",
        "Mask",
        "T-Shirt"]
    }
)


def categorize_products(activities: pd.DataFrame):
    # create new dataframe
    groups = activities.groupby('sell_date')

    # perform aggregation
    stats = groups.agg(
    num_sold=('product', 'nunique'), 
    products=('product', lambda x: ','.join(sorted(set(x))))
    ).reset_index()

    stats.sort_values('sell_date', inplace=True)

    return stats


result = categorize_products(activities)
print(result)

# without lambda
# def join_sorted_unique(x):
#     return ','.join(sorted(set(x)))

# def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
#     groups = activities.groupby('sell_date')
    
#     stats = groups.agg(
#         num_sold=('product', 'nunique'), 
#         products=('product', join_sorted_unique)  # just pass the function name
#         ).reset_index()
#     stats.sort_values('sell_date', inplace=True)
#     return stats