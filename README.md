# reddit_unlocked
A program for analyzing & visualizing data pulled from the Reddit API and scraped from news articles. CS 196 @ Illinois 2017

Pitch Powerpoint: http://bit.ly/2xidFrv
Goals Checklist/Process Outline: http://bit.ly/2h3Ieex

Duties:
- RAKE & Newspaper/Keyword Analysis: Ben & Jayam, Keshav
- PRAW/Data Management: Isaac
- PRAW/Data Visualization: Gary
  
  PRAW: PRAW is a library that we used to gain access to the reddit API, allowing us to pull threads from any subreddit's     section as well as their respective attributes. The format in which PRAW functions is a loop through the top posts of a   particular section ("hot" or "top") of a subreddit, so we added the attributes of the threads to a dataframe within the for   loop.
  
  Plot.ly: The reason we used plot.ly is primarily due to the more aesthetically pleasing features of their graphs, easy conversion from pandas dataframes to whatever graph we wish to do, and also the interactive feature of the graphs. It was also very vital that plot.ly allowed for graphs to be embedded into html and the url to the graph used for embedding into html would be updated with each new graph pulled.
- Website (Flask/HTML/CSS/Bootstrap): Isaac, Ismail
