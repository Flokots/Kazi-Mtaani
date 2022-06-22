from django.shortcuts import render
from .forms import NewsLetterForm

# Create your views here.

def subscribe(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            print('valid')
        else:
            form = NewsLetterForm()
        return render(request, 'subscribe.html', {'form': form})
