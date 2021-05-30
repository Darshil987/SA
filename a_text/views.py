from django.shortcuts import render, HttpResponseRedirect
from .models import TextInputData
from .forms import TextBodyForm
from textblob import TextBlob

# FOR TEXT 
import re
import nltk
from nltk.corpus import stopwords
# nltk.download('stopwords')
# nltk.download('vader_lexicon')
from nltk.stem.porter import PorterStemmer
from nltk.sentiment.vader import SentimentIntensityAnalyzer


# Create your views here.
def A_Text(request):
    if request.method == 'POST':
        print('POST METHOD CALLED')
        form_ob = TextBodyForm(request.POST)
        if form_ob.is_valid():
            u_keyword = form_ob.cleaned_data['keyword']
            u_text_body = form_ob.cleaned_data['text_body']
            print('KEYWORD---->', u_keyword)

            Subjectivity = 0
            analyse = TextBlob(u_text_body)
            Subjectivity = analyse.sentiment.subjectivity
            
            # analysis
            
            review = re.sub('[^a-zA-Z]', ' ', u_text_body)
            review = review.lower()
            review = review.split() 
            ps = PorterStemmer()
            review = [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
            review = ' '.join(review)
            sid = SentimentIntensityAnalyzer()
            res = sid.polarity_scores(review)
            for i in res:
                if i == 'compound':
                    comp = res[i]

            if comp > 0:
                comment = "Positive"
            elif comp < 0:
                comment = "Negative"
            else:
                comment = "Neutral"

            
            
            # --------------------------------------
                        # ------------------------------------------

            result = TextInputData(text_body=u_text_body, keyword=u_keyword, compound=comp,
                                   subjectivity=Subjectivity, comment=comment)
            result.save()
            form_ob = TextBodyForm()

    else:
        form_ob = TextBodyForm()
    table_data = TextInputData.objects.all()
    return render(request, 'a_text/text.html', {'form': form_ob, 'Textdb': table_data})


# ========================================================

# FUNCTION TO DELETE RESULTS
def delete_text(request, id):
    print('----------------------')
    print('DELETEEEEEEEEEEEEEEEEEEEEEEEEEEE')
    print('----------------------')
    if request.method == 'POST':
        recent_del = TextInputData.objects.get(pk=id)
        recent_del.delete()
        return HttpResponseRedirect('/text')


# =========================================================

# FUNCTION TO VIEW TEXT RESULTS
def view_text(request, id):
    data_view = TextInputData.objects.get(pk=id)

    print('----------------------')
    print('VIEW BUTTON CLICKED')
    print('----------------------')

    return render(request, 'a_text/results.html', {'data': data_view})


def home(request):
    return render(request, 'a_text/welcome.html')
