import praw
import matplotlib.pyplot as plt

reddit = praw.Reddit(client_id='UHCBgwhLYPSEeg',
			client_secret='dw7eLPuOBlsQXo5EtWhWiSGgWvk',
			user_agent='Vcrew192')

for submission in reddit.subreddit('news').hot(limit=10):
    print(submission.domain, submission.score)

plt.hist(submission.score)

plt.show
