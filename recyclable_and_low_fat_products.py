import pandas as pd
# given data
data = { 'product_id':[0,1,2,3,4],
        'low_fats':['Y','Y','N','Y','N'],
        'recyclable':['N','Y','Y','Y','N']
}

# create a dataframe
products = pd.DataFrame(data)

# write a function
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    df = products[(products['low_fats'] == 'Y') & 
                  (products['recyclable'] =='Y')]
    return df[['product_id']]

result = find_products(products)
print(result)

    
