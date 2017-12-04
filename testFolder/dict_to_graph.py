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