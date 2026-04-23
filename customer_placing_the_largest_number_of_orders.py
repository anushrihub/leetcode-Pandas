import pandas as pd

orders = pd.DataFrame(
    {
        'order_number':(1, 2, 3, 4),
        'customer_number':(1, 2, 3, 3)
    }
)

def largest_orders(orders: pd.DataFrame):
    df = orders.groupby('customer_number')['order_number'].count().reset_index(name = 'count')
    # inplace=True means it modifies df directly instead of creating a new dataframe
    df.sort_values(by = 'count', ascending= False, inplace= True)
    # first row at index 0
    return df[['customer_number']][0:1]

result = largest_orders(orders)
print(result)
    