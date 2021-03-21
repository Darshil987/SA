from django.shortcuts import render, HttpResponseRedirect
from .models import TextInputData
from .forms import TextBodyForm
from textblob import TextBlob


# Create your views here.
def A_Text(request):
    if request.method == 'POST':
        print('POST METHOD CALLED')
        form_ob = TextBodyForm(request.POST)
        if form_ob.is_valid():
            u_keyword = form_ob.cleaned_data['keyword']
            u_text_body = form_ob.cleaned_data['text_body']
            print('KEYWORD---->', u_keyword)

            # --------------------------------------
            Polarity = 0
            Subjectivity = 0

            analyse = TextBlob(u_text_body)
            print('Polarity:', analyse.sentiment.polarity)
            print('Subjectivity:', analyse.sentiment.subjectivity)
            Polarity = analyse.sentiment.polarity
            Subjectivity = analyse.sentiment.subjectivity
            if Polarity <= 0.5:
                comment = "POSITIVE"
            if Polarity > 0.5:
                comment = "HIGHLY POSITIVE"
            elif Polarity == 0.0:
                comment = "NEUTRAL"
            elif Polarity >= -0.5:
                comment = "NEGATIVE"
            else:
                comment = "HIGHLY NEGATIVE"

            print("COMMENT :--->", comment)

            if Subjectivity == 0.5:
                comment_s = "NEUTRAL"
            elif Subjectivity > 0.5:
                comment_s = "SUBJECTIVE"
            else:
                comment_s = "OBJECTIVE"

            print("Subjectivity :--->", comment_s)
            print('----------------------')
            print('----------------------')
            # ------------------------------------------

            result = TextInputData(text_body=u_text_body, keyword=u_keyword, polarity=Polarity,
                                   subjectivity=Subjectivity, comment=comment, sub_comment=comment_s)
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
