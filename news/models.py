from django.db import models

# Create your models here.
class NewsData(models.Model):
	Headline_content=models.TextField(null=False)
	Headline_link=models.CharField(max_length=200,null=False,blank=False)
	Headline_title=models.CharField(max_length=200,null=False,blank=False)

	Polarity=models.FloatField(null=True,blank=False)
	Comment=models.CharField(null=True,blank=False,max_length=20)