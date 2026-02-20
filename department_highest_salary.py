import pandas as pd


employee = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "name": ["Joe", "Jim", "Henry", "Sam", "Max"],
    "salary": [70000, 90000, 80000, 60000, 90000],
    "departmentId": [1, 1, 2, 2, 1]
})

department=  pd.DataFrame({
    "id": [1, 2],
    "name": ["IT", "Sales"]
})



def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    # Merge tables
    df = pd.merge(department, employee, how= 'left', left_on='id', right_on='departmentId')
    # rename tables
    df.rename(columns={'name_x': 'Department', 'name_y': 'Employee', 'salary': 'Salary'}, inplace=True)
    # Select employees whose salary is equal to the department highest salary
    max_salary = df.groupby('Department')['Salary'].transform('max')
    df = df[df['Salary'] == max_salary]
    return df[['Department', 'Employee', 'Salary']]


s = department_highest_salary(employee,department)
print(s)