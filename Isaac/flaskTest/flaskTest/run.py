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

    for thread in subreddit.hot(limit=5): # TODO: change limit number when actually deploying program. 15 is the testing number.
        if thread.is_video:
            continue
        if 'fb' in thread.url:
            continue
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
    url = py.plot(fig, filename='reddit plot', auto_open=False)
    return "" + url

import operator
import rake as rake
rake_object = rake.Rake("SmartStoplist.txt", 1, 2, 1)
from textblob import TextBlob, Word, Blobber
import newspaper
from newspaper import Article
import numpy as np

def get_keyword_dict(input_dict):
    # Transforms dict returned by display_praw into DataFrame for working with
    top10news_df = pd.DataFrame.from_dict(input_dict)

    words = {}

    ## NEWSPAPER STUFF HERE ##

    # Get keywords out of all articles
    for i in range(len(top10news_df)):
        if "self" in top10news_df.iloc[i]["Domain"]:
            continue
        elif "youtube" in top10news_df.iloc[i]["Domain"]:
            continue
        elif "imgur" in top10news_df.iloc[i]["Domain"]:
            continue

        myArticle = Article(top10news_df.iloc[i]['URL'])
        try:
            myArticle.download()
            myArticle.parse()
        except:
            continue
        myArticle.nlp()

        # Run sentiment analysis on each article, fetch subjectivity and polarity
        text = myArticle.text
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Get associated Reddit post info for each keyword, store in dictionary
        for keyword in myArticle.keywords:

            # Don't waste time with numeric keywords, skip them if they contain numbers
            if any(char.isdigit() for char in keyword):
                continue        
                
                
            if keyword not in words:
                words[keyword] = [keyword, 1, 
                                  top10news_df.iloc[i]['# of Upvotes'],
                                  top10news_df.iloc[i]["# of Downvotes"], 
                                  top10news_df.iloc[i]["Net Score"],
                                  subjectivity, polarity, 
                                  {(top10news_df.iloc[i]["Domain"]):1}]
            else:
                words[keyword][1] += 1
                words[keyword][2] += top10news_df.iloc[i]['# of Upvotes']
                words[keyword][3] += int(top10news_df.iloc[i]['# of Downvotes'])
                words[keyword][4] += int(top10news_df.iloc[i]['Net Score'])
                words[keyword][5] = np.mean([subjectivity, words[keyword][5]])
                words[keyword][6] = np.mean([polarity, words[keyword][6]])
                if top10news_df.iloc[i]["Domain"] in words[keyword][7]:
                    words[keyword][7][(top10news_df.iloc[i]["Domain"])] += 1
                else:
                    words[keyword][7][top10news_df.iloc[i]["Domain"]] = 1

        ## RAKE STUFF HERE ##

        # Pull keywords from title strings
        for wordPair in rake_object.run(top10news_df.iloc[i]['Title']):
            currentWord = wordPair[0]

            # Don't waste time with numeric keywords, skip them if they contain numbers
            if any(char.isdigit() for char in currentWord):
                continue

            # Grab associated Reddit post data for each keyword, store in dictionary
            if currentWord not in words:
                words[currentWord] = [currentWord, 1, 
                                  top10news_df.iloc[i]['# of Upvotes'],
                                  top10news_df.iloc[i]["# of Downvotes"], 
                                  top10news_df.iloc[i]["Net Score"],
                                  subjectivity, polarity, 
                                  {(top10news_df.iloc[i]["Domain"]):1}]
            else:
                words[currentWord][1] += 1
                words[currentWord][2] += int(top10news_df.iloc[i]['# of Upvotes'])
                words[currentWord][3] += int(top10news_df.iloc[i]['# of Downvotes'])
                words[currentWord][4] += int(top10news_df.iloc[i]['Net Score'])
                if top10news_df.iloc[i]["Domain"] in words[currentWord][7]:
                    words[currentWord][7][(top10news_df.iloc[i]["Domain"])] += 1
                else:
                    words[currentWord][7][top10news_df.iloc[i]["Domain"]] = 1


    ### FOR GARY'S USE ###
    # Output dictionary is named 'words' #
    # Format is as such: #
    # key = keyword #
    # value = [Occurences, Upvotes, Downvotes, Score, Subjectivity, Polarity, Domain Dictionary] #
    
    return words