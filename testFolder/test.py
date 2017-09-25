from bs4 import BeautifulSoup
import json
import requests

subreddit = input('Insert subreddit: ' )

site = requests.get('https://reddit.com/r/{}.json'.format(subreddit), headers={'user-agent': 'Mozilla/5.0'}
)

reddit_json = json.loads(site.text)

master_dict = {}

for i in range(0, 19):	
	master_dict[reddit_json['data']['children'][i]['data']['domain']] = reddit_json['data']['children'][i]['data']['score']

print(master_dict)
