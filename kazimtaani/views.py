from django.http import HttpResponseRedirect
from django.shortcuts import render

from kazimtaani.models import NewsLetterRecipients
from .forms import NewsLetterForm

# Create your views here.

def index(request):
    return render(request, 'index.html')

def subscribe(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form.save()
            name=form.cleaned_data['name']
            email=form.cleaned_data['email']

            recipient=NewsLetterRecipients(name=name, email=email)
            recipient.save()
            HttpResponseRedirect('index')
            print('valid')
        else:
            form = NewsLetterForm()
        return render(request, 'subscribe.html', {'form': form})
