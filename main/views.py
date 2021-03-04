from django.shortcuts import render
from main.models import Contact
from main.forms import ContactForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ContactForm(request.POST or None)
        if form.is_valid():
            form.save()
            return HttpResponse('OK')
    else:
        form = ContactForm()
        context = {
            'form':form,
        }
    return render(request, 'home.html', {'form':form})
