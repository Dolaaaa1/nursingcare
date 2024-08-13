from django.shortcuts import render ,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .forms import PatientRequestForm
from django.views.generic import TemplateView
from .models import *
from django.views import View

# Create your views here.

def login(request):
    return render(request,'Login.html')

def profile(request):
    return render(request,'Profile.html')

def signup(request):
    return render(request,'Signup.html')


class ListItem(ListView):
    model = Sections
    template_name = 'base.html'
    
    
    def get_queryset(self):
        return Sections.objects.all().order_by('-id')
    
class SectionsDetailView(View):
    def get(self, request, pk):
        section = Sections.objects.get(pk=pk)
        form = PatientRequestForm()
        return render(request, 'sections_detali.html', {'section': section, 'form': form})

    def post(self, request, pk):
        section = Sections.objects.get(pk=pk)
        form = PatientRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # تأكد من استبدال `success_url` بمسار صالح
        return render(request, 'sections_detali.html', {'section': section, 'form': form})
    
    
    


class SuccessView(TemplateView):
    template_name = 'success.html'


    

class AboutUsView(TemplateView):
    template_name = 'about_us.html'



