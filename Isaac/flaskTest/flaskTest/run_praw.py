import praw
import pandas as pd
from datetime import datetime


# TODO: Make this program faster!

def run_praw(name):
    reddit = praw.Reddit(client_id='Pj5o8QpNXXJY9A',
                         client_secret='pQKMRBmhp0In48NoNvvktfRo2eA',
                         password='prawisgreat',
                         user_agent='Reddit Unlocked CS196 Project @ UIUC',
                         username='RedditUnlocked196')

    subreddit = reddit.subreddit(name)

    threads_df = pd.DataFrame({
        'Title': (),
        'URL': (),
        'Upvote Ratio (%)': (),
        'Net Score': (),
        '# of Upvotes': (),
        '# of Downvotes': (),
        'Post Date': (),
        'Self Post?': (),
        'Video Post?': ()
    })

    threads_df = threads_df[['Title', 'URL', 'Upvote Ratio (%)', 'Net Score', '# of Upvotes', '# of Downvotes',
                             'Post Date', 'Self Post?', 'Video Post?']]

    for thread in subreddit.top('year', limit=5):
        actualUps = int((thread.upvote_ratio * thread.score) / (thread.upvote_ratio * 2 - 1))
        actualDowns = actualUps - thread.score
        #if isinstance(str(datetime.utcfromtimestamp(thread.created_utc)), str):
        #    limitDate = (str(datetime.utcfromtimestamp(thread.created_utc)))[:10]
        #    newDate = limitDate.replace('-', ' ')
        #    time = datetime.strptime(newDate, '%Y %m %d')
        #    formatTime = time.strftime('%b %d, %Y')
        #else:
        #    formatTime = None
        gather = pd.Series([thread.title, thread.url, thread.upvote_ratio * 100, thread.score,
                            actualUps, actualDowns, thread.created_utc,
                            thread.is_self, thread.is_video],
                           index=['Title', 'URL', 'Upvote Ratio (%)', 'Net Score', '# of Upvotes', '# of Downvotes',
                                  'Post Date', 'Self Post?', 'Video Post?'])
        threads_df = threads_df.append(gather, ignore_index=True)

    return threads_df.to_dict(orient='records')
