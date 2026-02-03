import pandas as pd

employees = pd.DataFrame({
            'employee_id': [2,3,7,8,9],
            'name': ['Meir','Michael','Addilyn','Juan','Kannon'],
            'salary': [3000, 3800, 7400, 6100, 7700]
})

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # apply - Run this function row by row
    # x - each row
    employees['bonus'] = employees.apply( lambda x: x['salary'] if x['employee_id'] % 2 == 1 and not x['name'].startswith('M') else 0, axis = 1)
    df = employees[['employee_id', 'bonus']].sort_values('employee_id')
    return df

result = calculate_special_bonus(employees)
print(result)