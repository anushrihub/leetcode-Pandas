import pandas as pd

ads  =   pd.DataFrame({
            "ad_id": [1, 2, 3, 5, 1, 2, 3, 1, 2, 1],
            "user_id": [1, 2, 3, 5, 7, 7, 5, 4, 11, 2],
            "action": ["Clicked", "Clicked", "Viewed", "Ignored", "Ignored", "Viewed", "Clicked", "Viewed", "Viewed", "Clicked"]
        })


import numpy as np
def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    # Create numeric indicators
    ads['clicks'] = (ads['action'] == 'Clicked')
    ads['total'] = (ads['action'] != 'Ignored')
    
    # Group by ad_id for two columns clicks and total and sum
    df = ads.groupby('ad_id')[['clicks', 'total']].sum().reset_index()
    
    # Calculate CTR
    df['ctr'] = (df['clicks'] * 100 / df['total']).round(2).fillna(0)
    
    # Return sorted result
    return df[['ad_id', 'ctr']].sort_values(by=['ctr', 'ad_id'], ascending=[False, True])
 
    

result = ads_performance(ads)
print(result)