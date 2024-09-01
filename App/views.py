from django.shortcuts import render
from .forms import ClientForm

def home_page(request):
    return render(request, 'home.html')

def services_page(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        try:
            form.save()
        except:
            form.add_error(None, 'Ошибка')
    return render(request, 'services.html', {'form': form})

def contacts_page(request):
    return render(request, 'contacts.html')
