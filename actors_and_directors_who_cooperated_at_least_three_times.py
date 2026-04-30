import pandas as pd


actor_director = pd.DataFrame({
    'actor_id':    [1, 1, 1, 1, 1, 2, 2],
    'director_id': [1, 1, 1, 2, 2, 1, 1],
    'timestamp':   [0, 1, 2, 3, 4, 5, 6]
})



def actors_and_directors(actor_director: pd.DataFrame):
    df = actor_director.groupby(['actor_id','director_id'])['timestamp'].count().reset_index(name = 'cnt')
    df = df[df['cnt']>=3][['actor_id','director_id']]
    return df


result = actors_and_directors(actor_director)
print(result)
