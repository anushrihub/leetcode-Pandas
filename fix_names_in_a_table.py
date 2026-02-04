import pandas as pd

users = pd.DataFrame(
    {
        'user_id': [1, 2],
        'name': ['aLice', 'bOB']
    }
)

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    users['name'] = users['name'].str.capitalize()
    return users.sort_values('user_id')

result = fix_names(users)
print(result)