import pandas as pd

courses = pd.DataFrame(
    {
    "student": ["A", "B", "C", "D", "E", "F", "G", "H", "I"],
    "class": ["Math", "English", "Math", "Biology", "Math", "Computer", "Math", "Math", "Math"]

    }
    )

def find_classes(courses: pd.DataFrame):
    df = courses.groupby('class')['student'].count().reset_index()
    # df = courses.groupby('class')['student'].count()
    result = df[df['student'] >= 5][['class']]
    return result
    # return df
result = find_classes(courses)
print(result)
