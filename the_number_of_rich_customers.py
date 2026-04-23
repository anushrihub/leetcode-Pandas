import pandas as pd


store = pd.DataFrame({"bill_id": [6, 8, 4, 11, 13],
    "customer_id": [1, 1, 2, 3, 3],
    "amount": [549, 834, 394, 657, 257]})

def count_rich_customers(store: pd.DataFrame):
    # this is the pandas series output
    # count = store[store['amount'] > 500].nunique()
    # return count

    # find the greater then 500 amount
    rich_customers = store[store['amount'] > 500]
    # find the unique id's
    count = rich_customers['customer_id'].nunique()
    # creating a dataframe as output required in df format
    answer = pd.DataFrame({'rich_count': [count]})
    # return the answer
    return answer

result = count_rich_customers(store)
print(result)
