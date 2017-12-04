import praw
import pandas as pd
from datetime import datetime


# TODO: Make this program faster! (a lot faster, this is way too slow)

def display_praw(name):
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
        'Video Post?': (),
        'Domain': ()
    })

    threads_df = threads_df[['Title', 'URL', 'Upvote Ratio (%)', 'Net Score', '# of Upvotes', '# of Downvotes',
                             'Post Date', 'Self Post?', 'Video Post?', 'Domain']]

    for thread in subreddit.top('year', limit=15): # TODO: change limit number when actually deploying program. 15 is the testing number.
        actualUps = int((thread.upvote_ratio * thread.score) / (thread.upvote_ratio * 2 - 1))
        actualDowns = actualUps - thread.score
        gather = pd.Series([thread.title, thread.url, thread.upvote_ratio * 100, thread.score,
                            actualUps, actualDowns, thread.created_utc,
                            thread.is_self, thread.is_video, thread.domain],
                           index=['Title', 'URL', 'Upvote Ratio (%)', 'Net Score', '# of Upvotes', '# of Downvotes',
                                  'Post Date', 'Self Post?', 'Video Post?', 'Domain'])
        threads_df = threads_df.append(gather, ignore_index=True)

    threads_dict = threads_df.to_dict(orient='records')

    for entry in threads_dict:
        if isinstance(str(entry['Post Date']), str):
            time = datetime.fromtimestamp(entry['Post Date'])
            formatTime = time.strftime('%b %d, %Y')
        else:
            formatTime = None

        entry['Post Date'] = formatTime

    return threads_dict


def stats_praw(name):
    reddit = praw.Reddit(client_id='Pj5o8QpNXXJY9A',
                         client_secret='pQKMRBmhp0In48NoNvvktfRo2eA',
                         password='prawisgreat',
                         user_agent='Reddit Unlocked CS196 Project @ UIUC',
                         username='RedditUnlocked196')

    info = reddit.request('GET', '/r/' + name + '/about.json')

    infoDict = {}

    infoDict['Current Users'] = info['data']['active_user_count']
    infoDict['Creation Date'] = (datetime.fromtimestamp(info['data']['created_utc'])).strftime('%b %d, %Y')
    infoDict['Subscriber Count'] = info['data']['subscribers']
    infoDict['Title'] = info['data']['title']
    infoDict['Icon'] = info['data']['icon_img']

    return infoDict

import plotly
plotly.tools.set_credentials_file(username='reddit_unlocked', api_key='gfnXKc7JvUKST4HRJyFX')
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
#takes a dictionary of dictionaries of keywords from body text as input and returns the url for the plotly html embedding of
#scatterplot made from the keywords and their attributes
#'Keyword','Occurences', 'Upvotes', 'Downvotes',  "Score", "Subjectivity", "Polarity", "Domain"


def body_to_graph(words = {}, subreddit = str):
    """
    :type subreddit: String
    """
    frames = []
    #Turns dictionary of dictionaries into list of dataframes
    for key, value in words.items():
        frames.append(pd.DataFrame(data = value, columns = [key], index = ['Keyword','Occurences', 'Upvotes', 'Downvotes', 'Score', 'Subjectivity', 'Polarity', 'Domain']).transpose())
    #Concatenates the list of dataframes
    data_df = pd.concat(frames)
    trace1 = go.Scatter(
        y = data_df.Subjectivity, #Subjectivity of the text the keyword was found in on y axis
        x = data_df.Occurences * data_df.Score,#Occurrences * Score on x-axis for more spread out data
        mode = 'markers',
        marker = dict(
            size =  (data_df.Occurences) * 20, #Occurrences of Keyword for size
            color = data_df.Polarity, #Polarity for color of the post (blue is sad, red is happy)
            colorscale = 'Portland',
            showscale = True
        ),
        text = "Keyword: " + data_df.Keyword
    )
    layout = go.Layout(
        annotations=Annotations([
            Annotation(
                x=0.5,
                y=-0.123,
                showarrow=False,
                text='(Occurrences * Score)',
                xref='paper',
                yref='paper'
            ),
            Annotation(
                x=1.055,
                y=0.5,
                showarrow=False,
                text='Text Polarity',
                textangle=-90,
                xref='paper',
                yref='paper'
            ),
            Annotation(
                x=.01,
                y=1,
                showarrow=False,
                text='Size = Occurrences',
                textangle=0,
                xref='paper',
                yref='paper',
                bordercolor = '#1f77b4',
                font=dict(
                    family='Courier New, monospace',
                    size=16,
                    color='#ff7f0e'
                )
            )
        ]),
        title = 'Stats of top reddit/r/' + subreddit + ' keywords',
        yaxis = dict(
            title = 'Subjectivity',
            ticks = 5,
        ),
        xaxis = dict(
            title = 'popularity',
            ticklen = 10,
        )
    )
    data = [trace1]
    fig = go.Figure(data = data, layout = layout)
    url = py.plot(fig, filename = 'reddit plot')
    return "" + url