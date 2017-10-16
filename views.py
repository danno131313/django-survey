from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'survey_app/index.html')

def result(request):
    context = {
        'name':     request.session['name'],
        'location': request.session['location'],
        'lang':     request.session['lang'],
        'comment':  request.session['comment'],
    }
    return render(request, 'survey_app/result.html', context, messages)

def process(request):
    messages.add_message(request, messages.SUCCESS, "Thank you for submitting!")
    request.session['name']     = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['lang']     = request.POST['lang']
    request.session['comment']  = request.POST['comment']
    return redirect('/survey/result')
