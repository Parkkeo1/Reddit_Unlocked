### Libraries We Used

##### PRAW - Python Wrapper For The Reddit API
PRAW is a library that we used to gain access to the reddit API, allowing us to pull threads from any subreddit's section as well as their respective attributes. The format in which PRAW functions is a loop through the top posts of a particular section ("hot" or "top") of a subreddit, so we added the attributes of the threads to a dataframe within the for loop. -Gary

##### Pandas 
With its fast and easy-to-use data structures and data organization functions, Pandas was an invaluable library in storing and sorting extensive subreddit, submission, and keyword data that we gathered from the Reddit API. Specifically, we opted to use Pandas dataframes for their speed and intuitive structure compared to standard Python dictionaries and lists. -Isaac

##### Newspaper 
We used this package to parse through the HTML markup of any URL we passed to it. Newspaper is built to handle news articles, so if we detected that a Reddit post had an article linked to it, we were able to use newspaper to parse through the text in the article and extract keywords with Newspaper's built-in keywords method. -Jayam

##### RAKE - Rapid Automatic Keyword Extraction
The Rapid Automatic Keyword Extraction (RAKE) library allows us to pass in standalone strings (as opposed to URLs that point to articles) to analyze for keywords. This library's algorithm looks at the frequency of word appearance and co-occurrence with other words inside a text to determine which words describe the text as a whole. The library proved useful in analyzing Reddit post titles, which we were able to directly obtain as strings. -Jayam

##### TextBlob
Sentiment Analysis Library Based on NLTK (WIP description/docs)

##### Plotly
The reason we used plot.ly is primarily due to the more aesthetically pleasing features of their graphs, easy conversion from pandas dataframes to whatever graph we wish to do, and also the interactive feature of the graphs. It was also very vital that plot.ly allowed for graphs to be embedded into html and the url to the graph used for embedding into html would be updated with each new graph pulled. -Gary

##### Flask
From the start, we knew we wanted to deploy our program onto a dynamic website. After some research and recommendations from upperclassmen, we decided to use Flask. Flask enabled us to integrate the front-end HTML and CSS with the back-end Python program. Flask's sessions utility was especially useful because it allowed the saving and transfer of (data) variables across multiple pages in the website. -Isaac

##### Flask-Session
In the final stages to combining the back-end with the front-end website using Flask, I ran into a problem: the default client-side 4KB-size cookie that Flask provided for transfering data across different pages could not store all of the necessary Reddit and keyword data we need to run the program. Thus, I opted to use Flask-Session, a Flask plugin that enabled me to implement a server-side filesystem cookie system that was able to save all of the data needed thanks to its greater size. -Isaac

##### Bootstrap
Since this was my first time learning HTML and CSS, I decided to use Bootstrap to ease my introduction to web development. With its built-in utilities and components, I developed a functional front-end without having to write CSS from scratch. -Isaac
