<!-- # Influencer Enhancer

### Description:

How often have we been hesitant to post a tweet, instagram photo, facebook post only because we were afraid we wouldn't get the feedback we wanted? Well this project aims to help users gain insight on how their posts will be reacted to on their social media platfrom.

### Disclaimer:

This project's scope is aimed at using Twitter. However this can be later on scaled to use Facebook, Instagram, LinkedIn and many other platforms.

In addition, we used Elon Musk's tweets as our mock data.

### Gathering Data:

<ul>

<li>We use <a href = 'https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries/v2'>Twitter API v2</a> to get the tweets along with their corresponding number of retweets and favorites. This requires elevated access. In order to use the number of replies as well we will have to have an even higher access which was outside of this project's scope.
    
<li>We create a csv file that is the raw tweets extracted from the API to process later on.
    
</ul>

### Processing Data:

<ul>

<li> We start with stemming the words in the tweets and removing the stopwords. This is done using Snowball stemmer. 
    
<li> We then create two new csv files with the stemmed tweets. Each of the csv files correspond to the number of retweets and the number of favorites. This logic is used for later uses where the user might want to visualize data separately.
    
<li> We clear any tweets that only have urls, tags, and hashtags. Later on these metrics will be used is future scopes of this project.
    
</ul>

### Model Building:

We used two seperate models that have the same structure yet different outcomes. We instantiated an TF-IDF vectorizer to vectorize the tweets we have. We later feed these tweets to our two models with each targeting the number of favorites and number of retweets respectively. These two models are built using sklearn's Ridge regression. We later dump these models into pickle files for the dash app deployment. -->

### Web app:

This app uses <a href = 'https://plotly.com/dash/'>Plotly</a> dash app.

<img src = 'assets/images/overall webpage detailed.png'></img>

<ol>
<li> Username
<li> Retweets grouped by month
<li> Favorites grouped by month
<li> This updates the tweets in realtime. However it takes time to execute as it recalls all previous tweets as well
<li> Textbox area to enter the tweet to predict it's number of favorites and retweets
<li> This button triggers our two models to predict the corresponding metrics of the tweet specified
<li> Number of favorites predicted
<li> Number of retweets predicted
</ol>