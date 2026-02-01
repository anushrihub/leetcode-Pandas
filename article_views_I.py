import pandas as pd

views = pd.DataFrame({
    "article_id": [1, 1, 2, 2, 4, 3, 3],
    "author_id":  [3, 3, 7, 7, 7, 4, 4],
    "viewer_id":  [5, 6, 7, 6, 1, 4, 4],
    "view_date":  [
        "2019-08-01",
        "2019-08-02",
        "2019-08-01",
        "2019-08-02",
        "2019-07-22",
        "2019-07-21",
        "2019-07-21"
    ]
})

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]
    df.drop_duplicates('author_id', inplace=True)
    df.sort_values(by = 'author_id', inplace = True)
    df.rename(columns = {'author_id' : 'id'}, inplace=True)
    df = df[['id']]
    return df

result = article_views(views)
print(result)