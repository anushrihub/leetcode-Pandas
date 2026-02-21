import pandas as pd

person = pd.DataFrame({
    'id': [1,2,3],
    'email':['john@example.com ', 'bob@example.com', 'john@example.com ']
})

# using drop_duplicate function
def delete_duplicate_emails(person: pd.DataFrame) -> None:
    person.sort_values(by='id', inplace=True)
    person.drop_duplicates(subset=['email'],inplace= True)
    return person

# using group by
# def delete_duplicate_emails(person: pd.DataFrame) -> None:
#     min_id = person.groupby('email')['id'].transform('min')
#     removed_person = person[person['id'] != min_id] 
#     person.drop(removed_person.index, inplace=True)
#     return

result = delete_duplicate_emails(person)
print(result)