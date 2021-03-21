from django.contrib import admin
from django.urls import path
from a_tweet import views as vtweet
from a_text import views as vtext
from news import views as vnews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tweet', vtweet.tweet, name='v_tweet'),
    path('chart/<int:id>/', vtweet.view, name='chart'),
    path('', vtext.home, name='home'),
    path('delete/<int:id>/', vtweet.Delete_data, name='deletedata'),
    path('text/', vtext.A_Text, name='AText'),
    path('text/<int:id>', vtext.delete_text, name='deleteText'),
    path('result/<int:id>', vtext.view_text, name='resultText'),
    path('getnews/', vnews.get_news, name='getnews'),
    path('news/', vnews.welcome, name='welcome'),
    path('refresh/', vnews.refresh, name='refresh'),
    path('delete/', vnews.deleteNews, name='deleteNews'),
    path('read/<Headline_title>', vnews.read, name='read'),
]
