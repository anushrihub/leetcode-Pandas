import pandas as pd


daily_sales = pd.DataFrame(
                {   'date_id': ['2020-12-8', '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7',
                '2020-12-8', '2020-12-8', '2020-12-7', '2020-12-7', '2020-12-7'],
    'make_name': ['toyota', 'toyota', 'toyota', 'toyota', 'toyota',
                  'honda', 'honda', 'honda', 'honda', 'honda'],
    'lead_id': [0, 1, 1, 0, 0, 1, 2, 0, 1, 2],
    'partner_id': [1, 0, 2, 2, 1, 2, 1, 1, 2, 1]
                }
)


def daily_leads_and_partners(daily_sales: pd.DataFrame):
    df = daily_sales.groupby(['date_id','make_name']).agg(
        {   'lead_id':'nunique',
            'partner_id':'nunique'
        }).reset_index()

    df = df.rename(columns= {
        'lead_id': 'unique_leads',
        'partner_id': 'unique_partners'
    })
    return df


result = daily_leads_and_partners(daily_sales)
print(result)