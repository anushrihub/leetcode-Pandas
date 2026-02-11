import pandas as pd

employee = pd.DataFrame(
    {
        'id':[1, 2, 3],
        'salary' : [100, 200, 300]
    }
)

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # as we need only one column (salary) hence used below series 
    salaries = employee['salary'].drop_duplicates().sort_values(ascending= False)
    # salaries are less than 2
    if len(salaries) < 2:
        # return None
        return pd.DataFrame({'SecondHighestSalary': [None]})
    # return the second index from the dataframe
    return pd.DataFrame({'SecondHighestSalary': [salaries.iloc[1]]})

result = second_highest_salary(employee)
print(result)