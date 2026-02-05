import pandas as pd

users = pd.DataFrame({
        'user_id':[1, 2, 3, 4, 5, 6, 7],
        'name': [
        "Winston",
        "Jonathan",
        "Annabelle",
        "Sally",
        "Marwan",
        "David",
        "Shapiro"
    ],
        'mail': [
        "winston@leetcode.com",
        "jonathanisgreat",
        "bella-@leetcode.com",
        "sally.come@leetcode.com",
        "quarz#2020@leetcode.com",
        "david69@gmail.com",
        ".shapo@leetcode.com"
    ]
})

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    valid_mail = users[users['mail'].str.match('^[A-Za-z][A-Za-z0-9_\.\-]*@leetcode(\?com)?\.com$')]
    return valid_mail

result = valid_emails(users)
print(result)