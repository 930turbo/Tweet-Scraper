# Tweet-Scraper

This program uses the Python library "tweepy" to access the Twitter API and "pandas" to create and manipulate a dataframe to store the scraped tweets. The program prompts the user to input a hashtag or topic to track, and then uses the "Cursor" object provided by the tweepy library to scrape tweets that contain that topic or hashtag.

First, the program imports the necessary libraries, tweepy, pandas, datetime

Next, it defines the Twitter API credentials, which are required to authenticate the program with the Twitter API. The consumer_key, consumer_secret, access_token, and access_token_secret are used to authenticate the program. These credentials can be obtained by creating a developer account on the Twitter Developer website.

Then, it creates an OAuth2 object by passing the consumer_key and consumer_secret to tweepy.OAuthHandler, and sets the access_token and access_token_secret using the set_access_token method. This object is used to authenticate the program with the Twitter API.

The user is prompted to input the topic or hashtag, it uses the api.search_tweets method and the "Cursor" object provided by tweepy to scrape tweets that contain the user-specified topic or hashtag. It limits the results to tweets in the english language, since_id is set to Jan 1st, 2021 and the number of tweets scraped to 100.

The tweets are then stored in a list, where each element of the list is a list containing the screen name of the user who tweeted the tweet, the location of the user, and the text of the tweet.

The tweets are then used to create a pandas dataframe with columns "Username", "Location", and "Text". The tweets list is passed as data and the columns are specified in the columns argument

The dataframe is then saved as a CSV file. The filename is created by concatenating the topic and the current date in the format of topic_year-month-day. The dataframe is saved to the current directory with the specified filename, with index set to false

The program then prints a message indicating the location of the saved file.

It is worth noting that the number of requests that can be made to the twitter API per time range is limited, this is called rate limiting, and exceeding the limit can cause errors. Also, the since_id and tweets count to scrape are adjustable values
