import pandas as pd

customers = pd.DataFrame({
    'id': [1, 2, 3, 4],
    'name': ['Joe', 'Henry', 'Sam', 'Max']
})

orders = pd.DataFrame({
    'id': [1,2],
    'customerId':[3,1]
})

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(customers, orders, how= 'left', left_on= 'id', right_on = 'customerId')
    df = df[df['customerId'].isna()]
    df = df[['name']].rename(columns={'name':'customers'})
    return df

result = find_customers(customers, orders)
print(result)

    