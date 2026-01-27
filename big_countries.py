# https://leetcode.com/problems/big-countries/

import pandas as pd

# given data
data = {
    'name': ['China', 'India', 'France', 'Iceland'],
    'population': [1400000000, 1380000000, 67000000, 370000],
    'area': [9596961, 3287263, 551695, 103000]
}
# create a dataframe
world = pd.DataFrame(data)

# function
def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    
    # df is used to store the filtered DataFrame
    df = world[(world['area'] >= 3000000) | (world['population'] >= 25000000)]
    # return the result set
    return df[['name','population','area']]

result = big_countries(world)
print(result)