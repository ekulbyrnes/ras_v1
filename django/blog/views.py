#from django.shortcuts import render
from django.views import generic
from django.shortcuts import render
from .models import Page

# Create your views here.

def index(request):
    return render(request, 'ras_index.html')

class PageList(generic.ListView):
    queryset = Page.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PageDetail(generic.DetailView):
    model = Page
    template_name = 'page_detail.html'
