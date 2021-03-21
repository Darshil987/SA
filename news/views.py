from django.shortcuts import render,HttpResponseRedirect
from bs4 import BeautifulSoup
import requests
from .models import NewsData
from textblob import TextBlob
import math
# Create your views here.


def get_news(request):

	
	html_text=requests.get('https://indianexpress.com/section/india/').text
	soup=BeautifulSoup(html_text,'lxml')
	headlines=soup.find_all('div',class_='articles')
	for headline in headlines :

		news_date=headline.find('div',class_='date').text
		headline_title=headline.find('h2',class_='title').text
		headline_link=headline.find('h2',class_='title').a['href']
		headline_overview=headline.find('p').text

		
		#-------------------GETTING CONTENT------------------------
		
		html_text2=requests.get(headline_link).text
		soup2=BeautifulSoup(html_text2,"lxml")

		article=soup2.find("div",class_="articles")
		content=article.find(id="pcl-full-content")
		# print(content)
		paras=content.find_all("p")
		# print(paras)
		paragraph=""
		for p in paras:
		    paragraph=paragraph+ p.text
		    # print(p.text)
		#-----------------------------------------------------------
		#-----------------------ANALYZING---------------------------
		polarity=0
		subjectivity=0
			
		analyse=TextBlob(paragraph)
		print('Polarity:',analyse.sentiment.polarity)
		polarity=analyse.sentiment.polarity
		polarity=(math.ceil(polarity*1000)/1000)
		
		if polarity<=0.5 :
			comment="POSITIVE"
		if polarity>0.5:
			comment="HIGHLY POSITIVE"
		elif polarity==0.0:
			comment="NEUTRAL"
		elif polarity >=-0.5:
			comment="NEGATIVE"
		else:
			comment="HIGHLY NEGATIVE"

		print("COMMENT :--->",comment)   
		print('----------------------------------------------------') 
		#-----------------------------------------------------------    
		#-----------------------SAVING------------------------------    
		result=NewsData(
			Headline_content=paragraph,
			Headline_link=headline_link,
			Headline_title=headline_title,
			Polarity=polarity,
			Comment=comment,
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

def read(request,id):
	content_view=NewsData.objects.get(pk=id)
	return render(request,'a_text/read.html',{'content':content_view})