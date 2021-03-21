from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class TextInputData(models.Model):
	text_body=RichTextField(null=False)
	keyword=models.CharField(max_length=20,null=False,blank=False)
	polarity=models.FloatField(null=True,blank=False)
	subjectivity=models.FloatField(null=True,blank=False)
	comment=models.CharField(null=True,blank=False,max_length=20)
	sub_comment=models.CharField(null=True,blank=False,max_length=20)
