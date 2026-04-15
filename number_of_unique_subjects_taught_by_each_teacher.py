import pandas as pd

data = [
    [1, 2, 3],
    [1, 2, 4],
    [1, 3, 3],
    [2, 1, 1],
    [2, 2, 1],
    [2, 3, 1],
    [2, 4, 1]
]

teacher = pd.DataFrame( data = data, columns= ["teacher_id", "subject_id", "dept_id"]
) 

def count_unique_subjects(teacher: pd.DataFrame):
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    df = df.rename({'subject_id':'cnt'}, axis = 1)
    return df

result = count_unique_subjects(teacher)
print(result)