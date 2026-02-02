import pandas as pd

tweets = pd.DataFrame(
    {
        'tweet_id' : [1, 2],
        'content' : ['Let us Code', 'More than fifteen chars are here!']
    }
)

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    is_valid = tweets['content'].str.len() > 15
    df = tweets[is_valid]
    return df[['tweet_id']]

result = invalid_tweets(tweets)
print(result)