import pandas as pd

employee = pd.DataFrame(
    {
        "id" : [1, 2, 3, 4],
        "salary": [100, 200, 300, 300]
    }
)


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Remove duplicate salaries so each salary is counted only once
    dist = employee.drop_duplicates(subset= 'salary')

    # Rank salaries in descending order (highest salary gets rank 1)
    # 'dense' means ranks are consecutive with no gaps
    dist['rnk'] = dist['salary'].rank(method= 'dense', ascending= False)

    # Select the row where the rank equals N and keep only the salary column
    ans = dist[dist.rnk == N][['salary']]

    # If no such rank exists (i.e., N is larger than number of distinct salaries)
    if not len(ans):
        # Return a DataFrame with one column and a None value as required
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Rename the salary column to the required output column name
    ans = ans.rename(columns= {'salary':f'getNthHighestSalary({N})'})

    # Return the final DataFrame containing the N-th highest salary
    return ans

result = nth_highest_salary(employee,2)
print(result)