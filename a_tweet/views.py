import base64, io, urllib

from django.shortcuts import render, HttpResponseRedirect
from .forms import AnalyzeTweets
from .models import InputData

from textblob import TextBlob
import tweepy
from matplotlib import pyplot as plt


# Create your views here.

def tweet(request):
    if request.method == 'POST':
        fmo = AnalyzeTweets(request.POST)
        if fmo.is_valid():
            u_topic = fmo.cleaned_data['topic']
            u_no_tweets = fmo.cleaned_data['no_tweets']

            # print('TOPIC:',u_topic)

            # ------------------------------------------------------
            def percentage(part, whole):
                return 100 * float(part) / float(whole)

            # ------------------------------------------------------
            # variables that contain user credentials used to access twitter API
            consumerKey = "ep0JHxcW9dkutUk2F5xhpOtPR"
            consumerSecret = "l19qUhuxnkRxRUBOSf9rDYMmHYQcWDjsVzSq5C36YkomZfFGHZ"
            accessToken = "1265513188893786113-Ne0HMrV5aXUAcTV5XJ9p2tdX2iLXBh"
            accessTokenSecret = "f4MMIC9sQQMljTM16j6Ig7Vbj0cpKrusFO691o3m9nEU6"
            # ----------------------------------------------------------------
            auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
            auth.set_access_token(accessToken, accessTokenSecret)
            api = tweepy.API(auth)

            searchTerm = u_topic
            numofsearchterms = int(u_no_tweets)

            tweets = tweepy.Cursor(api.search, q=searchTerm).items(numofsearchterms)

            positive = 0
            negative = 0
            neut = 0
            polarity = 0

            for tweet in tweets:

                analysis = TextBlob(tweet.text)
                polarity += analysis.sentiment.polarity

                if (analysis.sentiment.polarity == 0):
                    neut += 1
                elif (analysis.sentiment.polarity < 0.00):
                    negative += 1
                elif (analysis.sentiment.polarity > 0.00):
                    positive += 1

            positive = percentage(positive, numofsearchterms)
            negative = percentage(negative, numofsearchterms)
            neut = percentage(neut, numofsearchterms)

            positive = format(positive, '.2f')
            negative = format(negative, '.2f')
            neut = format(neut, '.2f')

            print('POSITIVE:', positive)
            print("NEGATIVE:", negative)
            print("NEUTRAL:", neut)

            result = InputData(topic=u_topic, no_tweets=u_no_tweets, pos=positive, neg=negative, neutral=neut)
            result.save()
            fmo = AnalyzeTweets()

    else:
        fmo = AnalyzeTweets()

    Input_Data = InputData.objects.all()
    return render(request, 'a_tweet/twitter.html', {'form': fmo, 'InputData': Input_Data})


# ===================================================================================


# delete function
def Delete_data(request, id):
    if request.method == 'POST':
        recent_del = InputData.objects.get(pk=id)
        recent_del.delete()
        return HttpResponseRedirect('/tweet')


#  ===================================================================================


# view function
def view(request, id):
    if request.method == 'POST':
        x = InputData.objects.get(pk=id)
        topic = x.topic
        numofsearch = x.no_tweets
        pos = x.pos
        neg = x.neg
        neut = x.neutral

        labels = ['POSITIVE[' + str(pos) + '%]', 'NEUTRAL[' + str(neut) + '%]', 'NEGATIVE[' + str(neg) + '%]']
        sizes = [pos, neut, neg]
        myexplode = [0.1, 0, 0]
        colors = ['green', 'gold', 'red']
        patches, texts = plt.pie(sizes, colors=colors, explode=myexplode)
        plt.legend(patches, labels, loc="best")
        plt.title("People's reaction on " + topic + " by analyzing " + str(numofsearch) + " Tweets.")
        plt.axis('equal')
        plt.tight_layout()
        plt.show()

        return HttpResponseRedirect('/tweet')
