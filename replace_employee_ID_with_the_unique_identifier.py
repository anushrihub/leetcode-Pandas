import pandas as pd



employees = pd.DataFrame({
    'id': [1, 7, 11, 90, 3],
    'name': ['Alice', 'Bob', 'Meir', 'Winston', 'Jonathan']
})

employee_uni = pd.DataFrame({
    'id': [3, 11, 90],
    'unique_id': [1, 2, 3]
})


def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame):
    df = pd.merge(employees, employee_uni,how= 'left', on ='id')
    return df[['unique_id','name']]
    

result = replace_employee_id(employees, employee_uni)
print(result)