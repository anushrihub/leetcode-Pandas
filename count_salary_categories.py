import pandas as pd

accounts = pd.DataFrame({
    "account_id" : [3,2,8,6],
    "income" : [108939, 12747, 87709, 91796]
})


def count_salary_categories(accounts: pd.DataFrame):
    # find the low salary
    LowSalary =  (accounts['income'] < 20000).sum()
    # find the average salary
    AverageSalary = ((accounts['income'] >= 20000) & (accounts['income'] <= 50000)).sum()
    # find the high salary
    HighSalary = (accounts['income'] > 50000).sum()
    # create a dataframe
    return pd.DataFrame({'category': ['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count': [LowSalary, AverageSalary, HighSalary]})
    

result = count_salary_categories(accounts)
print(result)