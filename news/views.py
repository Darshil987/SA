from django.shortcuts import render,HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .models import NewsData
from textblob import TextBlob
import math
# Create your views here.

def get_news(request):

    html_text=requests.get('https://indianexpress.com/latest-news/').text
    soup = BeautifulSoup(html_text,'html.parser')
    # print(html_text)

    headline_title=soup.find("div", class_="title").text
    headline_link=soup.find("div", class_="title").a["href"]

    main=soup.find_all('p')
    # print(main)
    paragraph = ""
    for p in main:
        paragraph = paragraph + p.text
        #print(p.text)
    
     #-----------------------------------------------------------
        #-----------------------ANALYZING---------------------------
    polarity=0
    subjectivity=0
            
    analyse=TextBlob(paragraph)
    print('Polarity:',analyse.sentiment.polarity)
    polarity=analyse.sentiment.polarity
    polarity=(math.ceil(polarity*1000)/1000)
        
    if polarity > 0 :
        comment = "POSITIVE"
    elif polarity < 0:
        comment = "NEGATIVE"
    else:
        comment = "NEUTRAL"

    print("COMMENT :--->",comment)   
    print('----------------------------------------------------') 
        #-----------------------------------------------------------    
        #-----------------------SAVING------------------------------    
    if NewsData.objects.exists() == True:
        news_all=NewsData.objects.values('Headline_link')
        li = news_all[0]['Headline_link']
        if headline_link != li:       
            result=NewsData(
                Headline_content=paragraph,
                Headline_link=headline_link,
                Headline_title=headline_title,
                Polarity = polarity,
                Comment = comment,
                )
            result.save()
    else:
        result=NewsData(
                Headline_content=paragraph,
                Headline_link=headline_link,
                Headline_title=headline_title,
                Polarity = polarity,
                Comment = comment,
                )
        result.save()    
    
    news_all=NewsData.objects.all()
    return render(request,'news/news.html',{'news':news_all})

# =======================================================================

def refresh(request):
    news_all=NewsData.objects.all()
    news_all.delete()
    return HttpResponseRedirect('/getnews')


def read_news(request):
    HttpResponseRedirect('/news')


def deleteNews(request):
    if request.method=='POST':
        news_all=NewsData.objects.all()
        news_all.delete()
        return HttpResponseRedirect('/news')
    else:
        news_all=NewsData.objects.all()
        news_all.delete()
        return HttpResponseRedirect('/news')

def welcome(request):
    return render(request,'news/welcomeNews.html')
