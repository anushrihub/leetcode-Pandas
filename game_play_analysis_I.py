import pandas as pd

activity = pd.DataFrame(
    {
    "player_id": [1, 1, 2, 3, 3],
    "device_id": [2, 2, 3, 1, 4],
    "event_date": ["2016-03-01", "2016-05-02", "2017-06-25", "2016-03-02", "2018-07-03"],
    "games_played": [5, 6, 1, 0, 5]
})

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    # Group by player_id and select only event_date, then take the minimum (earliest) date per player
    df = activity.groupby('player_id')['event_date'].min()
    # Reset index to turn player_id from index back into a regular column
    df = df.reset_index()
    # Rename event_date to first_login to reflect that it represents each player's first login date
    return df.rename(columns={'event_date': 'first_login'})

result = game_analysis(activity)
print(result)