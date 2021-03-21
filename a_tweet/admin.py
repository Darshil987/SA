from django.contrib import admin
from .models import InputData
# Register your models here.


@admin.register(InputData)
class InputDataAdmin(admin.ModelAdmin):
	list_display=('id','topic','no_tweets','pos','neg','neutral')