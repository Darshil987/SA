from django.contrib import admin
from .models import TextInputData
# Register your models here.

@admin.register(TextInputData)

class TextInputDataAdmin(admin.ModelAdmin):
	list_display=('keyword','text_body','compound','subjectivity','comment')