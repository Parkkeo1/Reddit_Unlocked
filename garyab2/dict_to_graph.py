import plotly
plotly.tools.set_credentials_file(username='reddit_unlocked', api_key='gfnXKc7JvUKST4HRJyFX')
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.graph_objs import *
import pandas as pd


#takes a list of dictionaries of keywords from body text as input and returns the url for the plotly html embedding of
#scatterplot made from the keywords and their attributes
def body_to_graph(posts = [], subreddit):
    """
    :type subreddit: String
    """
    data_df = pd.DataFrame(posts)
    trace1 = go.Scatter(
        x = data_df.month_posted,
        y = data_df.score,
        mode = 'markers',
        marker = dict(
            size = (data_df.upvotes + data_df.downvotes) / 200000 * 50,
            color = data_df.polarity,
            colorscale = 'Portland',
            showscale = True
        ),
        text = data_df.keyword + '\n' + data_df.domain
    )
    layout = go.Layout(
        title = 'Stats of top reddit/r/' + subreddit + ' posts',
        xaxis = dict(
            title = 'month_posted',
            ticks = 12,
        ),
        yaxis = dict(
            title = 'score',
            ticklen = 5,
        )
    )
    data = [trace1]
    fig = go.Figure(data = data, layout = layout)
    url = py.plot(fig, filename = 'reddit plot')
    return "" + url