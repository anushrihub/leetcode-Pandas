import pandas as pd


employees = pd.DataFrame({
    'emp_id': [1, 1, 1, 2, 2],
    'event_day': ['2020-11-28', '2020-11-28', '2020-12-03', '2020-11-28', '2020-12-09'],
    'in_time': [4, 55, 1, 3, 47],
    'out_time': [32, 200, 42, 33, 74]
})



def total_time(employees: pd.DataFrame):
    employees['total_time'] = employees["out_time"] - employees["in_time"]
    employees = employees.groupby(["event_day", "emp_id"])["total_time"].sum().reset_index()
    employees.rename({"event_day": "day"}, axis=1, inplace= True)
    return employees


result = total_time(employees)
print(result)