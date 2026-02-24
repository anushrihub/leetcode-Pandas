import pandas as pd
import numpy as np

products = pd.DataFrame({
    'product_id':[0, 1],
    'store1':[95, 70],
    'store2':[100, np.nan],
    'store3':[105, 80]
})


def rearrange_products_table(products: pd.DataFrame):
    a = products.loc[products['store1'].notna(),['product_id', 'store1']]
    a['store'] = 'store1'
    a.rename(columns={'store1':'price'}, inplace= True)
    a = a[['product_id', 'store', 'price']]
    
    b = products.loc[products['store2'].notna(),['product_id', 'store2']]
    b['store'] = 'store2'
    b.rename(columns={'store2':'price'}, inplace= True)
    b = b[['product_id', 'store', 'price']]

    c = products.loc[products['store3'].notna(),['product_id', 'store3']]
    c['store'] = 'store3'
    c.rename(columns={'store3':'price'}, inplace= True)
    c = c[['product_id', 'store', 'price']]

    ans = pd.concat([a, b, c])
    return ans
result = rearrange_products_table(products)
print(result)
