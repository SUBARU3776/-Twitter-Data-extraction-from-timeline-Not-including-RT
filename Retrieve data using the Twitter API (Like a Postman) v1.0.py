import requests
import pandas as pd

bearer_token = 'Your bearer token key'

headers = {'Authorization': f'Bearer {bearer_token}'}

params = {
    'max_results': '100',
    'expansions': 'author_id',
    'tweet.fields': 'created_at,public_metrics,referenced_tweets',
    'user.fields': 'created_at,public_metrics'
}

user_id = '1315676658314215426'
handle = 'Hidetoshi_H_'
url = f'https://api.twitter.com/2/users/{user_id}/tweets'

response = requests.get(url, headers=headers, params=params)
response.raise_for_status()

data = response.json()

while 'next_token' in data['meta']:
    params['pagination_token'] = data['meta']['next_token']
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data['data'] += response.json()['data']
    data['meta'] = response.json()['meta']

df = pd.DataFrame(data['data'])
metrics_df = pd.DataFrame(df['public_metrics'].tolist())

df = pd.concat([df, metrics_df], axis=1).drop('public_metrics', axis=1)

df.to_csv(f'{handle}.csv', index=False)

print(df.head())