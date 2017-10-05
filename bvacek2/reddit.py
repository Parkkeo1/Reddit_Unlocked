from bs4 import BeautifulSoup
import json
import requests
import pandas as pd

subreddit = input('Insert subreddit: ' )

site = requests.get('https://reddit.com/r/{}.json'.format(subreddit), headers={'user-agent': 'Mozilla/5.0'}
)

reddit_json = json.loads(site.text)

master_dict = {}

for i in range(0, 19):	
	master_dict[reddit_json['data']['children'][i]['data']['title']] = reddit_json['data']['children'][i]['data']['score']

reddit_df = pd.DataFrame(master_dict, index=[0])

print(reddit_df)
